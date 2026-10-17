---
tipo: pilar
pilar:
  - entorno
fecha_revision: 2026-10-03
---

# P09 Entorno y exposiciones

El pilar más propio del enfoque evolutivo: la distancia entre el entorno en el que evolucionamos y el entorno actual.

## Subpilares y temas a desarrollar

**Luz**: Luz solar · Luz artificial · Pantallas
**Temperatura**: Frío · Calor
**Naturaleza y aire**: Naturaleza · Aire · Ruido · Calidad del ambiente
**Químicos**: Contaminantes · Cosméticos · Productos domésticos
**Social**: Contacto social

## Nodos del pilar

```base
filters:
  and:
    - 'pilar.contains("entorno")'
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
