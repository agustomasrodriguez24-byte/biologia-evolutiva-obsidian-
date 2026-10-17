# /// script
# requires-python = ">=3.9"
# ///
"""Extrae los posts compartidos en un chat de la exportación de Instagram (formato JSON).

Uso:
  uv run --python 3.13 extraer.py <zip-o-carpeta> --chat <texto> [--desde AAAA-MM-DD] [--salida archivo.md] [--listar]

- <zip-o-carpeta>: el ZIP que descarga Meta o la carpeta ya descomprimida.
- --chat: parte del nombre de la carpeta del chat o de un participante (ej. "nutricionancestral").
- --listar: solo muestra los chats que coinciden, sin extraer nada.
- --desde: ignora mensajes anteriores a esa fecha (para importaciones incrementales).

Lee únicamente el chat pedido. No imprime el contenido de otras conversaciones.
"""
import argparse
import datetime as dt
import json
import re
import sys
import zipfile
from pathlib import Path


def arreglar(texto):
    """Meta exporta UTF-8 mal codificado (mojibake). Lo corrige si hace falta."""
    if not isinstance(texto, str):
        return texto
    try:
        return texto.encode("latin-1").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return texto


def archivos_de_mensajes(origen: Path):
    """Devuelve (ruta_carpeta_chat, contenido_json) de cada message_N.json."""
    patron = re.compile(r"messages/(inbox|message_requests)/([^/]+)/message_\d+\.json$")
    if origen.is_file() and origen.suffix.lower() == ".zip":
        with zipfile.ZipFile(origen) as z:
            for nombre in z.namelist():
                m = patron.search(nombre.replace("\\", "/"))
                if m:
                    yield m.group(2), json.loads(z.read(nombre).decode("utf-8"))
    else:
        for ruta in origen.rglob("message_*.json"):
            m = patron.search(ruta.as_posix())
            if m:
                yield m.group(2), json.loads(ruta.read_text(encoding="utf-8"))


def coincide(carpeta, datos, texto):
    texto = texto.lower()
    if texto in carpeta.lower():
        return True
    return any(texto in arreglar(p.get("name", "")).lower() for p in datos.get("participants", []))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("origen")
    ap.add_argument("--chat", required=True)
    ap.add_argument("--desde")
    ap.add_argument("--salida")
    ap.add_argument("--listar", action="store_true")
    a = ap.parse_args()

    origen = Path(a.origen)
    if not origen.exists():
        sys.exit(f"No existe: {origen}")
    desde = dt.datetime.fromisoformat(a.desde) if a.desde else None

    chats = {}
    for carpeta, datos in archivos_de_mensajes(origen):
        if coincide(carpeta, datos, a.chat):
            chats.setdefault(carpeta, {"participantes": set(), "mensajes": []})
            chats[carpeta]["participantes"].update(arreglar(p.get("name", "")) for p in datos.get("participants", []))
            chats[carpeta]["mensajes"].extend(datos.get("messages", []))

    if not chats:
        sys.exit(f"Ningún chat coincide con '{a.chat}'.")
    if a.listar:
        for carpeta, c in chats.items():
            print(f"{carpeta}: {', '.join(sorted(c['participantes']))} ({len(c['mensajes'])} mensajes)")
        return

    filas = []
    for carpeta, c in chats.items():
        for m in c["mensajes"]:
            fecha = dt.datetime.fromtimestamp(m.get("timestamp_ms", 0) / 1000)
            if desde and fecha < desde:
                continue
            share = m.get("share") or {}
            link = share.get("link", "")
            texto = arreglar(share.get("share_text", "")) or ""
            autor = arreglar(share.get("original_content_owner", "")) or ""
            nota = arreglar(m.get("content", "")) or ""
            if not (link or texto or nota):
                continue
            filas.append((fecha, carpeta, autor, link, texto, nota))

    filas.sort(key=lambda f: f[0])
    lineas = [f"# Posts compartidos ({len(filas)})", ""]
    for fecha, carpeta, autor, link, texto, nota in filas:
        lineas.append(f"## {fecha:%Y-%m-%d %H:%M} · @{autor or 'sin autor'}")
        if link:
            lineas.append(f"- Link: {link}")
        if nota and nota != texto:
            lineas.append(f"- Nota de Agus: {nota}")
        if texto:
            lineas.append("- Texto del post:")
            lineas.extend(f"  > {l}" if l.strip() else "  >" for l in texto.splitlines())
        lineas.append("")

    salida = "\n".join(lineas)
    if a.salida:
        Path(a.salida).write_text(salida, encoding="utf-8")
        print(f"OK: {len(filas)} posts → {a.salida}")
    else:
        print(salida)


if __name__ == "__main__":
    main()
