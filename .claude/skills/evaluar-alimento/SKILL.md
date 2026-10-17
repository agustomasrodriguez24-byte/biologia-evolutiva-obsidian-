---
name: evaluar-alimento
description: Evalúa un alimento con la Matriz de Cobertura Nutricional de Nutrición Evolutiva (densidad, digestibilidad, biodisponibilidad por nutriente, utilización) y actualiza la cobertura del núcleo. Usar cuando el usuario quiere analizar un alimento, cargar su surtido o "analizar el núcleo".
---

# Evaluar un alimento

Leé `00 Sistema/Matriz de Cobertura Nutricional.md` (rúbrica 1–5) y usá `90 Plantillas/Alimento.md`. Ejemplo: `14 Alimentos/Huevo.md`.

1. **Buscá antes de crear** en `14 Alimentos/`.
2. **Composición por porción habitual**: tomá las cantidades de USDA FoodData Central (anotá el FDC ID) o de la tabla nacional. Si no podés verificar un valor, marcalo como aproximado y dejá la nota en `estado: borrador`. Nunca presentes un valor de memoria como verificado.
3. Calculá el **% de la referencia adulta** de cada nutriente, con la referencia del NIH ODS (anotá cuál usaste).
4. **Biodisponibilidad nutriente por nutriente**: potenciadores, inhibidores (fitatos, oxalatos) y forma química (hierro hemo o no hemo, retinol o betacaroteno, EPA/DHA o ALA).
5. Asigná los cuatro puntajes con la rúbrica y **justificá cada uno** en la nota.
6. Enlazá cada nutriente clave a su nota en `15 Nutrientes/`; si no existe, creala con `90 Plantillas/Nutriente.md`.
7. Preparación recomendada para maximizar el valor efectivo, antinutrientes y para quién no es.

## Analizar el núcleo
Cuando Agus pida analizar el núcleo (alimentos con `en_nucleo: true`):
1. Para cada nutriente de `15 Nutrientes/`, calculá su cobertura a partir de esos alimentos y poné `estado_cobertura`: `cubierto` / `parcial` / `hueco` / `contexto`.
2. Reportá una tabla de huecos y qué alimentos los cubrirían mejor con la menor cantidad de alimentos agregados.
