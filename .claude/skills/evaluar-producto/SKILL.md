---
name: evaluar-producto
description: Pasa un producto (alimento o herramienta) por los criterios de la tienda Nutrición Evolutiva, ajusta la promesa a la evidencia y escribe su ficha de valor. Usar cuando el usuario quiere sumar, revisar o vender un producto.
---

# Evaluar un producto

Leé `00 Sistema/Criterios de la tienda.md` y usá la plantilla `90 Plantillas/Producto.md`. Ejemplo terminado: `08 Productos/Lentes con filtro de luz azul.md`.

1. **Buscá antes de crear** en `08 Productos/`.
2. **Necesidad primero**: ¿qué necesidad del cuerpo cubre? Buscá el concepto o protocolo en el vault. Si no existe, la cadena está cortada: avisá y proponé crear primero el conocimiento.
3. **Si es alimento**: tiene que tener su nota en `14 Alimentos/` evaluada con `/evaluar-alimento`. Umbral para entrar: densidad ≥4 y ningún otro puntaje <3, salvo que cubra un hueco del núcleo.
4. **Evidencia por capa**: ingrediente o mecanismo / formulación / producto específico / afirmaciones del fabricante (F). Buscá evidencia real del producto o la categoría (Cochrane, PubMed, NIH ODS, NCCIH). Citá la fuente y creá su nota en `04 Fuentes/`.
5. **Promesa**: `nivel_promesa` = la evidencia del producto específico. Completá la tabla "Qué podemos decir y qué no".
6. **Ficha de valor** en lenguaje simple: para qué te sirve / cómo encaja en tu biología / cómo usarlo / qué podés esperar y qué no / para quién no es.
7. **Recomendación**: `aprobado`, `aprobado-con-condiciones` (decí cuáles) o `rechazado` (con el motivo). Dejá `estado_tienda: evaluando` y la decisión en manos de Agus; cuando decida, registrala en `20 Negocio/Decisiones.md`.
8. Proponé el guion del video de regalo como nota en `10 Contenido/` si Agus lo pide.
