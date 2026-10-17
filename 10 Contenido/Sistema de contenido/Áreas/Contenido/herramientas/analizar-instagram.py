#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ordena el rendimiento de lo publicado en Instagram. Ordena, no opina.

    python Áreas/Contenido/herramientas/analizar-instagram.py                    # el crudo más nuevo
    python Áreas/Contenido/herramientas/analizar-instagram.py <archivo.json|.csv>

Lee una de estas dos fuentes, la que haya:

1. **Un export de Meta Business Suite** (Estadísticas → Contenido → últimos 90 días → Exportar,
   en .csv), guardado en `Empresa/Datos y feedback/Crudos/aaaa-mm-instagram.csv`. Es el camino de
   todos los días: no necesita ninguna conexión. Las columnas se reconocen por nombre, en español
   o en inglés, así que no importa el orden.
2. **Un JSON** `aaaa-mm-instagram.json` en la misma carpeta, si algún día se conecta la API de
   Instagram con un script propio (lista de piezas con fecha, tipo, enlace, pie, alcance,
   guardados, comentarios, likes y compartidos).

Imprime en Markdown, listo para pegar en el informe de investigación:

- Las 10 que más se mandaron: **compartidos sobre alcance**. Que te manden es la señal más fuerte
- El **múltiplo** de cada pieza: su alcance sobre la mediana de la cuenta. Más de 3x es una señal;
  menos de 1,5x es un día normal
- Las 10 mejores por **tasa de guardado** (guardados / alcance) — la señal más fuerte de que una
  pieza sirvió. Se ordena por tasa y no por guardados totales para no premiar solo lo que el
  algoritmo empujó
- Las 10 mejores por alcance, y las 10 peores (con alcance) — lo que no hay que repetir
- El rendimiento promedio **por formato** (reel, carrusel, imagen) y **por día de la semana**
- El rendimiento según el **largo del pie**

