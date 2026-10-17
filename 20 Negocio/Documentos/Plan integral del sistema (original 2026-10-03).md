# Plan integral del sistema: Nutrición Evolutiva

Documento que ordena todas las ideas: sistemas, módulos, riesgos, orden de construcción y skills/automatizaciones.

---

## 1. Visión general

Cuatro sistemas conectados, alimentados por una misma base de conocimiento:

| # | Sistema | Función |
|---|---------|---------|
| 1 | Gestión de documentos personal | Base de conocimiento y de negocio; alimenta todo el contenido |
| 2 | Página web | Cara pública (cliente) y panel de administración |
| 3 | Datos y analítica | Base de datos de tests, perfiles y análisis |
| 4 | Ventas y clientes | WhatsApp, carrito/pagos, CRM, embudo, logística |

Flujo central: **Inbox → Conocimiento → contenido (blogs, anuncios, fichas) → web → test → datos → perfil de cliente → ventas → recompra.**

---

## 2. Sistema 1: Gestión de documentos personal

### Estructura de carpetas
- **Conocimiento:** salud, biología, alimentación y temas afines.
- **Negocio:** estrategia, áreas de la empresa, procesos y documentos de negocio.
- **Inbox:** punto de entrada de links y documentos.

### Automatización del Inbox
1. Se ingresa un link o documento.
2. Una automatización lo procesa: resumen, fuente, fecha, nivel de evidencia.
3. Lo guarda en la carpeta correcta de *Conocimiento*, con estado **"pendiente de revisión"**.

### Uso posterior
Esta base es la fuente única desde la que Claude genera blogs, anuncios, fichas de producto y cualquier otro contenido.

---

## 3. Sistema 2: Página web

### 3.1 Versión cliente
- **Landing** con video de inicio y secciones informativas.
- **Catálogo de productos.**
- **Test / cuestionario gratuito:** entrega información útil según parámetros.
- **Ficha por producto:** es el destino de los anuncios de un producto específico.
- **Captura de contacto** (WhatsApp o email) al final del test, a cambio del resultado.

### 3.2 Versión administrador (con inicio de sesión)
- Gestión de **stock**.
- Gestión de **productos** (descripción, alta de productos nuevos de forma simple).
- Alta de **blogs** fácilmente.
- Visualización de **respuestas de los tests**.
- Módulo de **logística** (ver sección 6).

---

## 4. Sistema 3: Datos y analítica

- Base de datos con las respuestas de los tests.
- Analíticas a partir de las respuestas (patrones, segmentos).
- Vista individual de cada persona y su información.
- Idea futura: gestión avanzada de cada cliente que entra al embudo, con un **perfil bien armado** (dentro de la web o en un sistema aparte).

---

## 5. Sistema 4: Ventas y clientes

### Versiones
- **V1:** botón o chat de WhatsApp (sin carrito).
- **V2:** carrito + pasarela de pagos dentro del sistema, lo antes posible.
- **V3:** CRM conectado, embudo, campañas segmentadas por perfil, automatizaciones de WhatsApp, base de clientes actuales.

### Decisión sobre perfiles
Idealmente los datos del test quedan vinculados a un perfil de cliente desde el inicio, pero eso complica mucho la V1. Se deja para una versión próxima, tras validar. **Mitigación barata para la V1:** capturar WhatsApp o email al final del test, para no perder el lead ni los datos.

---

## 6. Módulo de logística (admin, sobre el carrito V2)

### Funciones
- **Vista por día de reparto:** martes (ruta regular) y días especiales por separado.
- **Pedidos agrupados por zona y franja horaria**, con hoja de ruta para el repartidor (imprimible o por WhatsApp).
- **Lista de preparación:** total de unidades por producto a armar ese día.
- **Estados del pedido:** recibido → pagado → preparado → en ruta → entregado / no entregado.

### A definir
- **Corte de pedidos** (ej.: domingo 20:00 para el martes); la web calcula sola la fecha de entrega.
- **Cupos por zona y franja.**
- **Zonas de cobertura**, costo de envío por zona y mínimo para envío gratis.
- **Pedidos especiales:** recargo, hora límite, condición de stock y repartidor disponible.
- **Stock:** reservar al pedir, descontar al entregar, controlar vencimientos en frescos.
- **Datos de dirección:** pin en mapa, instrucciones, teléfono, quién recibe.
- **Entrega fallida:** reintento, reprogramación o nuevo cobro.
- **Mensajes automáticos por WhatsApp:** confirmación, "salimos en ruta", ventana estimada.
- **Pago contra entrega:** estado "cobrado" para cuadrar caja.

