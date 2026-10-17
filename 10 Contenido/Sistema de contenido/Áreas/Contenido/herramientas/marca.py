#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lee la ficha de la marca (Empresa/Marca/marca.json) para los demás scripts.

No se corre solo: lo importan video.py, revisar-texto.py y aplicar-marca.py. Así el nombre, la
cuenta, los hashtags, lo prohibido y las paletas se escriben una sola vez.
"""
import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent.parent
FICHA = RAIZ / "Empresa" / "Marca" / "marca.json"
LOGOS = RAIZ / "Empresa" / "Marca" / "logos"

NEUTRA = {
    "base": "#1f2a44", "tinta_base": "#ffffff", "acento": "#ffd23f",
    "clara": "#f3f4f8", "tinta_clara": "#1f2a44", "acento_clara": "#3b5bdb",
    "golpe": "#ffd23f", "tinta_golpe": "#1f2a44",
}


def cargar():
    try:
        return json.loads(FICHA.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as e:
        raise SystemExit("Empresa/Marca/marca.json tiene un error de formato (línea %d): %s" % (e.lineno, e.msg))


MARCA = cargar()


def dato(clave, defecto=""):
    """Un dato de la ficha, con un valor de reserva si falta."""
    v = MARCA
    for parte in clave.split("."):
        if not isinstance(v, dict) or parte not in v:
            return defecto
        v = v[parte]
    return v


def es_placeholder(valor):
    return isinstance(valor, str) and ("{{" in valor or valor == "@tucuenta" or valor.startswith("#Tu"))


def luminancia(hexa):
    h = hexa.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in (r, g, b)]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def oscuro(hexa):
    return luminancia(hexa) < 0.35


def rgba(hexa, alfa):
    h = hexa.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return "rgba(%d,%d,%d,%s)" % (r, g, b, alfa)


def logo_para(fondo):
    """Qué logo va sobre un fondo: el de fondo oscuro o el de fondo claro."""
    return "logo-fondo-oscuro.png" if oscuro(fondo) else "logo-fondo-claro.png"


def paletas():
    """Las paletas de la ficha, completas. Siempre hay al menos una."""
    crudas = {k: v for k, v in (dato("paletas", {}) or {}).items() if isinstance(v, dict)}
    if not crudas:
        crudas = {"principal": NEUTRA}
    salida = {}
    for nombre, p in crudas.items():
        q = {**NEUTRA, **{k: v for k, v in p.items() if not k.startswith("_")}}
        salida[nombre] = q
    return salida


def paleta_por_defecto():
    pals = paletas()
    n = dato("paleta_por_defecto", "")
    return n if n in pals else next(iter(pals))


def paletas_video():
    """Las paletas con la forma que usa video.py: base, tinta, acento, golpe, golpe_tinta, logo."""
    return {n: dict(base=p["base"], tinta=p["tinta_base"], acento=p["acento"], golpe=p["golpe"],
                    golpe_tinta=p["tinta_golpe"], logo=logo_para(p["base"]))
            for n, p in paletas().items()}
