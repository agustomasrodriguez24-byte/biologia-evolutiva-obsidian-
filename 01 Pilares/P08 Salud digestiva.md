---
tipo: pilar
pilar:
  - digestiva
fecha_revision: 2026-10-03
---

# P08 Salud digestiva

## Subpilares y temas a desarrollar

**Órganos (en orden de recorrido)**: Boca · Estómago · Hígado · Vesícula · Páncreas · Intestino delgado · Colon
**Secreciones**: Ácido gástrico · Pepsina
**Procesos**: Digestión · Absorción · Motilidad · Eliminación
**Ecosistema y barrera**: Microbiota · Permeabilidad intestinal

## Nodos del pilar

```base
filters:
  and:
    - 'pilar.contains("digestiva")'
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
