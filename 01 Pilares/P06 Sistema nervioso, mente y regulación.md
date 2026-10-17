---
tipo: pilar
pilar:
  - mente
fecha_revision: 2026-10-03
---

# P06 Sistema nervioso, mente y regulación

> [!warning] Separación obligatoria en este pilar
> Diferenciá **concepto filosófico** de **concepto psicológico** de **mecanismo fisiológico demostrado**. Presencia o conciencia pueden estar en el sistema, pero no se presentan como mecanismos biomédicos sin evidencia.

## Subpilares y temas a desarrollar

**Sistema nervioso autónomo**: Simpático · Parasimpático · Nervio vago
**Estrés y regulación**: Estrés · Regulación emocional · Estado emocional · Respiración
**Cognición**: Percepción · Atención · Neuroplasticidad
**Prácticas**: Meditación · Presencia

## Nodos del pilar

```base
filters:
  and:
    - 'pilar.contains("mente")'
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
