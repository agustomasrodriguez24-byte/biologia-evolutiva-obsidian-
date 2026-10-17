"""Exporta cada lámina de un carrusel a PNG de 1080 x 1350.

Uso:  python .claude/skills/carrusel/render.py Áreas/Contenido/outputs/<aaaa-mm>/carruseles/<NN-tema>

NN es el número de la pieza en el plan del mes (Pieza 3 → 03-tema).

Abre el index.html de la carpeta con Chrome (o Edge) sin ventana, una vez por lámina, y deja
slide-01.png, slide-02.png... en la misma carpeta, al lado del index.html. Las fuentes están en el repo (Áreas/Contenido/herramientas/fuentes): no hace falta internet.

**Usa Playwright si está instalado** (`pip install playwright`, una sola vez). No hace falta
`playwright install`: usa el Chrome o el Edge que ya tiene la máquina. Es el camino bueno,
porque fija el tamaño exacto de la pantalla.

Sin Playwright usa Chrome por línea de comando. Ahí Chrome descuenta el marco de la ventana
de la altura y la lámina sale cortada abajo, así que se abre más alta y se recorta con Pillow
(`pip install pillow`). Si tampoco está Pillow, avisa y no exporta.
"""
import os
import re
import subprocess
import sys
from pathlib import Path

ANCHO, ALTO, ESCALA = 540, 675, 2
# Historias: 540 x 960 de CSS → 1080 x 1920. Se detecta por class="slide historia"

NAVEGADORES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
]


def con_playwright(html, laminas, salida, ancho=ANCHO, alto=ALTO, nombre="slide"):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        navegador = None
        for canal in ("chrome", "msedge", None):
            try:
                navegador = p.chromium.launch(channel=canal) if canal else p.chromium.launch()
                break
            except Exception:
                continue
        if navegador is None:
            raise RuntimeError("Playwright no encontró Chrome ni Edge")
        pagina = navegador.new_page(viewport={"width": ancho, "height": alto},
                                    device_scale_factor=ESCALA)
        for n in range(1, laminas + 1):
            png = salida / f"{nombre}-{n:02d}.png"
            pagina.goto(f"{html.as_uri()}?s={n}")
            pagina.wait_for_load_state("networkidle")
            pagina.evaluate("document.fonts.ready")
            pagina.screenshot(path=str(png))
            print(png.relative_to(salida.parent))
        navegador.close()


def con_chrome(html, laminas, salida, ancho=ANCHO, alto=ALTO, nombre="slide"):
    try:
        from PIL import Image
    except ImportError:
        sys.exit("Falta Playwright o Pillow. Instalar uno:  pip install playwright")
    ruta = next((r for r in NAVEGADORES if Path(r).exists()), None)
    if not ruta:
        sys.exit("No encontré Chrome ni Edge instalados.")
    # Como root (Linux, contenedores) Chrome no arranca sin --no-sandbox
    extra = ["--no-sandbox"] if hasattr(os, "geteuid") and os.geteuid() == 0 else []
    for n in range(1, laminas + 1):
        png = salida / f"{nombre}-{n:02d}.png"
        subprocess.run([
            ruta, *extra, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            f"--force-device-scale-factor={ESCALA}", f"--window-size={ancho},{alto + 200}",
            "--virtual-time-budget=6000", f"--screenshot={png}",
            f"{html.as_uri()}?s={n}",
        ], check=True, capture_output=True)
        Image.open(png).crop((0, 0, ancho * ESCALA, alto * ESCALA)).save(png)
        print(png.relative_to(salida.parent))


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    carpeta = Path(sys.argv[1]).resolve()
    html = carpeta / "index.html"
    texto = html.read_text(encoding="utf-8")
    laminas = len(re.findall(r'<section class="slide[ "]', texto))
    historia = 'class="slide historia' in texto
    medidas = dict(ancho=540, alto=960, nombre="historia") if historia else {}
    salida = carpeta
    for viejo in list(salida.glob("slide-*.png")) + list(salida.glob("historia-*.png")):  # una lámina borrada no tiene que quedar colgada
        viejo.unlink()
    try:
        con_playwright(html, laminas, salida, **medidas)
    except ImportError:
        con_chrome(html, laminas, salida, **medidas)
    if re.search(r'<body class="[^"]*\blinkedin\b', texto):  # LinkedIn se sube como documento PDF
        from PIL import Image
        hojas = [Image.open(p).convert("RGB") for p in sorted(salida.glob("slide-*.png"))]
        hojas[0].save(salida / "carrusel.pdf", save_all=True, append_images=hojas[1:], resolution=144)
        print("PDF para LinkedIn:", salida / "carrusel.pdf")


if __name__ == "__main__":
    main()
