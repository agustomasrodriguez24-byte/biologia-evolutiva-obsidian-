---
tipo: estado
area: conocimiento
fecha_revision: 2026-10-03
---

# Estado - Conocimiento

> Nota corta que Claude lee al empezar cada sesión de esta área. Se actualiza con `/cerrar-sesion`.

## Dónde estamos
- Arquitectura armada: 10 pilares, 14 tipos de nota con plantillas, paneles (Mapa general, Auditoría, Bandeja, Tienda, Cobertura).
- Capas: escala de evidencia A–F, [[Flujo de ingreso]], [[Criterios de la tienda]], [[Matriz de Cobertura Nutricional]].
- Notas de ejemplo: cadena de luz y ritmo circadiano ([[Ritmo circadiano]] → [[Protocolo - Luz matutina]]), [[Sodio]], [[Huevo]], [[Colina]], [[Lentes con filtro de luz azul]].
- 8 fuentes institucionales cargadas (OMS ×2, NIH ODS, NCCIH ×2, Cochrane, USDA, FAO).

- **Información madre (2026-10-07):** cerebro maestro creado ([[Información madre]] + `17 Información madre/`). 12 tesis armadas con 19 videos de referentes y *Hábitos atómicos*. Las 20 entradas de la bandeja quedan en `pendiente`: ya alimentaron las tesis, pero falta llevarlas a las notas del sistema (órganos, nutrientes, mecanismos y la nota de Hidratación) con `/procesar-bandeja`. Cola: [[Cola de la Información madre]].

- **Sistema de salud (2026-10-07, noche):** canales completos de Nutrillermo y Academia Unani procesados → [[Referente - Nutrillermo]], [[Marco Unani]] y el entregable central **[[Sistema de salud Nutrición Evolutiva]]** (paso a paso de 18 semanas, test de 4 bloques, seguridad, escalera de negocio). 11 tesis actualizadas. Todo en `borrador`, esperando la revisión de Agus.

## Próximos pasos
> Se trabaja con el [[Método de trabajo]]: un órgano por semana, de punta a punta. Hoy estamos en la **Fase 0 (cimientos)**: la plantilla de órgano ya está; sigue el marco de ChatGPT y después el primer órgano (ojos y cerebro).

0. **Archivo de oro de Instagram** (chat de @agustin.nutricion.evolutiva con @nutricionancestral.uy): hay una muestra en la bandeja (2026-10-07). Para procesarlo completo, Agus exporta sus mensajes de Instagram en JSON y deja el ZIP en Descargas; se procesa **solo ese chat** (y el grupo con eselmomento13 si Agus lo pide), no el resto de sus conversaciones.
1. Pasar la información de ChatGPT al vault con `/procesar-bandeja`. Conviene exportar las conversaciones (ChatGPT → Configuración → Controles de datos → Exportar).
2. Cargar el surtido de alimentos del núcleo y evaluarlos con `/evaluar-alimento`.
3. Verificar los valores del [[Huevo]] en FoodData Central.
4. Cargar fuentes de la cadena circadiana (hoy figuran como pendientes).
5. Agregar la propiedad `zona` (órgano o zona del cuerpo) para alimentar el mapa de la web.

## Huecos conocidos
*Auditoría 2026-10-06.*
- **Capa de órganos:** la plantilla, las reglas y la carpeta `16 Órganos/` ya están; faltan las notas de cada órgano.
- **El marco de Agus:** la estructura está en [[Modelo Nutrición Evolutiva]] (borrador); falta integrar el contenido de ChatGPT.
- **Requerimientos casi vacíos**: 1 nutriente ([[Colina]]) y 1 alimento ([[Huevo]], `en_nucleo: false`). El núcleo tiene 0 alimentos y la [[Matriz de Cobertura Nutricional]] no puede calcular nada.
- **Casi nada publicable**: la única nota de conocimiento `activo` es [[Sodio]] (sin contar las fuentes). La cadena circadiana está en borrador o `revisar`.
- **Fuentes vacías** en [[Ritmo circadiano]], [[Señalización lumínica circadiana]] (ambas nivel A sin fuente), [[Exposición lumínica matutina]], [[Protocolo - Luz matutina]] y [[Regularidad del sueño]].
- [[Regularidad del sueño]] no tiene `nivel_evidencia`.
- Fuentes sin uso: [[NCCIH - Revisiones de evidencia]] y [[NCCIH - Uso seguro de productos y prácticas complementarias]].
- **La información de ChatGPT (el marco de Agus) todavía no entró al vault**: la bandeja está vacía.
- Pilares sin notas propias: P05 Movimiento (solo la fuente OMS), P06 Mente, P08 Digestiva, P10 Propósito.
- Los paneles Bases todavía no se probaron dentro de Obsidian.

## Última sesión
2026-10-03: creación del sistema completo y reorganización por áreas.
