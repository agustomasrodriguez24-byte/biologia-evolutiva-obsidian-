---
tipo: pilar
pilar:
  - biologia
fecha_revision: 2026-10-03
---

# P01 Biología humana y fundamentos

La base sobre la que se apoyan los otros nueve pilares: cómo está hecho el organismo, cómo obtiene energía y cómo mantiene su equilibrio interno.

## Subpilares y temas a desarrollar

Los temas en texto plano todavía no tienen nota. Cuando se cree una, reemplazalo por un `[[enlace]]`.

**Sistemas**
- Anatomía · Fisiología · Bioquímica
- Sistema nervioso · endocrino · inmunológico · digestivo · cardiovascular · musculoesquelético · renal · reproductivo

**Energía y metabolismo**
- ATP · Mitocondrias · Glucosa · Ácidos grasos · Cuerpos cetónicos
- Metabolismo energético · Flexibilidad metabólica
- Insulina · Glucagón · AMPK · mTOR

**Homeostasis**
- Temperatura · Glucosa · Presión osmótica · Electrolitos · pH · Balance ácido-base · Osmolaridad · Equilibrio hidroelectrolítico

## Nodos del pilar

```base
filters:
  and:
    - 'pilar.contains("biologia")'
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
