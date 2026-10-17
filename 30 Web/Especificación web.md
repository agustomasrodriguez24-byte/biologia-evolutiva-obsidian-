---
tipo: web
fecha_revision: 2026-10-06
---

# Especificación web

Qué tiene que hacer la web, sin entrar en cómo se programa. Cada ítem lleva la versión en la que entra y se marca cuando está construido. Origen: conversación inicial + [[Plan integral del sistema (original 2026-10-03)]].

## 1. Lo que ve el cliente
- [ ] **v1 · Landing** con video de inicio y secciones informativas (estructura del prototipo v0.3).
- [ ] **v1 · Catálogo** filtrable por necesidad.
- [ ] **v1 · Landing por producto**: es el destino de los anuncios de ese producto. Incluye necesidad, cadena de alineación, nivel de evidencia de la promesa, ficha de valor, origen y trazabilidad, preguntas frecuentes, para quién no es y botón de WhatsApp (fijo en el celular). El titular cambia según el ángulo del anuncio (`?angulo=`). Detalle: [[Brief para desarrollo]] §6.
- [ ] **v1 · Cómo elegimos** (`/como-elegimos`): criterios de la tienda y niveles de evidencia, para generar confianza.
- [ ] **v1 · Páginas legales**: privacidad, términos y aviso de salud.
- [ ] **v1 · Test gratuito**: entrega información útil según las respuestas. Al final pide WhatsApp o email (con consentimiento) a cambio del resultado.
- [ ] **v1 · Botón o chat de WhatsApp** (venta sin carrito).
- [ ] **v2 · Carrito y pagos.**
- [ ] **v2 · Blog** generado desde el conocimiento, con fuentes.
- [ ] **v3 · Mapa del cuerpo** generado desde el vault.
- [ ] **v3 · Buscador por suscripción mensual**: Claude responde solo con notas publicadas, citando fuente y nivel.
- [ ] **v3 · Cuenta del cliente**: compras, suscripción y resultados del test.

## 2. Panel de administración (con inicio de sesión)
- [ ] **v1 · Productos**: precio, stock y visibilidad. Los textos de salud **no** se editan desde el panel: salen de `08 Productos/` (fuente única), porque ahí pasan el control de claims.
- [ ] **v1 · Stock.**
- [ ] **v1 · Pedidos de WhatsApp**: carga manual de cada venta con su `ref_anuncio`, para medir qué anuncio vende.
- [ ] **v1 · Respuestas de los tests.**
- [ ] **v2 · Blog**: alta fácil.
- [ ] **v2 · Pedidos y logística**: ver [[Logística]].
- [ ] **v3 · Suscriptores.**

## 3. Datos y analítica
- [ ] **v1 · Base de datos** con las respuestas de los tests y los contactos (con consentimiento).
- [ ] **v1 · Medición**: UTMs, píxel de Meta y embudo (visita → test → contacto → compra).
- [ ] **v2 · Analítica de tests**: patrones y segmentos.
- [ ] **v2 · Vista individual** de cada persona y su información.
- [ ] **v3 · Perfil de cliente completo** y CRM (ver [[Ventas y clientes]]).
- [ ] **v3 · Búsquedas sin respuesta** → vuelven al vault como preguntas abiertas.

## 4. Conexión con el vault
- Solo se publican notas con `estado: activo`.
- Un proceso de publicación lee el vault y genera los datos del mapa, el catálogo con sus fichas y el índice de búsqueda. Ver [[Arquitectura del flujo]].
- El vault se respalda y versiona en GitHub (repositorio privado).

## 5. Requisitos generales
- Disclaimers y textos revisados contra [[Claims permitidos]].
- Consentimiento, política de privacidad y almacenamiento de datos según la Ley 18.331 (ver [[Riesgos y cumplimiento]]).
- Adaptada a celular.
