---
tipo: negocio
area: contenido
estado: borrador
fecha_creacion: 2026-10-11
fecha_revision: 2026-10-11
relacionados:
  - "[[Estado - Contenido]]"
  - "[[Estrategia de contenido]]"
  - "[[Estado - Negocio]]"
---

# Automatizaciones de contenido

> Qué está **conectado y funcionando**, qué está **decidido y pendiente**, y qué es **propuesta**. No se da por hecho nada que no esté probado.

## Conectado hoy
| Herramienta | Estado | Qué hace en contenido |
|---|---|---|
| **Metricool** | Conectado el 2026-10-11 (brand `agustin.nutricion.evolutiva`, id 7297706; zona `America/Montevideo`). Redes: Instagram `agustin.nutricion.evolutiva`, TikTok `agustin.tomas.rod`. Facebook solo como cuenta de anuncios | Programar publicaciones, ver las ya programadas, mejor hora por red, analítica |
| **Adspirer** | Conectado (2026-10-07). Cuenta de Meta "Agustin Tomas Rodriguez"; plan gratis, 15 usos por mes | Reporte semanal y, más adelante, anuncios sobre ángulos ganadores. Siempre con confirmación de Agus antes de gastar |
| **Sistema de contenido IA** | Instalado (2026-10-11) | Investigar, planificar, producir (carrusel, reel, historias) y reportar |

## Decidido y pendiente
| Qué | Estado |
|---|---|
| **n8n en un VPS propio** (Hostinger KVM 1 sugerido, San Pablo) | Decidido 2026-10-07. Falta que Agus contrate el VPS y pase la IP. Flujos previstos: reporte semanal de Instagram y anuncios, planilla de pedidos y caja, lead del test → WhatsApp, recordatorio de recompra |
| **Número de WhatsApp Business** | Pendiente de Agus; sin él el CTA es DM con palabra clave |

## Comentario → WhatsApp (propuesta lista, sin activar)
Cuando alguien comenta una palabra clave (ej. "huevos"), ManyChat le manda un DM con un botón `wa.me` que abre WhatsApp con el pedido ya escrito. Configuración completa en [[Campaña - Huevos de campo (anuncio y automatización)]]. **Requiere:** cuenta de ManyChat conectada a Instagram (la crea Agus) y el número de WhatsApp. **Decisión de Agus (12/10/2026): hacerlo con n8n.** Flujo importable y guía en `10 Contenido/n8n/` ([[Automatización n8n - comentario a WhatsApp]]). Ojo: con n8n propio hace falta App Review de Meta para que le llegue el DM a cualquier persona; ManyChat ya lo tiene.

## El circuito de una pieza (con Metricool)
```
Banco de ideas → /plan-mensual-contenido → /carrusel · /editar-video · /historias
   → Publicar.md (pie, hashtags, portada) → Metricool "para revisión"
   → Agus aprueba en el chat → programada → publicada → /reporte-contenido
```
- **Nada se programa sin el OK de Agus**, por pieza. El mes 1 todo va "para revisión". Cada publicación sale a su nombre.
- La **hora** sale de `getBestTimeToPostByNetwork`; el **pie** pasa por `revisar-texto.py` y [[Claims permitidos]] antes de cargarse.
- **A probar en la primera pieza:** cómo se adjunta el archivo (PNG/MP4) a la publicación de Metricool. Hasta confirmarlo, el pie y la hora quedan cargados y Agus sube el archivo.

## Ciclo semanal propuesto
Encaja en la semana tipo acordada (lunes conocimiento · martes contenido · miércoles producto · jueves BMAD · viernes métricas):

| Día | Qué |
|---|---|
| Lunes | Leer métricas de Metricool, decidir qué repetir y qué dejar |
| Martes | `/plan-mensual-contenido` o ajustes; escribir piezas de la semana |
| Miércoles | Agus graba por lote (1 hora = 3 o 4 piezas); Claude edita |
| Jueves | Programar en Metricool para revisión; Agus aprueba |
| Viernes | `/reporte-contenido`; aprendizajes a la biblioteca |

## Automatizaciones propuestas (todavía no existen)
- **Reporte semanal automático** de Metricool (+ Adspirer) a n8n → resumen en el vault.
- **Palabra clave → WhatsApp:** cuando alguien escribe "TEST", respuesta con el link del test (necesita WhatsApp Business).
- **Aprendizajes automáticos:** el reporte mensual actualiza *Aprendizajes* de [[Dirección creativa]].
- **Recordatorio de recompra** (ya previsto en n8n).
