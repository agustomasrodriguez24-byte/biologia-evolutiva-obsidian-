---
tipo: pilar
pilar:
  - cronobiologia
fecha_revision: 2026-10-03
---

# P04 Cronobiología, sueño y recuperación

El tiempo biológico: ritmos, luz, sueño y recuperación.

Toda intervención de este pilar se documenta como: **intervención → mecanismo propuesto → evidencia → riesgo → aplicación**.

## Subpilares y temas a desarrollar

**Ritmos**: [[Ritmo circadiano]] · Ritmos ultradianos · Ritmos infradianos · Temperatura corporal
**Señales temporales**: Luz · Exposición solar · Melatonina · Cortisol · Crononutrición · Timing de comidas · Actividad física
**Disrupción**: Jet lag · Turnos nocturnos · Luz nocturna
**Sueño**: Arquitectura del sueño · NREM · REM · Sueño profundo · Adenosina · Vigilia
**Recuperación**: Sistema nervioso autónomo · Estrés · Descanso · Rituales pre-sueño · Temperatura y ambiente del dormitorio

## Nodos del pilar

```base
filters:
  and:
    - 'pilar.contains("cronobiologia")'
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
