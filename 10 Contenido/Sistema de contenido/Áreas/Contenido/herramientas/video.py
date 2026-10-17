#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Edita los videos verticales de la marca: short simple (frases, info, inspiración) e instructor a cámara.

La cuenta, las paletas, el logo y el vocabulario salen de Empresa/Marca/marca.json (vía marca.py).

    python Áreas/Contenido/herramientas/video.py preparar <proyecto> [--transcribir]
    python Áreas/Contenido/herramientas/video.py armar    <proyecto>
    python Áreas/Contenido/herramientas/video.py revisar  <proyecto>
    python Áreas/Contenido/herramientas/video.py portada  <proyecto>

<proyecto> es una carpeta de Áreas/Contenido/outputs/aaaa-mm/videos/NN-tema/ (NN = el número de la
pieza en el plan del mes). Los clips del celular van en Áreas/Contenido/Material/Piezas/aaaa-mm/NN-tema/
(o en brutos/ dentro del proyecto). El script hace el trabajo mecánico y Claude decide: qué tomas van, dónde se corta,
qué dice la placa. La decisión queda escrita en <proyecto>/edl.json, que es lo que se corrige.

preparar  Mira cada clip: duración, resolución, una hoja de contacto (un cuadro cada tanto, con
          el segundo arriba) en trabajo/hojas/. Con --transcribir, además, la transcripción con
          el tiempo de cada palabra (faster-whisper, en español) en trabajo/transcripcion.json y
          una versión para leer en trabajo/transcripcion.txt.
armar     (con --vista-previa 15: solo los primeros 15 segundos, para aprobar la dirección)
          Lee edl.json y arma el video final 1080 x 1920: corta, encuadra, pega, suma la placa
          del gancho, los subtítulos (instructor), la música y la placa de cierre, y normaliza el
          volumen. Deja video-N.mp4 en la carpeta del proyecto, sin pisar las versiones anteriores
          (el edl de cada versión queda en trabajo/versiones/). Si el edl tiene "portada" con
          "al_inicio", el video arranca con la portada esos segundos.
revisar   Saca un cuadro de cada corte y de cada placa con las zonas seguras de Instagram
          marcadas, en trabajo/revision.jpg, y mide el volumen. Es lo que se mira antes de
          darlo por bueno.
portada   Arma portada.png (1080 x 1920) con el estilo de los carruseles: un cuadro del video a
          media pantalla, el título enorme abajo y la firma. Lo importante queda en el centro
          3:4, que es lo que muestra la grilla del perfil. Se sube como portada del reel
          (Editar portada → Agregar desde la galería). Lee "portada" del edl.json.

Necesita ffmpeg en el PATH. Para --transcribir: pip install faster-whisper. Para las placas:
pip install playwright (usa el Chrome instalado) — las mismas que el carrusel.
"""
import argparse
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent.parent
FUENTES = AQUI / "fuentes"

W, H, FPS = 1080, 1920, 30
# Zonas seguras de Reels (px sobre 1080 x 1920): arriba la barra de la app, abajo el pie,
# los botones y el nombre de la cuenta, a la derecha los íconos de like y compartir.
SEGURA = {"arriba": 220, "abajo": 1470, "izquierda": 60, "derecha": 120}

EXTENSIONES = {".mp4", ".mov", ".m4v", ".mkv", ".avi", ".webm"}
AUDIOS = {".wav", ".m4a", ".mp3", ".aac", ".flac", ".ogg", ".opus"}

# Lo que Whisper escucha mal en este rubro. Se corrige en la transcripción, antes de subtitular.
sys.path.insert(0, str(AQUI))
import marca as M  # noqa: E402

CUENTA = M.dato("cuenta", "@tucuenta")
DESCRIPTOR = M.dato("descriptor", "")
VOCABULARIO = M.dato("vocabulario_transcripcion", "") or ""
if "separados por coma" in VOCABULARIO:  # el texto de ejemplo de la ficha
    VOCABULARIO = ""
CORRECCIONES = {k: v for k, v in (M.dato("correcciones_transcripcion", {}) or {}).items()
                if "tu marca" not in k}


# ───────────────────────── utilidades ─────────────────────────

def ff(*args, cwd=None):
    """Corre ffmpeg y corta con el error legible si falla."""
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *map(str, args)]
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if r.returncode:
        sys.exit("ffmpeg falló:\n  %s\n%s" % (" ".join(map(str, cmd)), r.stderr[-2000:]))
    return r


def sondear(clip):
    # -show_streams y -show_format (y no -show_entries con side_data) anda en ffmpeg viejos y nuevos
    r = subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format",
                        "-of", "json", str(clip)], capture_output=True, text=True)
    if r.returncode:
        sys.exit("No pude leer %s: %s" % (clip, r.stderr))
    d = json.loads(r.stdout)
    video = next((s for s in d["streams"] if s["codec_type"] == "video"), {})
    tiene_audio = any(s["codec_type"] == "audio" for s in d["streams"])
    w, h = video.get("width", 0), video.get("height", 0)
    rot = int((video.get("tags") or {}).get("rotate", 0) or 0)
    for sd in video.get("side_data_list") or []:
        if "rotation" in sd:
            rot = int(sd["rotation"])
    if abs(rot) in (90, 270):
        w, h = h, w
    return {"duracion": float(d["format"]["duration"]), "ancho": w, "alto": h,
            "audio": tiene_audio}


MATERIAL = AQUI.parent / "Material"


def carpeta_de_clips(proyecto):
    """Los clips de una pieza van en Material/Piezas/aaaa-mm/NN-tema/ (el mismo nombre que la
    carpeta del proyecto). Si el proyecto tiene brutos/ propia, se usa esa."""
    propia = proyecto / "brutos"
    if propia.is_dir():
        return propia
    return MATERIAL / "Piezas" / proyecto.parent.parent.name / proyecto.name


def ruta_clip(proyecto, nombre):
    """Dónde está un clip del edl. Lo normal es nombrarlo desde el material, sin copiarlo:
    "Material/Videos/Calle/Calle pov 01.mov" (relativo a Áreas/Contenido). También vale
    "brutos/x.mov" o un nombre suelto: se busca en el proyecto, en la carpeta de clips de la
    pieza y, si no está, en Material/Videos por el nombre del archivo."""
    nombre = str(nombre).replace("\\", "/")
    if nombre.startswith("Material/"):
        return AQUI.parent / nombre
    candidatos = [proyecto / nombre, carpeta_de_clips(proyecto) / Path(nombre).name]
    for c in candidatos:
        if c.exists():
            return c
    hallados = sorted((MATERIAL / "Videos").rglob(Path(nombre).name)) if (MATERIAL / "Videos").is_dir() else []
    return hallados[0] if hallados else candidatos[0]


def clips(proyecto):
    brutos = carpeta_de_clips(proyecto)
    if not brutos.is_dir():
        sys.exit("No encuentro los clips. Van en %s (el mismo nombre que la pieza)." % brutos)
    lista = sorted(p for p in brutos.iterdir() if p.suffix.lower() in EXTENSIONES)
    if not lista:
        sys.exit("No hay clips en %s." % brutos)
    return lista


def rel(ruta, desde):
    """Ruta relativa con barras /: los filtros de ffmpeg no se llevan con 'C:\\'."""
    return os.path.relpath(ruta, desde).replace("\\", "/")


def hms(s):
    return "%d:%05.2f" % (s // 60, s % 60)


# ───────────────────────── preparar ─────────────────────────

def preparar(proyecto, transcribir, modelo):
    trabajo = proyecto / "trabajo"
    (trabajo / "hojas").mkdir(parents=True, exist_ok=True)
    resumen = []
    fuente = rel(FUENTES / "Poppins-SemiBold.ttf", proyecto)
    for clip in clips(proyecto):
        info = sondear(clip)
        paso = max(1, math.ceil(info["duracion"] / 48))  # hasta 48 cuadros por hoja
        cuadros = max(1, math.ceil(info["duracion"] / paso))
        filas = math.ceil(cuadros / 8)
        hoja = trabajo / "hojas" / (clip.stem + ".jpg")
        ff("-i", rel(clip, proyecto), "-vf",
           "fps=1/%d,scale=200:-2,drawtext=fontfile='%s':text='%%{eif\\:n*%d\\:d}s':"
           "x=6:y=6:fontsize=22:fontcolor=white:box=1:boxcolor=black@0.6:boxborderw=4,"
           "tile=8x%d:padding=4:color=white" % (paso, fuente, paso, filas),
           "-frames:v", "1", "-q:v", "3", rel(hoja, proyecto), cwd=proyecto)
        resumen.append({"clip": rel(clip, proyecto), **info, "hoja": rel(hoja, proyecto),
                        "segundos_por_cuadro": paso})
        print("%-28s %6.1f s  %dx%d  %s  → %s" % (clip.name, info["duracion"], info["ancho"],
              info["alto"], "con audio" if info["audio"] else "sin audio", rel(hoja, proyecto)))
    (trabajo / "clips.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=2),
                                        encoding="utf-8")
    sincronizar(proyecto)
    if transcribir:
        transcribir_clips(proyecto, modelo)


# ───────────────────────── audio grabado aparte ─────────────────────────
# Dos casos, los dos con los archivos de audio en la misma carpeta que los clips:
#  · Grabado AL MISMO TIEMPO que el video (un grabador o un celular aparte con el micrófono):
#    preparar lo sincroniza solo, comparando con el sonido del propio clip, y el video usa ese
#    audio. Queda en trabajo/sincro.json; si algo quedó mal, se corrige ahí el "desfase".
#  · VOZ EN OFF grabada después: no se sincroniza con nada. Va en el edl como "voz" y suena encima
#    de todo el video; los subtítulos salen de ese archivo.

def envolvente(archivo, desde=0.0, largo=None):
    """El volumen del sonido, 100 veces por segundo: lo que se compara para sincronizar."""
    import numpy as np
    cmd = ["ffmpeg", "-v", "error", "-ss", "%.3f" % desde]
    if largo:
        cmd += ["-t", "%.3f" % largo]
    cmd += ["-i", str(archivo), "-vn", "-ac", "1", "-ar", "8000", "-f", "s16le", "-"]
    datos = subprocess.run(cmd, capture_output=True).stdout
    x = np.abs(np.frombuffer(datos, dtype=np.int16).astype(np.float32))
    n = len(x) // 80
    if n < 10:
        return None
    e = x[:n * 80].reshape(n, 80).mean(axis=1)
    e = np.log1p(e)
    return (e - e.mean()) / (e.std() + 1e-6)


def desfase(clip_env, audio_env):
    """Dónde empieza el clip dentro del audio (segundos) y qué tan seguro es (0 a 1)."""
    import numpy as np
    n = len(clip_env) + len(audio_env)
    tam = 1 << (n - 1).bit_length()
    c = np.fft.irfft(np.fft.rfft(audio_env, tam) * np.conj(np.fft.rfft(clip_env, tam)), tam)
    c = np.concatenate([c[-(len(clip_env) - 1):], c[:len(audio_env)]])
    i = int(np.argmax(c))
    return (i - (len(clip_env) - 1)) / 100.0, float(c[i] / len(clip_env))


def sincronizar(proyecto):
    carpeta = carpeta_de_clips(proyecto)
    audios = sorted(p for p in carpeta.iterdir() if p.suffix.lower() in AUDIOS) if carpeta.is_dir() else []
    if not audios:
        return {}
    try:
        import numpy  # noqa: F401
    except ImportError:
        sys.exit("Para sincronizar el audio grabado aparte falta numpy:  pip install numpy")
    print("Audio grabado aparte: %s" % ", ".join(a.name for a in audios))
    trabajo = proyecto / "trabajo"
    (trabajo / "sincro").mkdir(parents=True, exist_ok=True)
    ruta = trabajo / "sincro.json"
    previo = json.loads(ruta.read_text(encoding="utf-8")) if ruta.exists() else {}
    envs = {a: envolvente(a) for a in audios}
    resultado, usados = {}, set()
    for clip in clips(proyecto):
        clave = rel(clip, proyecto)
        info = sondear(clip)
        if clave in previo and previo[clave].get("a_mano"):
            r = previo[clave]
        else:
            if not info["audio"]:
                print("  %-26s sin sonido propio: no se puede sincronizar solo. Si va con un audio,"
                      " anotarlo a mano en trabajo/sincro.json" % clip.name)
                continue
            e = envolvente(clip)
            if e is None:
                continue
            mejor = max(((a,) + desfase(e, envs[a]) for a in audios if envs[a] is not None),
                        key=lambda t: t[2])
            r = {"audio": rel(mejor[0], proyecto), "desfase": round(mejor[1], 2),
                 "confianza": round(mejor[2], 2)}
        audio = proyecto / r["audio"]
        usados.add(audio.resolve())
        salida = trabajo / "sincro" / (clip.stem + ".wav")
        d = r["desfase"]
        filtro = ["-af", "adelay=%d|%d,apad" % (int(-d * 1000), int(-d * 1000))] if d < 0 else ["-af", "apad"]
        ff("-ss", "%.3f" % max(0, d), "-i", audio, *filtro, "-t", "%.3f" % info["duracion"],
           "-ac", "2", "-ar", "48000", salida)
        r["archivo"] = rel(salida, proyecto)
        resultado[clave] = r
        aviso = "" if r.get("a_mano") or r["confianza"] >= 0.35 else "  ← poca confianza: mirarlo"
        print("  %-26s → %s, desde el segundo %.2f (confianza %.2f)%s" % (
            clip.name, audio.name, d, r.get("confianza", 1), aviso))
    sueltos = [a for a in audios if a.resolve() not in usados]
    for a in sueltos:
        print("  %s no coincide con ningún clip: queda como voz en off (\"voz\" en el edl)" % a.name)
    ruta.write_text(json.dumps(resultado, ensure_ascii=False, indent=2), encoding="utf-8")
    return resultado


def sincro(proyecto):
    ruta = proyecto / "trabajo" / "sincro.json"
    return json.loads(ruta.read_text(encoding="utf-8")) if ruta.exists() else {}


def corregir(texto):
    for patron, bien in CORRECCIONES.items():
        texto = re.sub(patron, bien, texto, flags=re.IGNORECASE)
    return texto


def audio_16k(archivo):
    """El audio en mono a 16 kHz, decodificado con ffmpeg. Así faster-whisper no usa PyAV, que en
    algunas versiones (Windows, Python 3.13) rompe con "metadata_errors"."""
    import numpy as np
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", str(archivo), "-f", "s16le", "-ac", "1",
                        "-ar", "16000", "-"], capture_output=True)
    if r.returncode:
        sys.exit("ffmpeg no pudo leer el audio de %s" % archivo)
    return np.frombuffer(r.stdout, np.int16).astype(np.float32) / 32768.0


def transcribir_clips(proyecto, modelo):
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        sys.exit("Falta faster-whisper:  pip install faster-whisper")
    print("Transcribiendo con el modelo '%s' (la primera vez lo descarga)…" % modelo)
    whisper = WhisperModel(modelo, device="auto", compute_type="auto")
    todo, lineas = {}, []
    sin = sincro(proyecto)
    fuentes = []
    for clip in clips(proyecto):
        clave = rel(clip, proyecto)
        if clave in sin:
            fuentes.append((clave, proyecto / sin[clave]["archivo"], clip.name))
        elif sondear(clip)["audio"]:
            fuentes.append((clave, clip, clip.name))
    carpeta = carpeta_de_clips(proyecto)
    usados = {(proyecto / r["audio"]).resolve() for r in sin.values()}
    for a in sorted(carpeta.iterdir()) if carpeta.is_dir() else []:
        if a.suffix.lower() in AUDIOS and a.resolve() not in usados:
            fuentes.append(("voz/" + a.name, a, a.name + " (voz en off)"))
    for clave, archivo, nombre in fuentes:
        segmentos, _ = whisper.transcribe(audio_16k(archivo), language="es", word_timestamps=True,
                                          vad_filter=True, initial_prompt=VOCABULARIO or None)
        palabras, frases = [], []
        for seg in segmentos:
            frases.append({"desde": round(seg.start, 2), "hasta": round(seg.end, 2),
                           "texto": corregir(seg.text.strip())})
            for w in seg.words or []:
                palabras.append({"p": corregir(w.word.strip()), "desde": round(w.start, 2),
                                 "hasta": round(w.end, 2)})
        todo[clave] = {"frases": frases, "palabras": palabras}
        lineas.append("## %s" % clave)
        lineas += ["[%s → %s] %s" % (hms(f["desde"]), hms(f["hasta"]), f["texto"]) for f in frases]
        lineas.append("")
        print("  %s: %d frases" % (nombre, len(frases)))
    trabajo = proyecto / "trabajo"
    (trabajo / "transcripcion.json").write_text(json.dumps(todo, ensure_ascii=False, indent=1),
                                               encoding="utf-8")
    (trabajo / "transcripcion.txt").write_text("\n".join(lineas), encoding="utf-8")
    print("→ trabajo/transcripcion.txt")


# ───────────────────────── placas (HTML → PNG transparente) ─────────────────────────

# Las mismas cuatro paletas que los carruseles (.claude/skills/carrusel/base.css). Se elige con
# "paleta" en el edl.json: el nombre de una paleta de marca.json (si falta, la de por defecto).
PALETAS = M.paletas_video()
PALETA_DEFECTO = M.paleta_por_defecto()
LOGOS = M.LOGOS


def paleta(edl):
    return PALETAS.get((edl or {}).get("paleta", PALETA_DEFECTO), PALETAS[PALETA_DEFECTO])


def css_capas(p, k, fuentes):
    """El estilo de las capas del video, igual que los carruseles: Switzer apretada, un color por
    capa, sin bordes. k = escala (1 para 1080 px, 0.5 para las placas estáticas a 540).
    fuentes = carpeta (URL) donde están los .woff2."""
    def px(n):
        return "%dpx" % round(n * k)
    return """
