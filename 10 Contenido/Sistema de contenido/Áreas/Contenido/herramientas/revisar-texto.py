#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Revisa un pie (o cualquier texto público) contra las reglas de la marca antes de publicarlo.

    python Áreas/Contenido/herramientas/revisar-texto.py pie.txt
    python Áreas/Contenido/herramientas/revisar-texto.py --texto "El pie entero acá"
    python Áreas/Contenido/herramientas/revisar-texto.py pie.txt --limpiar   # deja pie.limpio.txt
    python Áreas/Contenido/herramientas/revisar-texto.py Publicar.md   # revisa cada bloque de la sección "## Pie"

Muestra lo que el feed deja ver antes del "más" (los primeros 125 caracteres) y marca:

- FALLA: guion largo (—), caracteres invisibles, más de 5 hashtags, faltan los de marca,
  un link en el pie, y todo lo de "prohibido" en Empresa/Marca/marca.json
- AVISO: frases de IA de Empresa/Marca/Tono de voz.md, preguntas retóricas en cadena, más de dos
  emojis, cierres que ordenan en vez de explicar

--limpiar saca los invisibles y cambia el guion largo por coma. El resto se corrige a mano: es
criterio, no reemplazo. Adaptado de ig-human y ig-caption de instagram-agent-skill (MIT).
"""
import argparse
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import marca as M  # noqa: E402

VISIBLE = 125
# Los hashtags fijos y lo que no se dice salen de la ficha de la marca
MARCA = [h for h in M.dato("hashtags_marca", []) if not M.es_placeholder(h)]
PROHIBIDO = [(x.get("patron"), x.get("motivo", "")) for x in M.dato("prohibido", []) or []
             if isinstance(x, dict) and x.get("patron") and "ejemplo de frase" not in x.get("patron")]

INVISIBLES = re.compile("[​‌‍⁠﻿­᠎؜‎‏⁣"
                        "\U000e0000-\U000e007f]")
ESPACIOS_RAROS = re.compile("[      ]")

# De Empresa/Marca/Tono de voz.md, sección "Que no suene a IA"
FRASES_IA = [
    r"en un mundo donde", r"imagin[aá]te un mundo", r"\bdescubr[ií]\b", r"\bsumergite\b",
    r"\bdesbloque[aá]\b", r"no esperes más", r"vos pod[eé]s", r"¿y vos,? qu[eé] esper[aá]s",
    r"en este (?:posteo|post|video|reel) te (?:cuento|muestro)", r"ac[aá] te explico",
    r"cabe destacar", r"es importante mencionar", r"no obstante", r"en definitiva", r"dicho esto",
    r"\bsumamente\b", r"\babsolutamente\b", r"totalmente únic", r"\bincreíblemente\b",
    r"con el fin de", r"debido al hecho de que", r"tiene la capacidad de",
    r"integral, profesional", r"de excelencia", r"dej[aá] de scrollear", r"segu[ií]nos para más",
] + list(M.dato("frases_ia_extra", []) or [])
ORDENES = [r"^guard[aá] (?:este|el) post", r"^revis[aá] esto", r"^compart[ií] (?:esto|con)"]


def revisar(texto):
    fallas, avisos = [], []
    if "—" in texto:
        fallas.append("Guion largo (—) %d vez/veces. Coma, punto, dos puntos o paréntesis" % texto.count("—"))
    n_inv = len(INVISIBLES.findall(texto))
    if n_inv:
        fallas.append("%d caracter(es) invisible(s), típicos de texto generado. Usar --limpiar" % n_inv)
    if ESPACIOS_RAROS.search(texto):
        avisos.append("Espacios no comunes (no separables, finos). --limpiar los normaliza")
    tags = re.findall(r"#\w+", texto)
    if len(tags) > 5:
        fallas.append("%d hashtags. Instagram admite hasta 5" % len(tags))
    if not MARCA:
        avisos.append("Los hashtags de marca de Empresa/Marca/marca.json son de ejemplo: completarlos")
    faltan = [m for m in MARCA if m.lower() not in [t.lower() for t in tags]]
    if faltan:
        fallas.append("Faltan hashtags de marca: %s" % " ".join(faltan))
    if re.search(r"https?://|www\.|\b\w+\.(?:com|net|org|uy|ar|es|mx|cl|co|pe)\b", texto):
        fallas.append("Hay un link. En el pie no se puede tocar: va en la bio o por WhatsApp")
    for patron, motivo in PROHIBIDO:
        m = re.search(patron, texto, re.I)
        if m:
            fallas.append('"%s": %s' % (m.group(0), motivo or "está en lo prohibido de marca.json"))
    bajo = texto.lower()
    for f in FRASES_IA:
        m = re.search(f, bajo)
        if m:
            avisos.append('Suena a IA: "%s" → Empresa/Marca/Tono de voz.md' % m.group(0))
    for linea in texto.splitlines():
        if any(re.search(o, linea.strip().lower()) for o in ORDENES):
            avisos.append('Cierre que ordena ("%s"). Explicar por qué importa' % linea.strip()[:40])
    if re.search(r"\?[^?.!\n]{0,80}\?[^?.!\n]{0,80}\?", texto):
        avisos.append("Tres preguntas seguidas. Una sola, y concreta")
    emojis = [c for c in texto if unicodedata.category(c) == "So"]
    if len(emojis) > 2:
        avisos.append("%d emojis. Máximo uno o dos por pieza" % len(emojis))
    primera = texto.strip().split("\n")[0]
    if re.match(r"^\s*(#|hola|buen[oa]s)", primera, re.I):
        fallas.append("La primera línea arranca con un saludo o un hashtag")
    return fallas, avisos


def limpiar(texto):
    texto = INVISIBLES.sub("", texto)
    texto = ESPACIOS_RAROS.sub(" ", texto)
    texto = re.sub(r"\s*—\s*", ", ", texto)
    return re.sub(r",\s*([.,:;])", r"\1", texto)


def main():
    p = argparse.ArgumentParser(description="Revisa un texto contra las reglas de la marca")
    p.add_argument("archivo", nargs="?")
    p.add_argument("--texto")
    p.add_argument("--limpiar", action="store_true")
    a = p.parse_args()
    if a.texto:
        texto = a.texto
    elif a.archivo:
        texto = open(a.archivo, encoding="utf-8").read()
    else:
        texto = sys.stdin.read()
    if a.archivo and a.archivo.lower().endswith(".md") and not a.texto:
        seccion = re.search(r"^## Pie\b.*?(?=^## |\Z)", texto, re.S | re.M)
        bloques = re.findall(r"^```[^\n]*\n(.*?)^```", seccion.group(0), re.S | re.M) if seccion else []
        if not bloques:
            print("No encontré un bloque ``` en la sección \"## Pie\" de %s" % a.archivo)
            sys.exit(1)
        hubo_fallas = False
        for i, b in enumerate(bloques, 1):
            print("=== Pie %d de %d ===" % (i, len(bloques)))
            hubo_fallas |= mostrar(b)
            print()
        sys.exit(1 if hubo_fallas else 0)
    if a.limpiar:
        texto = limpiar(texto)
        if a.archivo:
            destino = re.sub(r"(\.\w+)?$", r".limpio\1", a.archivo, count=1)
            open(destino, "w", encoding="utf-8").write(texto)
            print("Limpio → %s\n" % destino)

    sys.exit(1 if mostrar(texto) else 0)


def mostrar(texto):
    """Imprime el informe de un pie. Devuelve True si hay fallas."""
    plano = re.sub(r"\s+", " ", texto.strip())
    print("LO QUE SE VE ANTES DEL \"MÁS\" (%d de %d caracteres)" % (min(len(plano), VISIBLE), VISIBLE))
    print("  " + plano[:VISIBLE] + ("…" if len(plano) > VISIBLE else ""))
    print()
    fallas, avisos = revisar(texto)
    for f in fallas:
        print("FALLA  " + f)
    for w in avisos:
        print("AVISO  " + w)
    print("\n" + ("LISTO para publicar" if not fallas and not avisos else
                  "%d falla(s), %d aviso(s). Las fallas se corrigen; cada aviso se decide" % (len(fallas), len(avisos))))
    return bool(fallas)


if __name__ == "__main__":
    main()
