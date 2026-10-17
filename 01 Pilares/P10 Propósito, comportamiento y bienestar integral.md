---
tipo: pilar
pilar:
  - proposito
fecha_revision: 2026-10-03
---

# P10 Propósito, comportamiento y bienestar integral

La parte más propia de la marca.

> [!warning] Credibilidad
> Los conceptos espirituales y existenciales tienen lugar en el sistema, pero no se presentan como mecanismos biomédicos demostrados. Cuando exista investigación (por ejemplo, sobre hábitos, conducta o relaciones sociales), se enlaza con su nivel de evidencia; cuando no, se marca como E o se deja como reflexión.

## Subpilares y temas a desarrollar

**Sentido**: Propósito · Valores · Identidad · Sentido · Coherencia
**Vínculos**: Relaciones · Comunidad · Trabajo
**Prácticas**: Gratitud · Presencia · Espiritualidad
**Conducta**: Hábitos · Conducta · Desarrollo personal

## Nodos del pilar

```base
filters:
  and:
    - 'pilar.contains("proposito")'
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
