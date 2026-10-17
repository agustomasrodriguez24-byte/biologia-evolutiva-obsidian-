---
tipo: operacion
fecha_revision: 2026-10-03
---

# Logística

Módulo del panel de administración, sobre el carrito de la V2. Origen: [[Plan integral del sistema (original 2026-10-03)]].

## Arranque simple (antes del módulo)
Exportar los pedidos del martes ordenados por zona y franja horaria, y pegar las direcciones en Google Maps. La optimización automática de rutas se suma solo cuando el volumen lo justifique.

## Funciones del módulo
- **Vista por día de reparto**: martes (ruta regular) y días especiales por separado.
- **Pedidos agrupados por zona y franja horaria**, con hoja de ruta para el repartidor (imprimible o por WhatsApp).
- **Lista de preparación**: total de unidades por producto para armar ese día.
- **Estados del pedido**: recibido → pagado → preparado → en ruta → entregado / no entregado. Con pago contra entrega, estado **cobrado** para cuadrar la caja.

## A definir
| Tema | Pregunta | Respuesta |
|---|---|---|
| Corte de pedidos | ¿Hasta cuándo se pide para el martes? (ej.: domingo 20:00). La web calcula sola la fecha de entrega | *pendiente* |
| Cupos | ¿Cuántos pedidos por zona y franja? | *pendiente* |
| Cobertura | Zonas o barrios, costo de envío por zona, mínimo para envío gratis | *pendiente* |
| Repartidores | ¿Cuántos? | *pendiente* |
| Pedidos especiales | Recargo, hora límite, stock y repartidor disponible | *pendiente* |
| Stock | Reservar al pedir, descontar al entregar, controlar vencimientos en frescos | *pendiente* |
| Frescos | ¿Qué productos requieren frío o control de vencimiento? | *pendiente* |
| Dirección | Pin en el mapa, instrucciones, teléfono, quién recibe | *pendiente* |
| Entrega fallida | ¿Reintento, reprogramación o nuevo cobro? | *pendiente* |
| Mensajes automáticos | Confirmación, "salimos en ruta", ventana estimada | *pendiente* |

## Skill prevista
**Hoja de ruta y preparación**: a partir de los pedidos del día, genera el listado por zona y franja y el total de unidades a preparar.
