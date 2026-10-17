---
tipo: pilar
pilar:
  - movimiento
fecha_revision: 2026-10-03
---

# P05 Movimiento y condición física

Referencia institucional de base: [[OMS - Actividad física]].

## Subpilares y temas a desarrollar

**Capacidades**: Fuerza · Hipertrofia · Potencia · Resistencia · VO₂max
**Modalidades**: Zona 2 · HIIT · Caminata · Movilidad
**Movimiento cotidiano**: NEAT · Postura · Equilibrio
**Recuperación** (cruza con [[P04 Cronobiología, sueño y recuperación]])

## Nodos del pilar

```base
filters:
  and:
    - 'pilar.contains("movimiento")'
    - 'tipo != "pilar"'
views:
  - type: table
    name: Nodos
    groupBy:
      property: tipo
      direction: ASC
    order:
      - file.name
      - subpilar
      - nivel_evidencia
      - estado
      - fecha_revision
```

Volver a [[Inicio]].
