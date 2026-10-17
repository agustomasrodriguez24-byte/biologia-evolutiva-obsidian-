---
tipo: sistema
fecha_revision: 2026-10-03
---

# Matriz de Cobertura Nutricional

> No alcanza con preguntar qué nutrientes tiene un alimento. Hay que preguntar: **¿cuánto contiene → cuánto se libera → cuánto se absorbe → cuánto puede usar el organismo → lo necesita esta persona?**

Esta matriz convierte la composición nutricional en **valor nutricional efectivo**. Es el filtro principal para los alimentos de la tienda ([[Criterios de la tienda]]).

## El filtro

```
ALIMENTO
  1. Densidad          ¿cuánto nutriente hay por porción?
  2. Digestibilidad    ¿cuánto puede liberar el sistema digestivo?
  3. Biodisponibilidad ¿qué proporción queda disponible para absorberse?
  4. Utilización       ¿el organismo lo puede usar en esa forma?
  5. Contexto          ¿esta persona lo necesita? ¿es su factor limitante?
  → VALOR NUTRICIONAL EFECTIVO
```

Absorción, distribución y función forman parte de *biodisponibilidad* y *utilización*. No se puntúan por separado porque casi nunca hay datos independientes para cada una.

**El contexto pertenece a la persona, no al alimento.** La matriz evalúa los alimentos frente a un adulto de referencia; el contexto (edad, sexo, embarazo, deporte, patologías, dieta completa) es una capa posterior.

## Precisión clave: la biodisponibilidad es por nutriente, no por alimento

La espinaca tiene vitamina K y folato que se aprovechan bien, pero su calcio y su hierro se absorben poco por los oxalatos. Ponerle "★★★" a la espinaca esconde esa diferencia. Por eso:

- En cada nota de alimento, la biodisponibilidad se registra **nutriente por nutriente** en la tabla de composición.
- La propiedad `biodisponibilidad` del alimento es solo un **resumen de sus nutrientes clave**.

## Rúbrica (1–5)

Las puntuaciones son una visualización de una evaluación documentada, no una verdad absoluta. Cada puntuación tiene que poder justificarse con la tabla de la nota y sus fuentes.

| Puntaje | Densidad (por porción habitual) | Digestibilidad | Biodisponibilidad (nutrientes clave) | Utilización |
|---|---|---|---|---|
| **5** | ≥5 nutrientes objetivo con ≥20 % de la referencia | Alta y documentada (proteína: DIAAS ≥100) | Formas de alta absorción (hierro hemo, B12 de origen animal, retinol) | Forma activa, se usa directamente (retinol, EPA/DHA) |
| **4** | 3–4 nutrientes con ≥20 % | Alta con preparación habitual | Mayormente alta, con alguna excepción | Mayormente directa |
| **3** | 1–2 nutrientes con ≥20 %, o ≥5 con ≥10 % | Depende de la preparación (cocción, remojo, fermentado) | Variable según matriz, potenciadores e inhibidores | Requiere conversión con eficiencia variable (betacaroteno → vitamina A) |
| **2** | Algún nutriente con ≥10 % | Limitada | Baja salvo con preparación específica | Conversión baja (ALA → EPA/DHA) |
| **1** | Ningún nutriente con ≥10 % | Baja | Muy limitada por inhibidores (fitatos, oxalatos) | Muy limitada |

Referencia de cantidades: ingestas recomendadas para adultos (NIH ODS u organismo equivalente), indicando cuál se usa en cada nutriente. Datos de composición: [[USDA - FoodData Central]] o la tabla nacional de composición de alimentos. Calidad proteica: [[FAO - Calidad proteica DIAAS (2013)]].

## Estados de cobertura (por nutriente)

Se calculan sobre el **núcleo**: los alimentos con `en_nucleo: true`.

- 🟢 `cubierto`: varios alimentos del núcleo lo aportan con buena biodisponibilidad.
- 🟡 `parcial`: hay fuentes, pero depende de cantidades.
- 🔴 `hueco`: el núcleo no lo cubre adecuadamente.
- ⚠️ `contexto`: depende de preparación, dieta completa o necesidades individuales.

## La pregunta central del núcleo

> ¿Qué combinación de alimentos ofrece la mayor densidad, diversidad y biodisponibilidad con la **menor cantidad de alimentos** necesaria para cubrir las necesidades humanas?

Formalmente es un problema de optimización conocido (el "problema de la dieta", que se resuelve con programación lineal). Cuando cada alimento del núcleo tenga cantidades por porción cargadas, se puede calcular. Hasta entonces, el sistema trabaja con los estados de cobertura.

## Alimentos evaluados

```base
filters:
  and:
    - 'tipo == "alimento"'
    - not:
        - file.inFolder("90 Plantillas")
formulas:
  puntaje: '((densidad + digestibilidad + biodisponibilidad + utilizacion) / 4).toFixed(1)'
views:
  - type: table
    name: Alimentos
    order:
      - file.name
      - grupo
      - en_nucleo
      - densidad
      - digestibilidad
      - biodisponibilidad
      - utilizacion
      - formula.puntaje
      - nutrientes_clave
```

## Cobertura del núcleo por nutriente

```base
filters:
  and:
    - 'tipo == "nutriente"'
    - not:
        - file.inFolder("90 Plantillas")
views:
  - type: table
    name: Cobertura
    groupBy:
      property: estado_cobertura
      direction: ASC
    order:
      - file.name
      - clase
      - ingesta_referencia
      - unidad
```

Volver a [[Inicio]].