@font-face { font-family: Switzer; src: url(%(f)s/switzer-latin-800-normal.woff2); font-weight: 800; }
@font-face { font-family: Switzer; src: url(%(f)s/switzer-latin-900-normal.woff2); font-weight: 900; }
@font-face { font-family: Switzer; src: url(%(f)s/switzer-latin-600-normal.woff2); font-weight: 600; }
@font-face { font-family: Poppins; src: url(%(f)s/poppins-latin-600-normal.woff2); font-weight: 600; }
.gancho { position: absolute; left: %(izq)s; right: %(der)s; top: %(arr)s; background: %(base)s; color: %(tinta)s;
  border-radius: %(r)s; padding: %(p1)s %(p2)s; font-family: Switzer, sans-serif; }
.gancho h1 { margin: 0; font-size: %(h1)s; line-height: 1.02; font-weight: 800; letter-spacing: -0.03em; }
.gancho h1 span { display: inline-block; }
.gancho .resalta, .cierre .resalta { color: %(acento)s; }
.gancho p { margin: %(m)s 0 0; font-size: %(rem)s; font-weight: 800; letter-spacing: -0.01em; color: %(acento)s; }
.grafico { position: absolute; left: %(izq)s; right: %(der)s; top: %(gtop)s; background: %(golpe)s; color: %(golpe_tinta)s;
  border-radius: %(r)s; padding: %(p1)s %(p2)s; font-family: Switzer, sans-serif; }
.grafico .dato, .grafico h2 { margin: 0; font-size: %(dato)s; font-weight: 900; line-height: .95; letter-spacing: -0.04em; }
.grafico p { margin: %(m)s 0 0; font-size: %(rem)s; font-weight: 600; line-height: 1.2; }
.cierre { position: absolute; inset: 0; background: %(base)s; color: %(tinta)s; display: flex; flex-direction: column;
  justify-content: center; gap: %(gap)s; padding: 0 %(lado)s; font-family: Switzer, sans-serif; }
.cierre img { width: %(logow)s; }
.cierre h2 { margin: 0; font-size: %(h2)s; line-height: 1.02; font-weight: 800; letter-spacing: -0.03em; }
.cierre .wa { align-self: flex-start; background: %(acento)s; color: %(base)s; border-radius: 999px;
  padding: %(b1)s %(b2)s; font-family: Poppins, sans-serif; font-size: %(bt)s; font-weight: 600; }
.cierre .cuenta { font-size: %(rem)s; font-weight: 600; opacity: .8; }
""" % dict(f=fuentes, izq=px(SEGURA["izquierda"]), der=px(SEGURA["derecha"]), arr=px(SEGURA["arriba"] + 40),
           r=px(28), p1=px(36), p2=px(44), h1=px(84), m=px(14), rem=px(40), gtop=px(760), dato=px(124),
           gap=px(48), lado=px(88), logow=px(420), h2=px(84), b1=px(24), b2=px(48), bt=px(42), **p)


def con_resalta(texto, resalta):
    t = esc(texto)
    if resalta:
        r = esc(resalta)
        t = t.replace(r, "<span class='resalta'>%s</span>" % r, 1)
    return t


def html_placa(cuerpo, p=None):
    css = css_capas(p or PALETAS[PALETA_DEFECTO], 0.5, FUENTES.as_uri())
    return ("<!doctype html><html lang='es'><head><meta charset='utf-8'><style>"
            "html, body { margin: 0; background: transparent; } .lienzo { position: relative; width: 540px; height: 960px; }"
            "%s</style></head><body><div class='lienzo'>%s</div></body></html>" % (css, cuerpo))


def esc(t):
    return (t or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def renderizar_placas(placas):
    """placas: lista de (html, png). PNG 1080x1920 con fondo transparente."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit("Falta Playwright para las placas:  pip install playwright")
    with sync_playwright() as p:
        nav = None
        for canal in ("chrome", "msedge", None):
            try:
                nav = p.chromium.launch(channel=canal) if canal else p.chromium.launch()
                break
            except Exception:
                continue
        if nav is None:
            sys.exit("Playwright no encontró Chrome ni Edge.")
        pag = nav.new_page(viewport={"width": 540, "height": 960}, device_scale_factor=2)
        with tempfile.TemporaryDirectory() as tmp:
            for i, (html, png) in enumerate(placas):
                f = Path(tmp) / ("p%d.html" % i)
                f.write_text(html, encoding="utf-8")
                pag.goto(f.as_uri())
                pag.wait_for_load_state("networkidle")
                pag.evaluate("document.fonts.ready")
                pag.screenshot(path=str(png), omit_background=True)
        nav.close()


# ───────────────────────── subtítulos (ASS) ─────────────────────────