Las piezas sin alcance (más de dos años, Instagram no da datos) se cuentan aparte, no como cero.
"""
import csv
import glob
import json
import os
import statistics
import sys
from datetime import datetime

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
CRUDOS = os.path.join(RAIZ, "Empresa", "Datos y feedback", "Crudos")
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

# Nombres posibles de cada columna en el export de Meta Business Suite
COLUMNAS = {
    "fecha": ["hora de publicación", "fecha de publicación", "publish time", "date"],
    "tipo": ["tipo de publicación", "tipo de contenido", "post type", "type"],
    "enlace": ["enlace permanente", "permalink", "link"],
    "pie": ["descripción", "description", "título", "title", "caption"],
    "alcance": ["alcance", "reach", "cuentas alcanzadas"],
    "guardados": ["guardados", "saves", "saved"],
    "comentarios": ["comentarios", "comments"],
    "likes": ["me gusta", "likes", "reacciones"],
    "compartidos": ["veces que se compartió", "compartidos", "shares"],
}


def numero(v):
    if v in (None, ""):
        return None
    try:
        return int(float(str(v).replace(".", "").replace(",", ".")))
    except ValueError:
        return None


def leer_csv(ruta):
    with open(ruta, encoding="utf-8-sig") as f:
        filas = list(csv.DictReader(f))
    if not filas:
        sys.exit("El CSV está vacío.")
    cab = {c.lower().strip(): c for c in filas[0].keys()}

    def col(clave):
        for nombre in COLUMNAS[clave]:
            for c_low, c in cab.items():
                if c_low.startswith(nombre):
                    return c
        return None

    mapa = {k: col(k) for k in COLUMNAS}
    if not mapa["alcance"]:
        sys.exit("No encontré la columna de alcance en el CSV. Columnas: %s" % list(cab.values()))
    piezas = []
    for f in filas:
        pie = (f.get(mapa["pie"]) or "") if mapa["pie"] else ""
        fecha = (f.get(mapa["fecha"]) or "") if mapa["fecha"] else ""
        piezas.append({
            "fecha": normalizar_fecha(fecha),
            "tipo": (f.get(mapa["tipo"]) or "—") if mapa["tipo"] else "—",
            "enlace": f.get(mapa["enlace"]) if mapa["enlace"] else None,
            "gancho": pie.strip().split("\n")[0][:120],
            "largo_del_pie": len(pie),
            **{k: numero(f.get(mapa[k])) if mapa[k] else None
               for k in ("alcance", "guardados", "comentarios", "likes", "compartidos")},
        })
    return piezas


def normalizar_fecha(texto):
    texto = texto.strip()
    for formato in ("%Y-%m-%d", "%m/%d/%Y %H:%M", "%d/%m/%Y %H:%M", "%Y-%m-%dT%H:%M:%S%z",
                    "%m/%d/%Y", "%d/%m/%Y"):
        try:
            return datetime.strptime(texto[:len(texto)], formato).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return texto[:10]


def leer(ruta):
    if ruta.lower().endswith(".csv"):
        return leer_csv(ruta), None
    with open(ruta, encoding="utf-8") as f:
        sobre = json.load(f)
    datos = sobre.get("datos", sobre)
    return datos.get("piezas", []), datos.get("cuenta")


def tasa(p):
    if p.get("alcance") and p.get("guardados") is not None:
        return p["guardados"] / p["alcance"]
    return None


MEDIANA = [1]


def compartida(p):
    if p.get("alcance") and p.get("compartidos") is not None:
        return p["compartidos"] / p["alcance"]
    return None


def fila(p):
    t = tasa(p)
    c = compartida(p)
    gancho = (p.get("gancho") or "").replace("|", "/") or "(sin pie)"
    enlace = p.get("enlace")
    gancho = "[%s](%s)" % (gancho, enlace) if enlace else gancho
    return "| %s | %s | %s | %s | %.1fx | %s | %s | %s | %s |" % (
        fecha_uy(p.get("fecha")), p.get("tipo") or "—", gancho,
        p.get("alcance") or "—", (p.get("alcance") or 0) / MEDIANA[0],
        "%.2f%%" % (c * 100) if c is not None else "—",
        p.get("guardados") if p.get("guardados") is not None else "—",
        "%.1f%%" % (t * 100) if t is not None else "—", p.get("comentarios") or 0)


def fecha_uy(f):
    try:
        return datetime.strptime(f, "%Y-%m-%d").strftime("%d/%m/%Y")
    except (TypeError, ValueError):
        return f or "—"


CABEZA = ("| Fecha | Formato | Gancho (primera línea del pie) | Alcance | Múltiplo | Compartidos / alcance "
          "| Guardados | Tasa de guardado | Comentarios |\n|---|---|---|---|---|---|---|---|---|")


def grupo(piezas, clave):
    grupos = {}
    for p in piezas:
        grupos.setdefault(clave(p), []).append(p)
    lineas = ["| Grupo | Piezas | Alcance mediano | Tasa de guardado mediana | Comentarios promedio |",
              "|---|---|---|---|---|"]
    for g, ps in sorted(grupos.items(), key=lambda x: -len(x[1])):
        tasas = [tasa(p) for p in ps if tasa(p) is not None]
        lineas.append("| %s | %d | %s | %s | %.1f |" % (
            g, len(ps), int(statistics.median([p["alcance"] for p in ps])),
            "%.1f%%" % (statistics.median(tasas) * 100) if tasas else "—",
            statistics.mean([p.get("comentarios") or 0 for p in ps])))
    return "\n".join(lineas)


def dia(p):
    try:
        return DIAS[datetime.strptime(p["fecha"], "%Y-%m-%d").weekday()]
    except (KeyError, TypeError, ValueError):
        return "—"


def largo(p):
    n = p.get("largo_del_pie") or 0
    return "corto (<300)" if n < 300 else "medio (300-900)" if n < 900 else "largo (900+)"


def main():
    if len(sys.argv) > 1:
        ruta = sys.argv[1]
    else:
        candidatos = sorted(glob.glob(os.path.join(CRUDOS, "*-instagram.json")) +
                            glob.glob(os.path.join(CRUDOS, "*-instagram.csv")))
        if not candidatos:
            sys.exit("No hay datos de Instagram en %s.\n"
                     "Exportá el .csv de Meta Business Suite (Estadísticas → Contenido → Exportar)\n"
                     "y guardalo ahí como aaaa-mm-instagram.csv, o pasá la ruta del archivo." % CRUDOS)
        ruta = candidatos[-1]

    piezas, cuenta = leer(ruta)
    con = [p for p in piezas if p.get("alcance")]
    sin = len(piezas) - len(con)

    print("## Fuente\n")
    print("`%s` · %d piezas, %d con datos, %d sin alcance (más de 2 años o sin insights)\n"
          % (os.path.relpath(ruta, RAIZ), len(piezas), len(con), sin))
    if cuenta:
        print("Cuenta: @%s · %s seguidores · %s publicaciones\n" % (
            cuenta.get("username"), cuenta.get("followers_count"), cuenta.get("media_count")))
    if not con:
        sys.exit("Ninguna pieza trae alcance: no hay nada que ordenar.")

    print("**Medianas de la cuenta:** alcance %d · tasa de guardado %s\n" % (
        statistics.median([p["alcance"] for p in con]),
        "%.1f%%" % (statistics.median([tasa(p) for p in con if tasa(p) is not None]) * 100)
        if any(tasa(p) is not None for p in con) else "—"))

    MEDIANA[0] = statistics.median([p["alcance"] for p in con]) or 1
    print("## Las 10 que más se mandaron (compartidos sobre alcance)\n")
    print(CABEZA)
    mandadas = [p for p in con if compartida(p)]
    for p in sorted(mandadas, key=compartida, reverse=True)[:10]:
        print(fila(p))
    if not mandadas:
        print("| Sin datos de compartidos en esta fuente | | | | | | | | |")
    print("\n## Las 10 que más se guardaron (por tasa)\n")
    print(CABEZA)
    for p in sorted([p for p in con if tasa(p) is not None], key=tasa, reverse=True)[:10]:
        print(fila(p))
    print("\n## Las 10 de más alcance\n")
    print(CABEZA)
    for p in sorted(con, key=lambda p: p["alcance"], reverse=True)[:10]:
        print(fila(p))
    print("\n## Las 10 de menos alcance\n")
    print(CABEZA)
    for p in sorted(con, key=lambda p: p["alcance"])[:10]:
        print(fila(p))
    print("\n## Por formato\n")
    print(grupo(con, lambda p: p.get("tipo") or "—"))
    print("\n## Por día de la semana\n")
    print(grupo(con, dia))
    print("\n## Por largo del pie\n")
    print(grupo(con, largo))


if __name__ == "__main__":
    main()