### Arranque simple
Exportar los pedidos del martes ordenados por zona y franja y pegar las direcciones en Google Maps. Automatizar la optimización de ruta solo cuando el volumen lo justifique.

---

## 7. Puntos ciegos a resolver

### Legal y sanitario
- Las promesas de salud y el contenido generado pueden requerir cumplir normativa del MSP o regulador del país.
- Definir qué se puede decir y qué no, con disclaimers.

### Datos de salud (sensibles)
- Consentimiento explícito, política de privacidad y claridad sobre dónde se almacenan.
- En Uruguay aplica la Ley 18.331. Conviene diseñarlo desde el inicio.

### Calidad de la información
- La automatización Inbox → Conocimiento puede incorporar fuentes malas.
- Mantener estado "pendiente de revisión", y guardar fuente y nivel de evidencia de cada dato.

### Lógica del test
- Necesita un criterio de recomendación validado, idealmente por un nutricionista, no solo un formulario.

### Logística y operación
- Envíos, devoluciones, vencimientos y cadena de frío.

---

## 8. Optimizaciones recomendadas

- **Captura de contacto al final del test** (casi gratis y resuelve el perfil desde el inicio).
- **No construir todo a medida al principio.** Para validar rápido: Tiendanube o Shopify (carrito, stock, pagos, blog), Tally o Typeform (test), Airtable o Supabase (datos) y WhatsApp Business. Programar a medida solo los cuellos de botella.
- **Una sola fuente de verdad de productos** (nombre, descripción, claims) que alimente web, anuncios y WhatsApp.
- **Medición:** UTMs, píxel de Meta y embudo (visita → test → contacto → compra).
- **Retención:** email o WhatsApp de recompra y suscripciones.
- **Pasarela de pagos:** verificar cuál opera en el país (Mercado Pago, dLocal, etc.), porque condiciona la plataforma.

---

## 9. Orden de construcción sugerido

1. Base de conocimiento + reglas de contenido (legal y tono).
2. Web con catálogo + test + captura de contacto + WhatsApp.
3. Carrito y pagos.
4. Logística básica (exportación por zona y franja).
5. Analítica de tests.
6. CRM, automatizaciones y campañas por segmento.

---

## 10. Skills y automatizaciones

### Gestión de documentos (empezar acá)
1. **Procesador de Inbox:** resumen, fuente, fecha, nivel de evidencia; guarda en Conocimiento como "pendiente de revisión".
2. **Organizador de carpetas:** clasifica documentos sueltos y detecta duplicados.
3. **Resumen de negocio:** documento vivo de estrategia, áreas y procesos.

### Contenido (solo desde Conocimiento)
4. **Generador de blogs**, citando fuentes.
5. **Generador de anuncios** por producto y perfil.
6. **Ficha de producto:** descripción, beneficios y preguntas frecuentes.
7. **Revisor de cumplimiento:** valida textos contra la lista de claims permitidos.

### Web y datos
8. **Analista de tests:** patrones y segmentos.
9. **Perfil de cliente:** perfil legible por persona.

### Ventas y clientes
10. **Borradores de WhatsApp** por perfil y producto.
11. **Hoja de ruta y preparación:** listado por zona y franja y total de unidades del día.
12. **Campañas por segmento** (cuando exista CRM).

**Prioridad:** 1 → 7 → 4/5/6 → 8 → resto. El Procesador de Inbox es la base de todo; el Revisor de cumplimiento va temprano para evitar problemas legales.

---

## 11. Preguntas pendientes

- ¿Dónde se guardan los documentos (Drive, carpetas locales, Notion)?
- ¿Qué categorías de conocimiento se necesitan desde el inicio?
- ¿Cuántas zonas o barrios se cubrirán y con cuántos repartidores?
- ¿Qué pasarela de pagos se usará?
- ¿Quién valida el criterio del test (nutricionista)?
- ¿Qué productos son frescos y requieren control de vencimiento o frío?
