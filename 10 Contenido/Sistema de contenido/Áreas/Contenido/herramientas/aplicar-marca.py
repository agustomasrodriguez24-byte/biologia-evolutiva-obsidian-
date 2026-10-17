#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aplica la ficha de la marca al sistema. Se corre cada vez que cambia Empresa/Marca/marca.json.

    python Áreas/Contenido/herramientas/aplicar-marca.py

Hace tres cosas:

1. Escribe .claude/skills/carrusel/marca.css: los colores, las letras y las paletas que usan los
   carruseles, las historias y las portadas. Ese archivo NO se edita a mano: se cambia la ficha y
   se vuelve a correr esto
2. Chequea el contraste de cada paleta (texto sobre fondo 4,5:1; acento sobre fondo 3:1)
3. Revisa que estén los logos (Empresa/Marca/logos/logo-fondo-oscuro.png y logo-fondo-claro.png)
4. Avisa qué falta completar en la ficha (lo que sigue con {{...}} o con el valor de ejemplo)

video.py y revisar-texto.py leen la ficha directo: no hace falta nada más para ellos.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import marca as M  # noqa: E402

DESTINO = M.RAIZ / ".claude" / "skills" / "carrusel" / "marca.css"


def bloque(nombre, p, primero):
    selector = "body" if primero else "body.paleta-%s" % nombre
    if primero:
        selector = "body, body.paleta-%s" % nombre
    lb = "var(--logo-oscuro)" if M.oscuro(p["base"]) else "var(--logo-claro)"
    lc = "var(--logo-oscuro)" if M.oscuro(p["clara"]) else "var(--logo-claro)"
    lg = "var(--logo-oscuro)" if M.oscuro(p["golpe"]) else "var(--logo-claro)"
    return """%s {
  /* base */  --b-fondo: %s; --b-tinta: %s; --b-suave: %s; --b-acento: %s; --b-linea: %s;
  /* clara */ --c-fondo: %s; --c-tinta: %s; --c-suave: %s; --c-acento: %s; --c-linea: %s;
  /* golpe */ --g-fondo: %s; --g-tinta: %s; --g-suave: %s; --g-acento: %s; --g-linea: %s;
  --b-logo: %s; --c-logo: %s; --g-logo: %s;
}
""" % (selector,
       p["base"], p["tinta_base"], M.rgba(p["tinta_base"], .8), p["acento"], M.rgba(p["tinta_base"], .25),
       p["clara"], p["tinta_clara"], M.rgba(p["tinta_clara"], .78), p["acento_clara"], M.rgba(p["tinta_clara"], .2),
       p["golpe"], p["tinta_golpe"], M.rgba(p["tinta_golpe"], .85), p["tinta_golpe"], M.rgba(p["tinta_golpe"], .3),
       lb, lc, lg)


def contraste(a, b):
    la, lb = sorted([M.luminancia(a), M.luminancia(b)], reverse=True)
    return (la + .05) / (lb + .05)


def main():
    f = M.dato("fuentes", {}) or {}
    pals = M.paletas()
    defecto = M.paleta_por_defecto()
    orden = [defecto] + [n for n in pals if n != defecto]

    css = ["/* GENERADO por aplicar-marca.py desde Empresa/Marca/marca.json. No se edita a mano. */",
           ":root {",
           "  --font-display: '%s', sans-serif;" % f.get("marca", "Poppins"),
           "  --font-body: '%s', sans-serif;" % f.get("texto", "Switzer"),
           "  --mk-tinta-oscura: %s;" % M.dato("color_tinta_oscura", "#141414"),
           "  --mk-whatsapp: %s;" % M.dato("color_whatsapp", "#25d366"),
           "  --radius-card: %s;" % M.dato("radio", "22px"),
           "}",
           "body {",
           "  --f-titulo: '%s', var(--font-body); --f-texto: '%s', var(--font-body);" % (
               f.get("titulo", "Switzer"), f.get("texto", "Switzer")),
           "  --f-frase: '%s', '%s', sans-serif; --f-marca: var(--font-display);" % (
               f.get("frase", "Bricolage Grotesque"), f.get("titulo", "Switzer")),
           "  --f-mano: '%s', cursive; --f-serif: '%s', serif;" % (f.get("mano", "Caveat"), f.get("serif", "Instrument Serif")),
           '  --logo-oscuro: url("../../../Empresa/Marca/logos/logo-fondo-oscuro.png");',
           '  --logo-claro: url("../../../Empresa/Marca/logos/logo-fondo-claro.png");',
           "}",
           "/* Paletas: %s. La primera es la de por defecto */" % " · ".join("paleta-" + n for n in orden)]
    for i, n in enumerate(orden):
        css.append(bloque(n, pals[n], i == 0))
    DESTINO.write_text("\n".join(css) + "\n", encoding="utf-8")
    print("Escrito:", DESTINO.relative_to(M.RAIZ))
    print("Paletas:", ", ".join(orden), "(por defecto: %s)" % defecto)

    print("\nContraste:")
    malos = 0
    for n, p in pals.items():
        for f, tt, minimo in [("base", "tinta_base", 4.5), ("base", "acento", 3), ("clara", "tinta_clara", 4.5),
                              ("clara", "acento_clara", 3), ("golpe", "tinta_golpe", 4.5)]:
            r = contraste(p[f], p[tt])
            if r < minimo:
                malos += 1
                print("  MAL  paleta %s: %s sobre %s da %.1f (mínimo %s)" % (n, tt, f, r, minimo))
    if not malos:
        print("  OK en todas las paletas")

    faltan = []
    for clave in ("nombre", "cuenta", "descriptor", "rubro", "ciudad", "cta.boton"):
        v = M.dato(clave)
        if not v or M.es_placeholder(v) or "000 000" in str(v) or str(v).startswith("Lo que hacés"):
            faltan.append(clave)
    if any(M.es_placeholder(h) or h in ("#TuRubro", "#TuCiudad") for h in M.dato("hashtags_marca", [])):
        faltan.append("hashtags_marca")
    for logo in ("logo-fondo-oscuro.png", "logo-fondo-claro.png"):
        if not (M.LOGOS / logo).exists():
            faltan.append("logo: Empresa/Marca/logos/" + logo)
    if list(M.LOGOS.glob("BORRAR-ESTO*")):
        faltan.append("logos: los de Empresa/Marca/logos/ son de ejemplo (reemplazarlos y borrar el aviso)")
    if faltan:
        print("\nFALTA completar:")
        for x in faltan:
            print("  -", x)
        print("Se puede seguir: las piezas salen, pero con los datos de ejemplo.")
    else:
        print("\nLa ficha está completa.")


if __name__ == "__main__":
    main()
