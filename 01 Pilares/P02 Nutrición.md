---
tipo: pilar
pilar:
  - nutricion
fecha_revision: 2026-10-03
---

# P02 Nutrición

Qué comemos, cómo se digiere y absorbe, y cómo la calidad del alimento afecta al organismo.

Referencia institucional de base: [[OMS - Alimentación saludable]] (adecuación, equilibrio, moderación, diversidad y seguridad).

## Subpilares y temas a desarrollar

**Macronutrientes**: Proteínas · Grasas · Carbohidratos · Fibra
**Micronutrientes**: Vitaminas · Minerales · Densidad nutricional · Biodisponibilidad
**Calidad del alimento**: Alimentos mínimamente procesados · Ultraprocesados · Digestibilidad · Antinutrientes
**Timing**: Timing alimentario (cruza con [[P04 Cronobiología, sueño y recuperación]])

## Nodos del pilar

```base
filters:
  and:
    - 'pilar.contains("nutricion")'
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
