---
tipo: sistema
fecha_revision: 2026-10-03
---

# Niveles de evidencia

Toda afirmación importante lleva un nivel. Se registra en la propiedad `nivel_evidencia` de la nota y, si una nota mezcla afirmaciones de distinto peso, se marca en línea: `(A)`, `(C)`, `(E)`.

| Nivel | Nombre | Qué incluye | Cómo se puede comunicar |
|---|---|---|---|
| **A** | Evidencia fuerte | Revisiones sistemáticas, metaanálisis, ensayos clínicos relevantes, guías oficiales | "La evidencia muestra…" |
| **B** | Evidencia moderada | Estudios observacionales, ensayos pequeños, mecanismos consistentes | "Los estudios sugieren…" |
| **C** | Evidencia preliminar | Estudios pequeños, en animales, mecanismos plausibles, evidencia indirecta | "Hay datos preliminares…" |
| **D** | Hipótesis | Propuesta teórica, modelo no validado | "Una hipótesis propone…" |
| **E** | Tradición / experiencia | Medicina tradicional, práctica ancestral, experiencia personal, testimonio | "En la tradición X…", "En mi experiencia…" |
| **F** | Comercial | Afirmación de un fabricante o vendedor | "El fabricante afirma…" |

## Reglas

- D, E y F **nunca** se presentan como evidencia clínica.
- Una fuente F nunca es la única evidencia de una afirmación sanitaria.
- El nivel lo da **la mejor evidencia disponible para esa afirmación concreta**, no la reputación del autor. Una guía oficial (A) puede contener recomendaciones puntuales basadas en evidencia débil: en ese caso se baja el nivel de esa afirmación.
- Evidencia sobre un mecanismo ≠ evidencia de que una intervención funciona en personas. Un mecanismo plausible (C) no convierte un protocolo en A.
- Cuando hay contradicción, se documenta en `## Debate / evidencia contradictoria` y se marca **CONFLICTO DE EVIDENCIA**.

## Separación de capas

Distinguí siempre: **hecho documentado · interpretación · hipótesis · experiencia · tradición · opinión · afirmación comercial**.

Ejemplos de dónde va cada cosa:

- Una guía de la OMS → `04 Fuentes/`, nivel A.
- Un modelo de la tradición Unani → `11 Hipótesis/`, nivel E (o D si propone un mecanismo verificable).
- Lo que observaste en vos durante 4 semanas → `09 Experimentos/`, nivel E.
- La etiqueta de un suplemento → `04 Fuentes/` con `tipo_fuente: comercial`, nivel F.

Volver a [[Inicio]].
