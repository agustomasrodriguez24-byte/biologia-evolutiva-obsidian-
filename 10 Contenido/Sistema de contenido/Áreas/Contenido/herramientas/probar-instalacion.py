#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prueba que esta compu tenga todo lo que usan los videos, los carruseles y los datos.

    python Áreas/Contenido/herramientas/probar-instalacion.py

Revisa Python, FFmpeg, Node.js, HyperFrames (con el Chrome de la compu), faster-whisper (baja el
modelo la primera vez y transcribe 10 segundos de un video, si encuentra uno en Material/) y
Playwright. No cambia nada. Deja el resultado en instalacion.txt, al lado de este archivo, para que
Claude lo lea. Tarda unos minutos la primera vez (el modelo pesa ~500 MB).
"""
import os, platform, shutil, subprocess, sys, time
from pathlib import Path

AQUI = Path(__file__).resolve().parent
MUESTRA = next((p for p in sorted((AQUI.parent / "Material").rglob("*"))
                if p.suffix.lower() in (".mp4", ".mov", ".m4v")), AQUI / "no-hay-video.mp4")
lineas = []


def anotar(ok, que, detalle=""):
    marca = "OK " if ok is True else ("-- " if ok is None else "MAL")
    linea = "%s  %-22s %s" % (marca, que, detalle)
    print(linea)
    lineas.append(linea)


def correr(cmd, timeout=120):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout,
                           shell=(os.name == "nt"), encoding="utf-8", errors="replace")
        return r.returncode, (r.stdout + r.stderr).strip()
    except Exception as e:
        return 1, str(e)


def chrome():
    for p in (os.environ.get("HYPERFRAMES_BROWSER_PATH"),
              r"C:\Program Files\Google\Chrome\Application\chrome.exe",
              r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
              r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
              r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
              shutil.which("google-chrome"), shutil.which("chromium")):
        if p and Path(p).exists():
            return p
    return None


anotar(None, "Sistema", "%s · Python %s" % (platform.platform(), platform.python_version()))
anotar(sys.version_info >= (3, 10), "Python 3.10 o más", platform.python_version())

for prog in ("ffmpeg", "ffprobe"):
    c, out = correr([prog, "-version"])
    anotar(c == 0, prog, out.splitlines()[0] if c == 0 and out else "no está: winget install Gyan.FFmpeg")

c, out = correr(["node", "-v"])
ver = out.strip().lstrip("v") if c == 0 else ""
anotar(c == 0 and int((ver or "0").split(".")[0]) >= 22, "Node.js 22 o más",
       out if c == 0 else "no está: winget install OpenJS.NodeJS.LTS")

c, out = correr(["npx", "-y", "hyperframes@latest", "--version"], timeout=300)
anotar(c == 0, "HyperFrames", out.splitlines()[-1] if out else "")
navegador = chrome()
anotar(bool(navegador), "Chrome o Edge", navegador or "no encontré Chrome ni Edge (HyperFrames lo necesita)")

try:
    from faster_whisper import WhisperModel
    anotar(True, "faster-whisper", "instalado")
    if MUESTRA.exists():
        t = time.time()
        modelo = WhisperModel("small", device="auto", compute_type="auto")
        import numpy as np  # el audio lo decodifica ffmpeg, no PyAV (igual que video.py)
        crudo = subprocess.run(["ffmpeg", "-v", "error", "-t", "10", "-i", str(MUESTRA), "-f", "s16le",
                                "-ac", "1", "-ar", "16000", "-"], capture_output=True).stdout
        audio = np.frombuffer(crudo, np.int16).astype(np.float32) / 32768.0
        segs, _ = modelo.transcribe(audio, language="es")
        texto = " ".join(s.text.strip() for s in segs)
        anotar(bool(texto), "Transcribe", "%.0f s · \"%s\"" % (time.time() - t, texto[:90]))
    else:
        anotar(None, "Transcribe", "no hay ningún video en Material/ para probar: se prueba con el primero que cargues")
except ImportError:
    anotar(False, "faster-whisper", "no está: pip install faster-whisper")
except Exception as e:
    anotar(False, "Transcribe", str(e)[:150])

try:
    import playwright  # noqa: F401
    anotar(True, "Playwright", "instalado (carruseles y placas)")
except ImportError:
    anotar(None, "Playwright", "no está: los carruseles usan Chrome directo. Opcional: pip install playwright")

(AQUI / "instalacion.txt").write_text("\n".join(lineas) + "\n", encoding="utf-8")
print("\nListo. El resultado quedó en", AQUI / "instalacion.txt")
