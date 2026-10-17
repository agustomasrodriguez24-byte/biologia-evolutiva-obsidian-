---
tipo: pilar
pilar:
  - hidratacion
fecha_revision: 2026-10-03
---

# P03 Hidratación y equilibrio hidroelectrolítico

Agua, electrolitos y balance hídrico.

> [!warning] Separación obligatoria en este pilar
> Acá conviven evidencia científica, hipótesis, el modelo Unani, experiencia personal y protocolos experimentales. Cada uno va en su capa: evidencia en `02 Conceptos/` con su nivel, modelos tradicionales en `11 Hipótesis/` (E), experiencias en `09 Experimentos/`.

## Subpilares y temas a desarrollar

**Agua y balance**: Agua · Agua de consumo · Balance hídrico · Osmolaridad
**Electrolitos**: [[Sodio]] · Potasio · Magnesio · Cloro · Bebidas con electrolitos
**Pérdidas y recuperación**: Sudoración · Deshidratación · Rehidratación
**Moduladores**: Actividad física · Temperatura ambiental

## Nodos del pilar

```base
filters:
  and:
    - 'pilar.contains("hidratacion")'
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
