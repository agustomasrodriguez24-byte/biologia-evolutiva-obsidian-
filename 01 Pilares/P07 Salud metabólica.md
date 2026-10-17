---
tipo: pilar
pilar:
  - metabolica
fecha_revision: 2026-10-03
---

# P07 Salud metabólica

Muchos temas de este pilar son también **métricas**: van en `07 Métricas/` con unidad y forma de medición, y se enlazan desde los conceptos.

## Subpilares y temas a desarrollar

**Regulación de la glucosa**: Insulina · Glucemia · HbA1c · Sensibilidad a la insulina · Flexibilidad metabólica
**Lípidos**: Triglicéridos · HDL · LDL
**Cardiovascular**: Presión arterial
**Composición corporal**: Circunferencia abdominal · Composición corporal
**Cuadros**: Síndrome metabólico · Inflamación

## Nodos del pilar

```base
filters:
  and:
    - 'pilar.contains("metabolica")'
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
