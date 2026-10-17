---
tipo: web
fecha_revision: 2026-10-03
---

# Hoja de ruta web

La web avanza por versiones. Cada versión tiene un objetivo, un alcance cerrado y un registro de lo que cambió. Alineada con el orden de construcción de [[Visión y objetivos]].

## Versiones

| Versión | Objetivo | Alcance | Estado |
|---|---|---|---|
| v0.1–v0.3 | Definir la estructura | Prototipos navegables (`30 Web/Prototipos/`) | Hecho |
| **v1** | Validar y captar | Landing con video, catálogo, fichas de producto, test con captura de contacto, WhatsApp, admin de productos, stock y respuestas, medición (UTMs, píxel) | Próxima |
| v2 | Vender dentro de la web | Carrito y pagos, logística básica, blog, analítica de tests | Planificada |
| v3 | Sistema vivo | Mapa desde el vault, buscador por suscripción, cuentas, CRM y campañas por segmento | Planificada |

Detalle de cada ítem: [[Especificación web]].

## Camino técnico
**Decidido (2026-10-03): código propio, desarrollado con Claude Code.** Se descarta la plataforma armada (Tiendanube o Shopify). La etapa 1 es local (Maldonado y Punta del Este) y no lleva pasarela de pago: el botón de compra deriva a WhatsApp, donde el pago se acuerda en forma personal. Ver [[Decisiones]].

**Stack (decidido 2026-10-04):** Next.js en Vercel + Supabase (productos, stock, respuestas del test, panel de administración) + enlaces a WhatsApp. El test se programa dentro de la web. El código vive fuera del vault, en `Downloads/nutricion evolutiva/web`. La pasarela de pagos queda para la v2.

## Registro de versiones
- **v0.3** (2026-10-03): estructura tipo Promix con colores profundos; menú por necesidad; franja de fuentes; tarjetas con sello de evidencia.
- **v0.2** (2026-10-03): elementos de Mill (menú flotante, objetivos, pasos) y de Promix (cinta, tarjetas con beneficio).
- **v0.1** (2026-10-03): primer prototipo con mapa del cuerpo, buscador y catálogo.