def ass_tiempo(s):
    s = max(0, s)
    return "%d:%02d:%05.2f" % (s // 3600, (s % 3600) // 60, s % 60)


def ass_color(hexa):
    """#RRGGBB → &H00BBGGRR (los colores de ASS van al revés)."""
    h = hexa.lstrip("#")
    return "&H00%s%s%s" % (h[4:6], h[2:4], h[0:2])


# Cómo se ven los subtítulos en cada estilo de animación (colores ASS: &HAABBGGRR, AA=transparencia)
SUBS = {
    "caja":    dict(tam=88, letra="&H00FFFFFF", borde=None, fondo="&H64000000", tipo=1, grosor=7, sombra=0),
    "fuerte":  dict(tam=96, letra="&H00FFFFFF", borde="&H000A0A0A", fondo="&H59000000", tipo=1, grosor=11, sombra=4,
                    mayusculas=True),
    "sticker": dict(tam=78, letra="&H00111111", borde="&H00FFFFFF", fondo="&H00FFFFFF", tipo=3, grosor=16, sombra=0),
    "cine":    dict(tam=70, letra="&H00FFFFFF", borde="&H00000000", fondo="&H80000000", tipo=1, grosor=0, sombra=5),
}
SUBS["cine-sticker"] = SUBS["cine"]


def subtitulos(edl, proyecto, destino):
    pal = paleta(edl)
    oscura = pal["tinta"] == "#ffffff"
    borde = pal["base"] if oscura else pal["golpe"]
    resalto = pal["acento"] if oscura else pal["base"]
    """Arma el .ass con las palabras de los segmentos, en tandas de hasta 3, y la palabra que se
    está diciendo en verde. Los tiempos se corren a la línea de tiempo del video armado."""
    trans = json.loads((proyecto / "trabajo" / "transcripcion.json").read_text(encoding="utf-8"))
    palabras, t0 = [], 0.0
    vo = edl.get("voz")
    if vo and vo.get("archivo"):
        for w in trans.get("voz/" + Path(vo["archivo"]).name, {}).get("palabras", []):
            t = w["desde"] - vo.get("recorte", 0) + vo.get("desde", 0)
            if t >= 0:
                palabras.append({"p": w["p"], "desde": t, "hasta": w["hasta"] - vo.get("recorte", 0) + vo.get("desde", 0)})
    for seg in ([] if palabras else edl["segmentos"]):
        desde, hasta = seg["desde"], seg["hasta"]
        for w in trans.get(seg["clip"], {}).get("palabras", []):
            if w["desde"] >= desde - 0.05 and w["hasta"] <= hasta + 0.05:
                palabras.append({"p": w["p"], "desde": t0 + w["desde"] - desde,
                                 "hasta": t0 + w["hasta"] - desde})
        t0 += hasta - desde
    reemplazos = edl.get("correcciones", {})
    for w in palabras:
        w["p"] = reemplazos.get(w["p"], w["p"]).replace("—", ",")

    # De a una palabra, en el centro (como los reels de referencia). "palabras_por_vez": 3 vuelve a tandas abajo
    por_vez = int(edl.get("palabras_por_vez", 1))
    tandas, actual = [], []
    for w in palabras:
        actual.append(w)
        if len(actual) == por_vez or re.search(r"[.?!,]$", w["p"]):
            tandas.append(actual)
            actual = []
    if actual:
        tandas.append(actual)

    estilo = edl.get("estilo_animacion", "cine-sticker")
    sub = dict(SUBS.get(estilo, SUBS["cine"]))
    if int(edl.get("palabras_por_vez", 1)) == 1:
        sub["tam"] = int(sub["tam"] * 1.3)  # una palabra sola va más grande
    if estilo == "sticker":
        resalto = pal["base"] if oscura else pal["golpe"]
    if sub.get("mayusculas"):
        for w in palabras:
            w["p"] = w["p"].upper()
    y = int(SEGURA["abajo"] - 170) if por_vez > 1 else 1140  # una sola palabra: más al centro, abajo de la cara
    cab = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: %d" % W, "PlayResY: %d" % H, "",
           "[V4+ Styles]",
           "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, "
           "BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, "
           "BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
           # Según el estilo de animación (la letra es siempre Switzer):
           #  caja: blanca con borde del color de base · fuerte: mayúsculas con borde negro grueso
           #  sticker: negra sobre recuadro blanco · cine: más chica, sin borde, con sombra suave
           "Style: Sub,Switzer Extrabold,%d,%s,&H00FFFFFF,%s,%s,0,0,0,0,100,100,"
           "0,0,%d,%d,%d,8,%d,%d,0,1" % (sub["tam"], sub["letra"], sub["borde"] or ass_color(borde), sub["fondo"],
                                          sub["tipo"], sub["grosor"], sub["sombra"],
                                          SEGURA["izquierda"], SEGURA["derecha"]),
           # Lo destacado: la palabra sobre un rectángulo recto del color de acento
           "Style: Dest,Switzer Extrabold,%d,%s,&H00FFFFFF,%s,&H00000000,0,0,0,0,100,100,"
           "0,0,3,14,0,8,%d,%d,0,1" % (sub["tam"], ass_color(pal["base"] if oscura else pal["tinta"]),
                                        ass_color(pal["acento"] if oscura else pal["golpe"]),
                                        SEGURA["izquierda"], SEGURA["derecha"]),
           "", "[Events]",
           "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
    verde = ass_color(resalto) + "&"  # la palabra que se está diciendo, en el acento de la paleta
    # "destacar": palabras o frases que salen solas, abajo y en etiqueta (como "Plixi" o "todos los meses")
    limpia = lambda t: re.sub(r"[^\wáéíóúñü]", "", t.lower())
    for w in palabras:
        w["dest"] = False
    for f in edl.get("destacar", []):  # la frase entera y seguida, no cada palabra suelta
        frase = [limpia(x) for x in f.split()]
        for i in range(len(palabras) - len(frase) + 1):
            if [limpia(palabras[i + j]["p"]) for j in range(len(frase))] == frase:
                for j in range(len(frase)):
                    palabras[i + j]["dest"] = True
    fondo_dest = ass_color(pal["acento"] if oscura else pal["golpe"])
    letra_dest = ass_color(pal["base"] if oscura else pal["tinta"])
    borde_sub = sub["borde"] or ass_color(borde)
    eventos = []
    for k, tanda in enumerate(tandas):
        siguiente = tandas[k + 1][0]["desde"] if k + 1 < len(tandas) else None
        for i, w in enumerate(tanda):
            fin = tanda[i + 1]["desde"] if i + 1 < len(tanda) else w["hasta"] + 0.15
            if siguiente is not None:
                fin = min(fin, siguiente)  # que no se pise con la tanda siguiente
                if por_vez == 1 and siguiente - w["hasta"] < 0.35:
                    fin = siguiente  # sin parpadeo entre palabras seguidas
            if por_vez == 1 and w["dest"]:
                eventos.append("Dialogue: 0,%s,%s,Dest,,0,0,0,,{\\pos(%d,%d)}%s" % (
                    ass_tiempo(w["desde"]), ass_tiempo(fin), W // 2, y, w["p"].rstrip(".,;:!?")))
                continue
            partes = []
            for x in tanda:
                if x["dest"]:
                    # lo destacado: en la misma línea y sin moverse, sobre un fondo del color de acento
                    palabra = x["p"].rstrip(".,;:!?")
                    partes.append("{\\bord18\\3c%s&\\c%s&}%s{\\bord%d\\3c%s&\\c%s&}%s" % (
                        fondo_dest, letra_dest, palabra, sub["grosor"], borde_sub, sub["letra"], x["p"][len(palabra):]))
                elif x is w and por_vez > 1:
                    partes.append("{\\c%s}%s{\\c%s}" % (verde, x["p"], sub["letra"] + "&"))
                else:
                    partes.append(x["p"])
            eventos.append("Dialogue: 0,%s,%s,Sub,,0,0,0,,{\\pos(%d,%d)}%s" % (
                ass_tiempo(w["desde"]), ass_tiempo(fin), W // 2, y, " ".join(partes)))
    destino.write_text("\n".join(cab + eventos) + "\n", encoding="utf-8")
    return len(palabras)


# ───────────────────────── armar ─────────────────────────

def encuadre(zoom=1.0, x=0.5, y=0.5):
    """Llena 1080x1920 sin bandas: escala para cubrir, zoom opcional y recorte centrado en x,y."""
    zw, zh = int(W * zoom), int(H * zoom)
    return ("scale=%d:%d:force_original_aspect_ratio=increase,"
            "crop=%d:%d:(iw-%d)*%.3f:(ih-%d)*%.3f,setsar=1,fps=%d,format=yuv420p"
            % (zw, zh, W, H, W, x, H, y, FPS))


TIPOS = ("instructor", "frases", "info", "inspiracion")


def tipo_de(edl):
    """Los cuatro tipos de video (Estilo de video.md, *Los cuatro tipos*):
    instructor  alguien habla a cámara: cortes, título, subtítulos, zooms, insertos, capítulos…
    frases      tomas con frases que cambian con corte seco, palabras en color, título y
                animaciones; con voz en off o solo texto
    info        una sola toma con un texto fijo centrado que explica algo
    inspiracion igual que info, en serif y más poético
    Los nombres viejos ("modo": short, "tipo": texto) se leen como frases o info."""
    tipo = edl.get("tipo") or edl.get("modo") or ""
    if tipo in TIPOS:
        return tipo
    t = edl.get("textos") or {}
    return "frases" if t.get("frases") or t.get("formato") == "frases" else "info"


def modo_de(edl):
    return "instructor" if tipo_de(edl) == "instructor" else "short"


# Zooms que cambian el ángulo: con una cámara parece que hubiera varias. Se alternan en cada corte
# (zoom, x, y); y < 0.5 sube el encuadre para que la cara quede arriba.
ANGULOS = [(1.0, 0.5, 0.5), (1.25, 0.5, 0.36), (1.1, 0.5, 0.45), (1.4, 0.5, 0.32)]


def buscar_archivo(proyecto, nombre):
    """Un inserto o recorte: en el proyecto, en los clips de la pieza o en Material/."""
    for base in (proyecto, carpeta_de_clips(proyecto), MATERIAL, MATERIAL / "Fotos", MATERIAL / "Videos"):
        if (base / nombre).exists():
            return base / nombre
    sys.exit("No encuentro %s (lo busqué en el proyecto, en los clips de la pieza y en Material/)." % nombre)


def mascara_redondeada(destino, ancho, alto, radio=40):
    from PIL import Image, ImageDraw
    m = Image.new("L", (ancho, alto), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, ancho - 1, alto - 1), radio, fill=255)
    m.save(destino)


def armar(proyecto, preview=None):
    ruta_edl = proyecto / "edl.json"
    if not ruta_edl.exists():
        sys.exit("Falta %s. Lo escribe Claude a partir de las hojas y la transcripción." % ruta_edl)
    edl = json.loads(ruta_edl.read_text(encoding="utf-8"))
    modo = modo_de(edl)
    trabajo = proyecto / "trabajo"
    tmp = trabajo / "armado"
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir(parents=True)

    # 1 · Cortar y encuadrar cada segmento, todos con el mismo formato y con pista de audio
    partes = []
    for i, seg in enumerate(edl["segmentos"]):
        clip = ruta_clip(proyecto, seg["clip"])
        info = sondear(clip)
        dur = seg["hasta"] - seg["desde"]
        if dur <= 0:
            sys.exit("Segmento %d: 'hasta' tiene que ser mayor que 'desde'." % (i + 1))
        if "zoom" in seg or edl.get("zooms", "auto" if modo == "instructor" else "no") != "auto":
            vf = encuadre(seg.get("zoom", 1.0), seg.get("x", 0.5), seg.get("y", 0.5))
        else:
            z, x0, y0 = ANGULOS[i % len(ANGULOS)]
            vf = encuadre(z, seg.get("x", x0), seg.get("y", y0))
        if seg.get("byn"):  # el momento de golpe, en blanco y negro
            vf += ",hue=s=0"
        salida = tmp / ("s%02d.mp4" % i)
        entrada_audio = []
        sin = sincro(proyecto).get(seg["clip"])
        if sin and edl.get("audio_original", True):
            entrada_audio = ["-ss", "%.3f" % seg["desde"], "-t", "%.3f" % dur, "-i", proyecto / sin["archivo"]]
            mapa = ["-map", "0:v:0", "-map", "1:a:0"]
        elif not info["audio"] or not edl.get("audio_original", modo == "instructor"):
            entrada_audio = ["-f", "lavfi", "-t", "%.3f" % dur, "-i",
                             "anullsrc=channel_layout=stereo:sample_rate=48000"]
            mapa = ["-map", "0:v:0", "-map", "1:a:0"]
        else:
            mapa = ["-map", "0:v:0", "-map", "0:a:0"]
        ff("-ss", "%.3f" % seg["desde"], "-t", "%.3f" % dur, "-i", clip, *entrada_audio,
           "-vf", vf, *mapa, "-af", "aresample=48000,aformat=channel_layouts=stereo",
           "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-c:a", "aac", "-b:a", "192k",
           "-shortest", salida)
        partes.append(salida)

    # 2 · Placas: gancho arriba y cierre al final
    animado = bool(edl.get("animado", True)) and not preview
    pal = paleta(edl)
    placas = []
    g = edl.get("gancho")
    if animado:
        g_anim, c_anim, graf_anim = g, edl.get("cierre"), edl.get("graficos", [])
        g = None
    if g and g.get("texto"):
        cuerpo = "<div class='gancho'><h1>%s</h1>%s</div>" % (
            con_resalta(g["texto"], g.get("resalta")), "<p>%s</p>" % esc(g["remate"]) if g.get("remate") else "")
        placas.append((html_placa(cuerpo, pal), tmp / "gancho.png"))
    c = None if animado else edl.get("cierre")
    if c:
        logo = (LOGOS / pal["logo"]).as_uri()
        cuerpo = ("<div class='cierre'><img src='%s' alt=''><h2>%s</h2>%s<span class='cuenta'>%s</span></div>" % (
            logo, con_resalta(c.get("texto", ""), c.get("resalta")),
            "<span class='wa'>%s</span>" % esc(c["boton"]) if c.get("boton") else "", esc(CUENTA)))
        placas.append((html_placa(cuerpo, pal), tmp / "cierre.png"))
    graficos = [] if animado else [x for x in edl.get("graficos", []) if x.get("texto")]
    for i, x in enumerate(graficos):
        cuerpo = "<div class='grafico'><h2>%s</h2>%s</div>" % (
            esc(x["texto"]), "<p>%s</p>" % esc(x["detalle"]) if x.get("detalle") else "")
        placas.append((html_placa(cuerpo, pal), tmp / ("grafico%02d.png" % i)))
    if preview:
        c = None  # la vista previa no lleva cierre: es para revisar la dirección
    if placas:
        renderizar_placas(placas)
    if c:
        seg_cierre = tmp / "s99.mp4"
        ff("-loop", "1", "-t", "%.2f" % c.get("segundos", 2.5), "-i", tmp / "cierre.png",
           "-f", "lavfi", "-t", "%.2f" % c.get("segundos", 2.5), "-i",
           "anullsrc=channel_layout=stereo:sample_rate=48000",
           "-vf", "scale=%d:%d,setsar=1,fps=%d,format=yuv420p" % (W, H, FPS),
           "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-c:a", "aac", "-b:a", "192k",
           "-shortest", seg_cierre)
        partes.append(seg_cierre)

    # 3 · Pegar
    lista = tmp / "lista.txt"
    lista.write_text("".join("file '%s'\n" % p.name for p in partes), encoding="utf-8")
    base = tmp / "base.mp4"
    ff("-f", "concat", "-safe", "0", "-i", "lista.txt", "-c", "copy", "base.mp4", cwd=tmp)
    total = sum(s["hasta"] - s["desde"] for s in edl["segmentos"])
    largo = total + (c.get("segundos", 2.5) if c else 0)
    if preview:
        largo = min(largo, preview)

    # 4 · Encima: placa del gancho, subtítulos, música, volumen
    entradas, filtros, v = ["-i", "base.mp4"], [], "[0:v]"
    n = 1
    if g and g.get("texto"):
        hasta = g.get("hasta") or total
        entradas += ["-i", "gancho.png"]
        filtros.append("%s[%d:v]overlay=0:0:enable='between(t,%.2f,%.2f)'[v%d]"
                       % (v, n, g.get("desde", 0), hasta, n))
        v, n = "[v%d]" % n, n + 1
    for i, x in enumerate(graficos):
        entradas += ["-i", "grafico%02d.png" % i]
        filtros.append("%s[%d:v]overlay=0:0:enable='between(t,%.2f,%.2f)'[v%d]"
                       % (v, n, x.get("desde", 0), x.get("hasta", total), n))
        v, n = "[v%d]" % n, n + 1
    for i, x in enumerate(edl.get("insertos", [])):
        archivo = buscar_archivo(proyecto, x["archivo"])
        d = x.get("desde", 0)
        dur = x.get("hasta", d + 2.5) - d
        forma = x.get("forma", "ventana")
        if archivo.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp"):
            entradas += ["-loop", "1", "-t", "%.2f" % dur, "-i", rel(archivo, tmp)]
        else:
            entradas += ["-ss", "%.2f" % x.get("inicio", 0), "-t", "%.2f" % dur, "-i", rel(archivo, tmp)]
        if forma == "pantalla":
            filtros.append("[%d:v]scale=%d:%d:force_original_aspect_ratio=increase,crop=%d:%d,setsar=1,fps=%d,"
                           "setpts=PTS-STARTPTS+%.3f/TB[i%d]" % (n, W, H, W, H, FPS, d, i))
            px, py = 0, 0
        elif forma == "arriba":
            filtros.append("[%d:v]scale=%d:%d:force_original_aspect_ratio=increase,crop=%d:%d,setsar=1,fps=%d,"
                           "setpts=PTS-STARTPTS+%.3f/TB[i%d]" % (n, W, H // 2, W, H // 2, FPS, d, i))
            px, py = 0, 0
        else:  # ventana: una tarjeta redondeada con borde blanco, como un recorte pegado
            an, al = x.get("ancho", 820), x.get("alto", 600)
            mascara_redondeada(tmp / ("mascara%02d.png" % i), an, al)
            filtros.append("[%d:v]scale=%d:%d:force_original_aspect_ratio=increase,crop=%d:%d,setsar=1,fps=%d,"
                           "pad=%d:%d:12:12:white,format=rgba[c%d]" % (n, an - 24, al - 24, an - 24, al - 24, FPS, an, al, i))
            entradas += ["-loop", "1", "-t", "%.2f" % dur, "-i", "mascara%02d.png" % i]
            n += 1
            filtros.append("[%d:v]format=gray,fps=%d[m%d];[c%d][m%d]alphamerge,setpts=PTS-STARTPTS+%.3f/TB[i%d]"
                           % (n, FPS, i, i, i, d, i))
            px, py = (W - an) // 2, x.get("y", 520)
        filtros.append("%s[i%d]overlay=%d:%d:enable='between(t,%.2f,%.2f)':eof_action=pass[vi%d]"
                       % (v, i, px, py, d, d + dur, i))
        v, n = "[vi%d]" % i, n + 1
    if edl.get("subtitulos", modo == "instructor"):
        if not (proyecto / "trabajo" / "transcripcion.json").exists():
            sys.exit("Los subtítulos necesitan la transcripción: preparar --transcribir")
        cantidad = subtitulos(edl, proyecto, tmp / "subs.ass")
        print("Subtítulos: %d palabras" % cantidad)
        filtros.append("%sass=subs.ass:fontsdir='%s'[vs]" % (v, rel(FUENTES, tmp)))
        v = "[vs]"
    a = "[0:a]"
    vo = edl.get("voz")
    if vo and vo.get("archivo"):
        archivo = proyecto / vo["archivo"] if (proyecto / vo["archivo"]).exists() else carpeta_de_clips(proyecto) / vo["archivo"]
        entradas += ["-i", rel(archivo, tmp)]
        ms = int(vo.get("desde", 0) * 1000)
        filtros.append("[%d:a]aresample=48000,aformat=channel_layouts=stereo,atrim=start=%.2f,asetpts=PTS-STARTPTS,"
                       "adelay=%d|%d,volume=%.2f[voz]" % (n, vo.get("recorte", 0), ms, ms, vo.get("volumen", 1.0)))
        filtros.append("%s[voz]amix=inputs=2:duration=first:normalize=0[av]" % a)
        a, n = "[av]", n + 1
    m = edl.get("musica")
    if m and m.get("archivo"):
        entradas += ["-stream_loop", "-1", "-i", rel(proyecto / m["archivo"], tmp)]
        vol = m.get("volumen", 0.9 if modo == "short" else 0.12)
        filtros.append("[%d:a]atrim=start=%.2f,asetpts=PTS-STARTPTS,volume=%.2f,"
                       "afade=t=out:st=%.2f:d=1.2[mus]" % (n, m.get("desde", 0), vol, max(0, largo - 1.2)))
        filtros.append("%s[mus]amix=inputs=2:duration=first:normalize=0[am]" % a)
        a, n = "[am]", n + 1
    filtros.append("%sloudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000,aformat=channel_layouts=stereo[af]" % a)
    a = "[af]"
    if v == "[0:v]":
        filtros.append("[0:v]null[vf]")
        v = "[vf]"

    version = 1 + max([int(m.group(1)) for p in proyecto.glob("video-*.mp4")
                       if (m := re.match(r"video-(\d+)", p.name))] or [0])
    salida = proyecto / ("video-%d%s.mp4" % (version, "-vista-previa" if preview else ""))
    ff(*entradas, "-filter_complex", ";".join(filtros), "-map", v, "-map", a,
       "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
       "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "-t", "%.3f" % largo,
       rel(salida, tmp), cwd=tmp)
    if animado:
        salida = animar(proyecto, salida, g_anim, graf_anim, c_anim, total, edl)
        largo = total + (c_anim.get("segundos", 2.5) if c_anim else 0)
    if edl.get("sonidos", True):
        poner_sonidos(salida, edl, total, animado, preview)
    al_inicio = float((edl.get("portada") or {}).get("al_inicio", 0) or 0)
    if al_inicio > 0 and not preview:
        largo += poner_portada(proyecto, edl, salida, al_inicio)
    versiones = trabajo / "versiones"
    versiones.mkdir(exist_ok=True)
    shutil.copy(ruta_edl, versiones / (salida.stem + ".edl.json"))
    print("→ %s  (%.1f s)" % (rel(salida, proyecto), largo))
    print("Siguiente: video.py revisar %s" % proyecto)


# ───────────────────────── efectos de sonido ─────────────────────────

# Generados con ffmpeg (tonos y ruido): son nuestros, sin licencia de terceros.
# whoosh: entra el gancho, una etiqueta o el cierre · pop: aparece un gráfico, un ítem de lista o
# un círculo · ding: veredicto ✓ (y el botón del cierre) · error: veredicto ✗ · tic: cada palabra
# del gancho animado. "sonidos": false en el edl los apaga.
SONIDOS = AQUI / "sonidos"


def poner_sonidos(video, edl, total, animado, preview):
    """Suma los efectos encima del audio del video, en los momentos de las capas."""
    eventos = []
    g = edl.get("gancho") or {}
    if g.get("texto"):
        t = g.get("desde", 0)
        if animado and g.get("animar"):  # sin animación, el título entra sin sonido
            eventos.append(("whoosh", t, 0.55))
            for i in range(len(g["texto"].split())):
                eventos.append(("tic", t + 0.15 + 0.08 * i, 0.35))
    for x in edl.get("graficos", []):
        if x.get("texto"):
            eventos.append(("pop", x.get("desde", 0), 0.7))
    for x in edl.get("insertos", []):
        eventos.append(("whoosh", x.get("desde", 0), 0.4))
    if animado:
        for x in edl.get("etiquetas", []):
            eventos.append(("whoosh", x.get("desde", 0), 0.45))
        for x in edl.get("listas", []):
            for k in range(len(x.get("items", []))):
                eventos.append(("pop", x.get("desde", 0) + 0.2 + x.get("paso", 0.6) * k, 0.6))
        for x in edl.get("veredictos", []):
            eventos.append(("ding" if x.get("tipo", "bien") == "bien" else "error", x.get("desde", 0), 0.6))
        for x in edl.get("flechas", []):
            eventos.append(("pop", x.get("desde", 0), 0.6))
        for x in edl.get("capitulos", []):
            eventos.append(("whoosh", x.get("desde", 0), 0.5))
        for x in edl.get("recortes", []):
            eventos.append(("pop", x.get("desde", 0), 0.6))
    c = edl.get("cierre")
    if c and not preview:
        eventos.append(("whoosh", total, 0.55))
        if c.get("boton"):
            eventos.append(("ding", total + 0.4, 0.5))
    if not eventos:
        return
    entradas, filtros = ["-i", video], []
    for i, (nombre, t, vol) in enumerate(eventos, 1):
        entradas += ["-i", SONIDOS / (nombre + ".wav")]
        ms = int(t * 1000)
        filtros.append("[%d:a]volume=%.2f,adelay=%d|%d[e%d]" % (i, vol, ms, ms, i))
    mezcla = "".join("[e%d]" % i for i in range(1, len(eventos) + 1))
    filtros.append("[0:a]%samix=inputs=%d:duration=first:normalize=0[a]" % (mezcla, len(eventos) + 1))
    con = video.with_name(video.stem + "-sfx.mp4")
    ff(*entradas, "-filter_complex", ";".join(filtros), "-map", "0:v", "-map", "[a]",
       "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", con)
    con.replace(video)


# ───────────────────────── capas animadas (HyperFrames) ─────────────────────────

HF = AQUI / "hyperframes"

ESTILO_HF = """
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { width: 1080px; height: 1920px; overflow: hidden; background: #111; }
#root { position: relative; width: 100%; height: 100%; }
.clip { position: absolute; inset: 0; }
video.clip { width: 100%; height: 100%; object-fit: cover; }
.gancho, .grafico { inset: auto; }
"""


ESTILO_EXTRA = """
.etiqueta { inset: auto; left: %(izq)dpx; top: 960px; background: %(base)s; color: %(tinta)s; border-radius: 22px;
  padding: 22px 34px; font-family: Switzer, sans-serif; border-left: 14px solid %(acento)s; }
.etiqueta b { display: block; font-size: 52px; font-weight: 800; letter-spacing: -0.02em; }
.etiqueta span { display: block; font-size: 34px; font-weight: 600; color: %(acento)s; margin-top: 4px; }
.lista { inset: auto; left: %(izq)dpx; right: %(der)dpx; top: 640px; font-family: Switzer, sans-serif; }
.lista h3 { display: inline-block; background: %(golpe)s; color: %(golpe_tinta)s; font-size: 44px; font-weight: 800;
  padding: 10px 26px; border-radius: 16px; margin-bottom: 18px; }
.lista li { list-style: none; display: flex; align-items: center; gap: 22px; background: %(base)s; color: %(tinta)s;
  font-size: 54px; font-weight: 800; letter-spacing: -0.02em; padding: 18px 30px; border-radius: 20px; margin-top: 14px; }
.lista li i { font-style: normal; display: grid; place-items: center; width: 64px; height: 64px; border-radius: 50%%;
  background: %(acento)s; color: %(base)s; font-size: 38px; flex: none; }
.veredicto { display: grid; place-items: center; }
.veredicto .sello { display: flex; flex-direction: column; align-items: center; gap: 18px; font-family: Switzer, sans-serif; }
.veredicto .marca { width: 300px; height: 300px; border-radius: 50%%; display: grid; place-items: center; font-size: 210px;
  font-weight: 900; line-height: 1; color: #fff; }
.veredicto.bien .marca { background: #2d9d2d; }
.veredicto.mal .marca { background: #dc2626; }
.veredicto .sello b { background: rgba(6,8,6,.85); color: #fff; font-size: 64px; font-weight: 800; padding: 12px 34px; border-radius: 18px; }
.flecha { inset: auto; font-family: Switzer, sans-serif; }
.flecha .punta { width: 120px; height: 120px; border-radius: 50%%; border: 12px solid %(acento)s; }
.flecha b { position: absolute; left: 140px; top: 20px; white-space: nowrap; background: %(acento)s; color: %(base)s;
  font-size: 46px; font-weight: 800; padding: 10px 26px; border-radius: 999px; }
"""


# ───────── Estilos de animación: el mismo contenido, cuatro maneras de verse ─────────
# Se elige con "estilo_animacion" en el edl: cine-sticker (por defecto), caja, fuerte, sticker o cine.
# Los colores salen siempre de la paleta.
ESTILOS_ANIMACION = {
    "caja": "",
    # FUERTE: sin cajas, letra enorme en mayúsculas con borde grueso, la palabra clave sobre un bloque de color
    "fuerte": """
#root.fuerte .gancho, #root.fuerte .grafico, #root.fuerte .etiqueta, #root.fuerte .lista li { background: none; }
#root.fuerte .gancho h1, #root.fuerte .lista li, #root.fuerte .grafico .dato, #root.fuerte .etiqueta b {
  color: #fff; text-transform: uppercase; font-weight: 900; -webkit-text-stroke: 14px #0a0a0a; paint-order: stroke fill;
  text-shadow: 0 10px 0 rgba(0,0,0,.35); letter-spacing: -0.02em; }
#root.fuerte .gancho h1 { font-size: 104px; line-height: .98; }
#root.fuerte .gancho .resalta { background: %(acento)s; color: %(base)s; -webkit-text-stroke: 0; text-shadow: none;
  padding: 0 14px; display: inline-block; transform: rotate(-2deg); }
#root.fuerte .gancho p { display: inline-block; background: #0a0a0a; color: %(acento)s; padding: 8px 20px; text-transform: uppercase; }
#root.fuerte .grafico .dato { font-size: 150px; color: %(acento)s; }
#root.fuerte .grafico p { color: #fff; -webkit-text-stroke: 8px #0a0a0a; paint-order: stroke fill; font-weight: 800; font-size: 48px; }
#root.fuerte .lista h3 { background: %(acento)s; color: %(base)s; text-transform: uppercase; transform: rotate(-2deg); }
#root.fuerte .lista li { padding: 4px 0; font-size: 76px; }
#root.fuerte .lista li i { background: %(acento)s; color: %(base)s; -webkit-text-stroke: 0; width: 88px; height: 88px; font-size: 52px; border-radius: 18px; }
#root.fuerte .etiqueta { border: 0; padding: 0; }
#root.fuerte .etiqueta b { font-size: 80px; }
#root.fuerte .etiqueta span { display: inline-block; background: %(acento)s; color: %(base)s; padding: 6px 18px; text-transform: uppercase; }
#root.fuerte .veredicto .marca { background: none !important; font-size: 360px; -webkit-text-stroke: 16px #0a0a0a; paint-order: stroke fill; }
#root.fuerte .veredicto.bien .marca { color: #3ddc4f; } #root.fuerte .veredicto.mal .marca { color: #ff3b3b; }
#root.fuerte .veredicto .sello b { text-align: center; background: none; font-size: 96px; font-weight: 900; text-transform: uppercase; -webkit-text-stroke: 12px #0a0a0a; paint-order: stroke fill; }
""",
    # STICKER: etiquetas blancas inclinadas con sombra, como recortes pegados; acentos a mano
    "sticker": """
@font-face { font-family: Caveat; src: url(caveat-latin-700-normal.woff2); font-weight: 700; }
#root.sticker .gancho { background: #fff; color: #111; transform: rotate(-2.5deg); box-shadow: 0 18px 40px rgba(0,0,0,.35); right: auto; max-width: 900px; }
#root.sticker .gancho .resalta { background: %(acento)s; color: %(base)s; padding: 0 12px; border-radius: 14px; display: inline-block; }
#root.sticker .gancho p { font-family: Caveat, cursive; font-size: 64px; font-weight: 700; color: %(base)s; transform: rotate(-3deg); }
#root.sticker .grafico { background: %(acento)s; color: %(base)s; transform: rotate(2deg); box-shadow: 0 18px 40px rgba(0,0,0,.35); right: auto; }
#root.sticker .etiqueta { background: #fff; color: #111; border: 0; transform: rotate(-3deg); box-shadow: 0 14px 30px rgba(0,0,0,.35); }
#root.sticker .etiqueta span { font-family: Caveat, cursive; font-size: 46px; color: %(base)s; }
#root.sticker .lista h3 { font-family: Caveat, cursive; font-size: 72px; background: none; color: #fff; text-shadow: 0 4px 12px rgba(0,0,0,.6); }
#root.sticker .lista li { background: #fff; color: #111; width: fit-content; box-shadow: 0 14px 30px rgba(0,0,0,.3); }
#root.sticker .lista li:nth-child(odd) { transform: rotate(-2deg); } #root.sticker .lista li:nth-child(even) { transform: rotate(1.8deg); margin-left: 40px; }
#root.sticker .veredicto .sello { transform: rotate(-8deg); }
#root.sticker .veredicto .marca { width: 260px; height: 260px; font-size: 170px; border: 10px solid #fff; box-shadow: 0 18px 40px rgba(0,0,0,.4); }
#root.sticker .veredicto .sello b { background: #fff; color: #111; font-family: Caveat, cursive; font-size: 84px; }
#root.sticker .flecha b { background: #fff; color: #111; transform: rotate(-3deg); box-shadow: 0 10px 24px rgba(0,0,0,.35); }
#root.sticker .flecha .punta { border-color: #fff; border-style: dashed; }
""",
    # CINE: sin cajas, letra más fina con itálica, sombra suave y líneas finas; más lento y elegante
    "cine": """
#root.cine::after { content: ""; position: absolute; inset: 0; pointer-events: none;
  background: linear-gradient(180deg, rgba(0,0,0,.45) 0%%, transparent 28%%, transparent 62%%, rgba(0,0,0,.55) 100%%); }
#root.cine .gancho, #root.cine .grafico, #root.cine .etiqueta, #root.cine .lista li { background: none; box-shadow: none; z-index: 2; }
#root.cine .gancho h1 { font-weight: 600; font-size: 88px; letter-spacing: -0.02em; text-shadow: 0 4px 30px rgba(0,0,0,.6); color: #fff; }
#root.cine .gancho .resalta { font-style: italic; font-weight: 800; color: %(acento)s; }
#root.cine .gancho p { font-weight: 600; font-size: 30px; letter-spacing: .3em; text-transform: uppercase; color: #fff; opacity: .85; }
#root.cine .grafico { border-left: 4px solid %(acento)s; border-radius: 0; color: #fff; padding: 10px 0 10px 36px; }
#root.cine .grafico .dato { font-weight: 600; font-style: italic; text-shadow: 0 4px 30px rgba(0,0,0,.6); }
#root.cine .grafico p { letter-spacing: .2em; text-transform: uppercase; font-size: 28px; }
#root.cine .etiqueta { border: 0; border-left: 4px solid %(acento)s; border-radius: 0; color: #fff; padding: 6px 0 6px 28px; }
#root.cine .etiqueta b { font-weight: 600; font-size: 56px; text-shadow: 0 4px 20px rgba(0,0,0,.6); }
#root.cine .etiqueta span { color: #fff; opacity: .8; letter-spacing: .2em; text-transform: uppercase; font-size: 24px; }
#root.cine .lista h3 { background: none; color: #fff; letter-spacing: .25em; text-transform: uppercase; font-size: 34px; font-weight: 700; padding: 0; text-shadow: 0 2px 16px rgba(0,0,0,.9); }
#root.cine .lista li { color: #fff; font-weight: 600; font-size: 60px; padding: 18px 0; border-radius: 0; border-bottom: 2px solid rgba(255,255,255,.35); text-shadow: 0 2px 6px rgba(0,0,0,.7), 0 4px 30px rgba(0,0,0,.8); }
#root.cine .lista li i { background: none; color: %(acento)s; font-style: italic; font-weight: 800; font-size: 54px; width: auto; }
#root.cine .veredicto .marca { width: 170px; height: 170px; font-size: 110px; background: none !important; border: 4px solid; }
#root.cine .veredicto.bien .marca { color: %(acento)s; } #root.cine .veredicto.mal .marca { color: #ff6b6b; }
#root.cine .veredicto .sello b { background: none; font-weight: 600; font-style: italic; font-size: 72px; text-shadow: 0 4px 24px rgba(0,0,0,.7); }
#root.cine .flecha .punta { border-width: 4px; }
#root.cine .flecha b { background: none; color: #fff; font-style: italic; font-weight: 600; text-shadow: 0 4px 20px rgba(0,0,0,.8); }
""",
}


# CINE-STICKER (el de por defecto): todo como cine, menos los destacados (listas,
# punteos, opciones), que van como recortes de sticker pegados encima
_cine = [l.replace(", #root.cine .lista li", "") for l in ESTILOS_ANIMACION["cine"].strip().split("\n")
         if ".lista" not in l.replace(", #root.cine .lista li", "")]
_sticker = [l for l in ESTILOS_ANIMACION["sticker"].strip().split("\n") if ".lista" in l or "@font-face" in l]
ESTILOS_ANIMACION["cine-sticker"] = "\n" + "\n".join(_cine + _sticker).replace("#root.cine ", "#root.cine-sticker ").replace(
    "#root.cine::after", "#root.cine-sticker::after").replace("#root.sticker ", "#root.cine-sticker ") + "\n"
POR_DEFECTO = "cine-sticker"


def css_estilo(edl, pal):
    estilo = (edl or {}).get("estilo_animacion", POR_DEFECTO)
    estilo = estilo if estilo in ESTILOS_ANIMACION else POR_DEFECTO
    return estilo, ESTILOS_ANIMACION[estilo] % pal


ESTILO_NUEVO = """
@font-face { font-family: Caveat; src: url(caveat-latin-700-normal.woff2); font-weight: 700; }
#root .gancho { left: 110px; right: 110px; text-align: center; }
.texto-fijo, .frase { inset: auto; left: 110px; right: 110px; text-align: center; color: #fff;
  font-size: 50px; line-height: 1.28; text-shadow: 0 0 3px rgba(0,0,0,.9), 0 1px 2px rgba(0,0,0,.9), 0 2px 14px rgba(0,0,0,.6), 0 0 30px rgba(0,0,0,.45); }
.texto-fijo .resalta, .frase .resalta { color: %(acento)s; position: relative; }
.raya { position: absolute; left: -2%%; right: -2%%; bottom: -.16em; height: .24em; transform-origin: left center; }
.texto-fijo .kicker { color: %(acento)s; font-weight: 800; }
.texto-fijo p + p { margin-top: 14px; }
.texto-fijo p, .texto-fijo .kicker, .frase, #root .gancho h1 { text-wrap: balance; }
.texto-fijo.info { left: 150px; right: 150px; font-size: 46px; line-height: 1.24; }
.texto-fijo.info .kicker { font-size: 56px; line-height: 1.05; letter-spacing: -0.02em; opacity: 1; margin-bottom: 22px; }
.texto-fijo .kicker, .frase .kicker { font-size: .78em; opacity: .9; margin-bottom: 14px; display: block; }
.velo { background: linear-gradient(180deg, rgba(0,0,0,.5) 0%%, rgba(0,0,0,.38) 30%%, rgba(0,0,0,0) 55%%); }
.capitulo { display: grid; place-items: center; text-align: center; font-family: Switzer, sans-serif; }
.capitulo .num { font-family: Caveat, cursive; font-size: 150px; font-weight: 700; color: %(acento)s; line-height: .8;
  text-shadow: 0 4px 24px rgba(0,0,0,.6); }
.capitulo b { display: inline-block; background: #fff; color: #111; font-size: 76px; font-weight: 800; letter-spacing: -0.03em;
  padding: 18px 40px; border-radius: 22px; transform: rotate(-2deg); box-shadow: 0 18px 40px rgba(0,0,0,.4); max-width: 880px; }
.repaso { inset: auto; left: %(izq)dpx; top: 250px; font-family: Switzer, sans-serif; color: #fff; font-size: 30px; font-weight: 600;
  line-height: 1.45; text-shadow: 0 2px 8px rgba(0,0,0,.8); }
.repaso i { font-style: normal; color: %(acento)s; font-weight: 800; }
.recorte { inset: auto; }
.recorte img { width: 100%%; display: block; filter: drop-shadow(7px 0 0 #fff) drop-shadow(-7px 0 0 #fff) drop-shadow(0 7px 0 #fff)
  drop-shadow(0 -7px 0 #fff) drop-shadow(0 16px 22px rgba(0,0,0,.4)); }
"""


# La letra de los videos de texto (como las de Instagram: simple, blanca, con sombra fina)
FUENTES_TEXTO = {
    "poppins": ("Poppins", "poppins-latin-600-normal.woff2", 600),
    "switzer": ("Switzer", "switzer-latin-600-normal.woff2", 600),
    "questrial": ("Questrial", "questrial-latin-400-normal.woff2", 400),
    "serif": ("Instrument Serif", "instrument-serif-latin-400-normal.woff2", 400),
}
POSICIONES_TEXTO = {"arriba": 300, "cielo": 480, "medio": 760}  # o "centro": en el medio exacto


# El título (gancho): cinco diseños. Por defecto "marcador" ; los otros se piden
# con "diseno" en el gancho, o "diseno": "turnar" para que salga del número de la pieza.
DISENOS_GANCHO = ("subrayado", "mezcla", "serif", "espaciado", "marcador", "simple")


def diseno_gancho(g, proyecto, tipo="instructor"):
    if g.get("diseno") in DISENOS_GANCHO:
        return g["diseno"]
    if g.get("diseno") != "turnar":
        return "simple" if tipo == "frases" else "marcador"  # en frases el título va limpio
    n = re.match(r"(\d+)", proyecto.name)
    return DISENOS_GANCHO[int(n.group(1)) % len(DISENOS_GANCHO) if n else 0]


def raya_svg(color, grosor=9):
    """Un trazo a mano, como subrayado con marcador (para el título y las frases)."""
    svg = ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 24' preserveAspectRatio='none'>"
           "<path d='M5 15 C 70 7, 160 5, 295 11' stroke='%s' stroke-width='%d' fill='none' stroke-linecap='round'/></svg>"
           % (color, grosor))
    return "url(\"data:image/svg+xml;utf8,%s\")" % svg.replace("#", "%23").replace('"', "'")


def css_gancho(pal):
    raya = raya_svg(pal["acento"])
    return """
@font-face { font-family: "Instrument Serif"; src: url(instrument-serif-latin-400-normal.woff2); font-weight: 400; }
@font-face { font-family: "Instrument Serif"; src: url(instrument-serif-latin-400-italic.woff2); font-weight: 400; font-style: italic; }
#root .gancho.d-subrayado h1 { font-family: Switzer, sans-serif; font-weight: 800; font-size: 86px; letter-spacing: -0.035em; }
#root .gancho.d-subrayado .resalta { color: #fff; font-style: normal; padding-bottom: .14em;
  background: %(raya)s no-repeat left bottom / 100%% .3em; }
#root .gancho.d-mezcla h1 { font-family: Switzer, sans-serif; font-weight: 800; font-size: 80px; letter-spacing: -0.035em; }
#root .gancho.d-mezcla .resalta { font-family: "Instrument Serif", serif; font-style: italic; font-weight: 400;
  font-size: 1.32em; letter-spacing: -0.01em; color: %(acento)s; line-height: .8; }
#root .gancho.d-serif h1 { font-family: "Instrument Serif", serif; font-weight: 400; font-size: 108px; line-height: .98;
  letter-spacing: -0.015em; }
#root .gancho.d-serif .resalta { font-style: italic; font-weight: 400; color: %(acento)s; }
#root .gancho.d-espaciado h1 { font-family: Switzer, sans-serif; font-weight: 600; font-size: 40px; letter-spacing: .28em;
  text-transform: uppercase; line-height: 1.5; }
#root .gancho.d-espaciado .resalta { display: block; font-weight: 900; font-style: normal; font-size: 150px; letter-spacing: -0.045em;
  line-height: .92; margin: .06em 0 .1em; color: %(acento)s; }
#root .gancho.d-simple h1 { font-family: Switzer, sans-serif; font-weight: 800; font-size: 80px; letter-spacing: -0.03em; }
#root .gancho.d-simple .resalta { color: inherit; font-style: normal; }
#root .gancho.d-marcador h1 { font-family: Switzer, sans-serif; font-weight: 800; font-size: 84px; letter-spacing: -0.035em; }
#root .gancho.d-marcador .resalta { color: %(base)s; font-style: normal; text-shadow: none; padding: 0 .12em; margin: 0 -.04em;
  background: linear-gradient(transparent 12%%, %(acento)s 12%%, %(acento)s 92%%, transparent 92%%); transform: rotate(-1.5deg); }
""" % dict(raya=raya, **pal)


def frase_desde(t, k, total):
    """Cuándo entra la frase k de un video de texto: "tiempos" si los hay, si no repartidas parejo."""
    if t.get("tiempos"):
        return t["tiempos"][k]
    return 0.3 + (total - 0.3) * k / max(1, len(t.get("frases", [])))


def capas_nuevas(edl, total, capas, anim, proyecto, hf):
    """Lo de los dos tipos: textos en pantalla (tipo texto) y capítulos, repaso y recortes (instructor)."""
    t = edl.get("textos") or {}
    tipo = tipo_de(edl)
    def marcar(frase, raya=False):
        h = esc(frase)
        extra = "<i class='raya'></i>" if raya else ""
        if "**" in h:  # lo resaltado se marca en la misma frase, como en la ficha: "El ritmo lo ponés **vos**"
            return re.sub(r"\*\*(.+?)\*\*", lambda m: "<span class='resalta'>%s%s</span>" % (m.group(1), extra), h)
        for r in t.get("resalta", []):  # o con la lista "resalta": la parte que importa, en el acento
            h = re.sub("(?i)(%s)" % re.escape(esc(r)), r"<span class='resalta'>\1%s</span>" % ("<i class='raya'></i>" if raya else ""),
                       h, count=1)
        return h
    if t:
        fuente = t.get("fuente", "serif" if tipo == "inspiracion" else "poppins")
        familia, archivo, peso = FUENTES_TEXTO.get(fuente, FUENTES_TEXTO["poppins"])
        shutil.copy(FUENTES / archivo, hf / archivo)
        posicion = t.get("posicion", "cielo" if tipo == "frases" else "centro")
        lugar = ("top: 0; bottom: 0; display: flex; flex-direction: column; justify-content: center;"
                 if posicion == "centro" else "top: %dpx;" % POSICIONES_TEXTO.get(posicion, 480))
        capas.append('<style>@font-face { font-family: "%s"; src: url(%s); font-weight: %d; } '
                     '.texto-fijo, .frase { font-family: "%s", sans-serif; font-weight: %d; %s %s }'
                     '.raya { background: %s no-repeat center / 100%% 100%%; }</style>'
                     % (familia, archivo, peso, familia, peso, lugar,
                        "font-size: 78px; line-height: 1.08;" if familia == "Instrument Serif" else "",
                        raya_svg(paleta(edl)["acento"], 11)))
        if familia == "Instrument Serif":
            capas.append('<style>.texto-fijo .resalta, .frase .resalta { font-style: italic; }</style>')
        if t.get("velo", posicion != "centro"):  # oscurece apenas arriba (el cielo es claro)
            capas.append('<div id="velo" class="clip velo" data-start="0" data-duration="%.2f"></div>' % total)
    kicker = "<span class='kicker'>%s</span>" % esc(t["kicker"]) if t.get("kicker") else ""
    formato = t.get("formato", "frases" if (tipo == "frases" or t.get("frases")) else "fijo")
    if formato == "fijo" and t.get("texto"):
        # todo el video, quieto: aparece desde el primer cuadro, sin animación
        parrafos = "".join("<p>%s</p>" % marcar(x) for x in t["texto"].split("\n") if x.strip())
        capas.append('<div id="tf" class="clip texto-fijo %s" data-start="0" data-duration="%.2f">%s%s</div>'
                     % ("info" if tipo == "info" else "", total, kicker, parrafos))
    for k, f in enumerate(t.get("frases", [])):
        # una frase por vez, con corte seco: la frase no se anima, el subrayado de lo destacado se dibuja
        d = 0 if k == 0 else frase_desde(t, k, total)
        h = frase_desde(t, k + 1, total) if k + 1 < len(t["frases"]) else total
        capas.append('<div id="fr%d" class="clip frase" data-start="%.2f" data-duration="%.2f">%s%s</div>'
                     % (k, d, h - d, kicker if k == 0 else "", marcar(f, raya=t.get("subrayar", True))))
        anim.append('tl.from("#fr%d .raya", {scaleX: 0, duration: 0.45, ease: "power2.out"}, %.2f);' % (k, d + 0.25))
    caps = edl.get("capitulos", [])
    for i, x in enumerate(caps):
        d = x.get("desde", 0)
        h = x.get("hasta", d + 2.2)
        num = x.get("numero", i + 1)
        capas.append('<div id="ca%d" class="clip capitulo" data-start="%.2f" data-duration="%.2f"><div>'
                     '<div class="num">%s.</div><b>%s</b></div></div>' % (i, d, h - d, esc(str(num)), esc(x["texto"])))
        anim.append('tl.from("#ca%d .num", {y: -30, opacity: 0, duration: 0.35, ease: "back.out(2)"}, %.2f);' % (i, d))
        anim.append('tl.from("#ca%d b", {scale: 0.5, opacity: 0, rotation: -10, duration: 0.4, ease: "back.out(2.2)"}, %.2f);' % (i, d + 0.12))
        if edl.get("repaso"):
            hasta_r = caps[i + 1]["desde"] if i + 1 < len(caps) else total
            items = "<br>".join("<i>%s.</i> %s" % (esc(str(c.get("numero", j + 1))), esc(c["texto"])) for j, c in enumerate(caps[:i + 1]))
            capas.append('<div id="re%d" class="clip repaso" data-start="%.2f" data-duration="%.2f">%s</div>'
                         % (i, h, max(0.1, hasta_r - h), items))
            anim.append('tl.from("#re%d", {x: -30, opacity: 0, duration: 0.3}, %.2f);' % (i, h))
    for i, x in enumerate(edl.get("recortes", [])):
        archivo = buscar_archivo(proyecto, x["archivo"])
        nombre = "recorte%02d%s" % (i, archivo.suffix.lower())
        shutil.copy(archivo, hf / nombre)
        d = x.get("desde", 0)
        h = x.get("hasta", d + 2.5)
        an = x.get("ancho", 420)
        capas.append('<div id="rc%d" class="clip recorte" style="width:%dpx;left:%dpx;top:%dpx;transform:rotate(%.1fdeg)" '
                     'data-start="%.2f" data-duration="%.2f"><img src="%s" alt=""></div>'
                     % (i, an, int(x.get("x", 0.5) * W - an / 2), int(x.get("y", 0.5) * H - an / 2), x.get("giro", -6), d, h - d, nombre))
        anim.append('tl.from("#rc%d img", {scale: 0, rotation: -25, duration: 0.45, ease: "back.out(2.4)"}, %.2f);' % (i, d))


def capas_extra(edl, total, capas, anim):
    """Elementos para los videos más armados (de instructor): etiqueta con el nombre, lista que aparece
    de a un ítem, veredicto ✓/✗, y un círculo que señala algo de la imagen. Solo con "animado"."""
    for i, x in enumerate(edl.get("etiquetas", [])):
        d, h = x.get("desde", 0), x.get("hasta", x.get("desde", 0) + 3)
        capas.append('<div id="et%d" class="clip etiqueta" data-start="%.2f" data-duration="%.2f"><b>%s</b>%s</div>'
                     % (i, d, h - d, esc(x["texto"]), "<span>%s</span>" % esc(x["detalle"]) if x.get("detalle") else ""))
        anim.append('tl.from("#et%d", {x: -500, opacity: 0, duration: 0.5, ease: "power3.out"}, %.2f);' % (i, d))
    for i, x in enumerate(edl.get("listas", [])):
        d, h = x.get("desde", 0), x.get("hasta", total)
        items = "".join("<li><i>%d</i>%s</li>" % (k + 1, esc(t)) for k, t in enumerate(x["items"]))
        capas.append('<div id="li%d" class="clip lista" data-start="%.2f" data-duration="%.2f">%s<ul>%s</ul></div>'
                     % (i, d, h - d, "<h3>%s</h3>" % esc(x["titulo"]) if x.get("titulo") else "", items))
        paso = x.get("paso", 0.6)
        anim.append('tl.from("#li%d h3", {y: -20, opacity: 0, duration: 0.3}, %.2f);' % (i, d))
        anim.append('tl.from("#li%d li", {x: -60, opacity: 0, duration: 0.35, stagger: %.2f, ease: "back.out(1.8)"}, %.2f);'
                    % (i, paso, d + 0.2))
    for i, x in enumerate(edl.get("veredictos", [])):
        d, h = x.get("desde", 0), x.get("hasta", x.get("desde", 0) + 1.6)
        bien = x.get("tipo", "bien") == "bien"
        capas.append('<div id="ve%d" class="clip veredicto %s" data-start="%.2f" data-duration="%.2f"><div class="sello">'
                     '<div class="marca">%s</div>%s</div></div>' % (i, "bien" if bien else "mal", d, h - d,
                     "✓" if bien else "✗", "<b>%s</b>" % esc(x["texto"]) if x.get("texto") else ""))
        anim.append('tl.from("#ve%d .marca", {scale: 2.2, opacity: 0, rotation: -12, duration: 0.35, ease: "back.out(2.5)"}, %.2f);' % (i, d))
        anim.append('tl.from("#ve%d .sello b", {y: 30, opacity: 0, duration: 0.3}, %.2f);' % (i, d + 0.25))
    for i, x in enumerate(edl.get("flechas", [])):
        d, h = x.get("desde", 0), x.get("hasta", x.get("desde", 0) + 2.5)
        left, top = int(x.get("x", 0.5) * W) - 60, int(x.get("y", 0.5) * H) - 60
        capas.append('<div id="fl%d" class="clip flecha" style="left:%dpx;top:%dpx" data-start="%.2f" data-duration="%.2f">'
                     '<div class="punta"></div>%s</div>' % (i, left, top, d, h - d,
                     "<b>%s</b>" % esc(x["texto"]) if x.get("texto") else ""))
        anim.append('tl.from("#fl%d .punta", {scale: 0, duration: 0.4, ease: "back.out(3)"}, %.2f);' % (i, d))
        anim.append('tl.to("#fl%d .punta", {scale: 1.15, duration: 0.4, yoyo: true, repeat: 3}, %.2f);' % (i, d + 0.4))
        if x.get("texto"):
            anim.append('tl.from("#fl%d b", {x: -30, opacity: 0, duration: 0.3}, %.2f);' % (i, d + 0.2))


def animar(proyecto, base, g, graficos, c, total, edl=None):
    """Arma las capas con movimiento (gancho palabra por palabra, gráfico que aparece, cierre)
    sobre el video ya cortado, con HyperFrames. Deja video-N.mp4 en lugar de la base."""
    if not shutil.which("npx"):
        sys.exit("Las capas animadas necesitan Node.js 22 o más:  winget install OpenJS.NodeJS.LTS")
    hf = proyecto / "trabajo" / "hyperframes"
    if hf.exists():
        shutil.rmtree(hf)
    hf.mkdir(parents=True)
    shutil.move(str(base), hf / "base.mp4")
    pal = paleta(edl)
    for archivo in ("switzer-latin-600-normal.woff2", "switzer-latin-800-normal.woff2",
                    "switzer-latin-900-normal.woff2", "poppins-latin-600-normal.woff2",
                    "caveat-latin-700-normal.woff2"):
        shutil.copy(FUENTES / archivo, hf / archivo)
    shutil.copy(HF / "gsap.min.js", hf / "gsap.min.js")
    for archivo in ("instrument-serif-latin-400-normal.woff2", "instrument-serif-latin-400-italic.woff2"):
        shutil.copy(FUENTES / archivo, hf / archivo)
    shutil.copy(LOGOS / pal["logo"], hf / "logo.png")

    cierre_s = c.get("segundos", 2.5) if c else 0
    capas, anim = [], []
    capas.append('<video id="base" class="clip" src="base.mp4" data-start="0" data-duration="%.2f" '
                 'data-has-audio="true"></video>' % total)
    if g and g.get("texto"):
        res = set((g.get("resalta") or "").split())
        palabras = " ".join("<span%s>%s</span>" % (" class='resalta'" if p in res else "", esc(p))
                            for p in g["texto"].split())
        remate = "<p>%s</p>" % esc(g["remate"]) if g.get("remate") else ""
        hasta = g.get("hasta") or total
        diseno = diseno_gancho(g, proyecto, tipo_de(edl or {}))
        capas.append('<div id="gancho" class="clip gancho d-%s" data-start="%.2f" data-duration="%.2f">'
                     '<h1>%s</h1>%s</div>' % (diseno, g.get("desde", 0), hasta - g.get("desde", 0), palabras, remate))
        t = g.get("desde", 0)
        if g.get("animar"):  # por defecto el título aparece de una, sin animación
            anim.append('tl.from("#gancho", {y: -40, opacity: 0, duration: 0.4, ease: "back.out(2)"}, %.2f);' % t)
            anim.append('tl.from("#gancho h1 span", {y: 30, opacity: 0, duration: 0.3, stagger: 0.08, ease: "power3.out"}, %.2f);' % (t + 0.15))
        if remate and g.get("animar"):
            anim.append('tl.from("#gancho p", {opacity: 0, y: 16, duration: 0.3}, %.2f);' % (t + 0.4 + 0.08 * len(g["texto"].split())))
    for i, x in enumerate(x for x in graficos if x.get("texto")):
        ident = "grafico%d" % i
        detalle = "<p>%s</p>" % esc(x["detalle"]) if x.get("detalle") else ""
        desde, hasta = x.get("desde", 0), x.get("hasta", total)
        capas.append('<div id="%s" class="clip grafico" data-start="%.2f" data-duration="%.2f">'
                     '<div class="dato">%s</div>%s</div>' % (ident, desde, hasta - desde, esc(x["texto"]), detalle))
        anim.append('tl.from("#%s", {scale: 0.6, opacity: 0, duration: 0.45, ease: "back.out(2.2)"}, %.2f);' % (ident, desde))
        if detalle:
            anim.append('tl.from("#%s p", {y: 20, opacity: 0, duration: 0.35}, %.2f);' % (ident, desde + 0.35))
    capas_extra(edl or {}, total, capas, anim)
    capas_nuevas(edl or {}, total, capas, anim, proyecto, hf)
    if c:
        boton = '<div class="wa">%s</div>' % esc(c["boton"]) if c.get("boton") else ""
        capas.append('<div id="cierre" class="clip cierre" data-start="%.2f" data-duration="%.2f">'
                     '<img src="logo.png" alt=""><h2>%s</h2>%s<div class="cuenta">%s</div></div>'
                     % (total, cierre_s, con_resalta(c.get("texto", ""), c.get("resalta")), boton, esc(CUENTA)))
        anim.append('tl.from("#cierre img", {y: 40, opacity: 0, duration: 0.4}, %.2f);' % (total + 0.05))
        anim.append('tl.from("#cierre h2", {y: 40, opacity: 0, duration: 0.4}, %.2f);' % (total + 0.2))
        if boton:
            anim.append('tl.from("#cierre .wa", {scale: 0.7, opacity: 0, duration: 0.4, ease: "back.out(2)"}, %.2f);' % (total + 0.4))

    estilo, css_e = css_estilo(edl, pal)
    css = ESTILO_HF + css_capas(pal, 1, ".") + ESTILO_EXTRA % dict(
        izq=SEGURA["izquierda"], der=SEGURA["derecha"], **pal) + ESTILO_NUEVO % dict(
        izq=SEGURA["izquierda"], der=SEGURA["derecha"], **pal) + css_e + css_gancho(pal)
    html = ("<!doctype html>\n<html lang=\"es\" data-resolution=\"portrait\"><head><meta charset=\"UTF-8\">"
            "<meta name=\"viewport\" content=\"width=1080, height=1920\">"
            "<script src=\"gsap.min.js\"></script><style>%s</style></head><body>"
            "<div id=\"root\" class=\"%s\" data-composition-id=\"main\" data-start=\"0\" data-duration=\"%.2f\" "
            "data-width=\"1080\" data-height=\"1920\">\n%s\n</div><script>\n"
            "const tl = gsap.timeline({paused: true});\n%s\n"
            "window.__timelines[\"main\"] = tl; tl.seek(0);\n</script></body></html>\n"
            % (css, estilo, total + cierre_s, "\n".join(capas), "\n".join(anim)))
    (hf / "index.html").write_text(html, encoding="utf-8")
    (hf / "hyperframes.json").write_text("{}\n", encoding="utf-8")

    salida = base
    print("Capas animadas con HyperFrames (tarda un minuto)…")
    npx = shutil.which("npx")
    entorno = {**os.environ, "HYPERFRAMES_SKIP_SKILLS": "1"}
    if not entorno.get("HYPERFRAMES_BROWSER_PATH"):  # en Windows usa el Chrome (o Edge) instalado
        for p in (r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                  r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                  r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"):
            if Path(p).exists():
                entorno["HYPERFRAMES_BROWSER_PATH"] = p
                break
    r = subprocess.run([npx, "-y", "hyperframes@latest", "render", "-o", str(salida)], cwd=hf,
                       env=entorno,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode or not salida.exists():
        sys.exit("HyperFrames falló. La composición quedó en %s; para verla: cd ahí y npx hyperframes preview\n%s"
                 % (rel(hf, proyecto), (r.stdout + r.stderr)[-1500:]))
    return salida


# ───────────────────────── portada ─────────────────────────

CARRUSEL = RAIZ / ".claude" / "skills" / "carrusel"

ESTILO_PORTADA = """
.slide.reel { width: 540px; height: 960px; padding: 0 48px; }
.reel .foto-mitad { margin: 0 -48px; height: 500px; }
.reel .cuerpo { margin: 30px 0 0; gap: 14px; }
.reel h1 { font-size: 78px; }
.reel .firma { margin-top: 26px; }
.reel .resto { flex: 1; }
"""


def portada(proyecto):
    """Arma portada.png con el estilo de los carruseles. Devuelve la ruta."""
    edl = json.loads((proyecto / "edl.json").read_text(encoding="utf-8"))
    po = edl.get("portada")
    if not po or not po.get("titulo"):
        sys.exit('Falta "portada" en edl.json, con al menos "titulo". Ver .claude/skills/editar-video/SKILL.md')
    trabajo = proyecto / "trabajo"
    trabajo.mkdir(exist_ok=True)
    cuadro = trabajo / "portada-cuadro.jpg"
    if po.get("foto"):
        shutil.copy(proyecto / po["foto"], cuadro)
    else:
        clip = ruta_clip(proyecto, po.get("clip") or edl["segmentos"][0]["clip"])
        seg = po.get("segundo", edl["segmentos"][0]["desde"] + 0.5)
        ff("-ss", "%.2f" % seg, "-i", clip, "-frames:v", "1", "-q:v", "2", "-vf",
           "scale=1080:-2", cuadro)
    titulo = esc(po["titulo"])
    if po.get("resalta"):
        r = esc(po["resalta"])
        titulo = titulo.replace(r, "<span class='resalta'>%s</span>" % r, 1)
    rosa = " rosa" if po.get("rosa") else ""
    partes = ["<div class='foto-mitad'><img src='%s'></div>" % cuadro.as_uri(),
              "<div class='cuerpo'>"]
    if po.get("kicker"):
        partes.append("<span class='kicker'>%s</span>" % esc(po["kicker"]))
    if po.get("sticker"):
        partes.append("<span class='sticker encima'>%s</span>" % esc(po["sticker"]))
    partes.append("<h1>%s</h1></div>" % titulo)
    partes.append("<div class='firma'><div class='iso'></div><div><b>%s</b>"
                  "<span>%s</span></div></div><div class='resto'></div>" % (esc(CUENTA), esc(DESCRIPTOR)))
    html = ("<!doctype html><html lang='es'><head><meta charset='utf-8'>"
            "<link rel='stylesheet' href='%s'><style>%s body{padding:0;background:none}</style></head>"
            "<body class='paleta-%s'><section class='slide reel%s'>%s</section></body></html>"
            % ((CARRUSEL / "base.css").as_uri(), ESTILO_PORTADA, po.get("paleta", edl.get("paleta", PALETA_DEFECTO)), rosa,
               "".join(partes)))
    destino = proyecto / "portada.png"
    renderizar_placas([(html, destino)])
    print("→ %s  (se sube como portada del reel)" % rel(destino, proyecto))
    return destino


def poner_portada(proyecto, edl, video, segundos):
    """Pone la portada al principio del video, los segundos que diga el edl. Devuelve los segundos."""
    png = proyecto / "portada.png"
    if not png.exists():
        png = portada(proyecto)
    con = video.with_name(video.stem + "-tmp.mp4")
    ff("-loop", "1", "-t", "%.3f" % segundos, "-i", png,
       "-f", "lavfi", "-t", "%.3f" % segundos, "-i", "anullsrc=channel_layout=stereo:sample_rate=48000",
       "-i", video, "-filter_complex",
       "[0:v]scale=%d:%d,fps=%d,format=yuv420p,setsar=1[p];[2:v]fps=%d,format=yuv420p,setsar=1[v];"
       "[p][1:a][v][2:a]concat=n=2:v=1:a=1[vo][ao]" % (W, H, FPS, FPS),
       "-map", "[vo]", "-map", "[ao]", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
       "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", con)
    con.replace(video)
    return segundos


# ───────────────────────── revisar ─────────────────────────

def videos(proyecto):
    return sorted([p for p in proyecto.glob("video-*.mp4") if re.match(r"video-\d+", p.name)],
                  key=lambda p: int(re.match(r"video-(\d+)", p.name).group(1)))


def revisar(proyecto):
    final = videos(proyecto)
    if not final:
        sys.exit("No hay ningún video-N.mp4 en el proyecto. Primero: armar")
    video = final[-1]
    guardado = proyecto / "trabajo" / "versiones" / (video.stem + ".edl.json")
    edl = json.loads((guardado if guardado.exists() else proyecto / "edl.json").read_text(encoding="utf-8"))
    corrida = 0.0 if "vista-previa" in video.name else float((edl.get("portada") or {}).get("al_inicio", 0) or 0)
    momentos, t = [0.6], corrida
    for seg in edl["segmentos"]:
        momentos.append(t + 0.15)                              # recién cortado
        momentos.append(t + (seg["hasta"] - seg["desde"]) / 2)  # medio de la toma
        t += seg["hasta"] - seg["desde"]
    for x in edl.get("graficos", []):
        momentos.append(corrida + x.get("desde", 0) + 0.3)
    if edl.get("cierre") and "vista-previa" not in video.name:
        momentos.append(t + 0.5)
    momentos = sorted(set(round(m, 2) for m in momentos))
    duracion = sondear(video)["duracion"]
    momentos = [m for m in momentos if m < duracion - 0.05]

    tmp = proyecto / "trabajo" / "revision"
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir(parents=True)
    marco = ("drawbox=x=0:y=0:w=iw:h=%d:color=red@0.25:t=fill,"
             "drawbox=x=0:y=%d:w=iw:h=ih-%d:color=red@0.25:t=fill,"
             "drawbox=x=iw-%d:y=0:w=%d:h=ih:color=red@0.25:t=fill,"
             "drawbox=x=0:y=0:w=%d:h=ih:color=red@0.25:t=fill" % (
                 SEGURA["arriba"], SEGURA["abajo"], SEGURA["abajo"],
                 SEGURA["derecha"], SEGURA["derecha"], SEGURA["izquierda"]))
    fuente = rel(FUENTES / "Poppins-SemiBold.ttf", tmp)
    for i, m in enumerate(momentos):
        ff("-ss", "%.2f" % m, "-i", rel(video, tmp), "-frames:v", "1", "-vf",
           marco + ",scale=270:-2,drawtext=fontfile='%s':text='%s':x=6:y=6:fontsize=20:"
           "fontcolor=white:box=1:boxcolor=black@0.7:boxborderw=4" % (fuente, ("%.1fs" % m).replace(":", "")),
           "c%02d.png" % i, cwd=tmp)
    columnas = min(6, len(momentos))
    ff("-i", "c%02d.png", "-vf", "tile=%dx%d:padding=6:color=white" % (
        columnas, math.ceil(len(momentos) / columnas)), "-frames:v", "1",
       "../revision.jpg", cwd=tmp)

    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(video), "-af", "ebur128",
                        "-f", "null", "-"], capture_output=True, text=True)
    lufs = re.findall(r"I:\s+(-?[\d.]+) LUFS", r.stderr)
    info = sondear(video)
    print("Video:     %s · %dx%d · %.1f s" % (rel(video, proyecto), info["ancho"], info["alto"],
                                             info["duracion"]))
    print("Volumen:   %s LUFS (Instagram: entre -16 y -13)" % (lufs[-1] if lufs else "?"))
    print("Revisión:  %s — lo rojo es lo que tapan la app y el pie" % rel(
        proyecto / "trabajo" / "revision.jpg", proyecto))


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("accion", choices=["preparar", "armar", "revisar", "portada"])
    p.add_argument("proyecto")
    p.add_argument("--transcribir", action="store_true")
    p.add_argument("--modelo", default="small", help="Modelo de Whisper: small, medium…")
    p.add_argument("--vista-previa", type=float, metavar="SEGUNDOS",
                   help="armar: solo los primeros N segundos, sin cierre, para aprobar la dirección")
    a = p.parse_args()
    if not shutil.which("ffmpeg"):
        sys.exit("No encuentro ffmpeg. En Windows:  winget install Gyan.FFmpeg  (y abrir otra terminal)")
    proyecto = Path(a.proyecto).resolve()
    if a.accion == "preparar":
        preparar(proyecto, a.transcribir, a.modelo)
    elif a.accion == "armar":
        armar(proyecto, a.vista_previa)
    elif a.accion == "portada":
        portada(proyecto)
    else:
        revisar(proyecto)


if __name__ == "__main__":
    main()
