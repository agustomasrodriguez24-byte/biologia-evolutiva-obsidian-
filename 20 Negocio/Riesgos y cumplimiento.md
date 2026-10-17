---
tipo: negocio
fecha_revision: 2026-10-03
---

# Riesgos y cumplimiento

Puntos ciegos a resolver antes de vender. Origen: [[Plan integral del sistema (original 2026-10-03)]].

## 1. Legal y sanitario
- Las promesas de salud en alimentos y productos, y el contenido generado, pueden estar alcanzados por la normativa del Ministerio de Salud Pública (MSP) y la normativa bromatológica de Uruguay.
- **Qué hacer**: mantener una lista de [[Claims permitidos]], usar disclaimers y validar los textos con un profesional regulatorio antes de publicar. La skill `/revisar-cumplimiento` controla cada texto contra esa lista.

## 2. Datos de salud (sensibles)
- Las respuestas del test pueden ser datos de salud. En Uruguay aplica la **Ley 18.331 de Protección de Datos Personales**.
- **Qué hacer desde el diseño**: consentimiento explícito antes de guardar respuestas, política de privacidad clara, saber dónde se almacenan los datos (país y proveedor), pedir solo lo necesario y dar opción de borrar los datos.
- *Validar con un abogado los requisitos concretos (por ejemplo, registro de bases de datos).*

## 3. Calidad de la información
- La automatización bandeja → conocimiento puede incorporar fuentes malas.
- **Qué hacer**: todo lo que entra por la bandeja queda en `estado: borrador` (pendiente de revisión) con fuente y nivel de evidencia. Solo lo que Agus revisa pasa a `activo`, y solo lo `activo` se publica.

## 4. Lógica del test
- El test necesita un criterio de recomendación validado, idealmente por un nutricionista, no solo un formulario.
- **Qué hacer**: documentar la lógica (pregunta → interpretación → recomendación) en una nota y hacerla revisar. *Pendiente: ¿quién valida?*

## 5. Logística y operación
- Envíos, devoluciones, vencimientos y cadena de frío. Ver [[Logística]].

## Estado
| Riesgo | Responsable | Estado |
|---|---|---|
| Normativa de claims (MSP) | *a definir* | Pendiente |
| Ley 18.331 (datos) | *a definir* | Pendiente |
| Calidad de información | Sistema (estado borrador → activo) | Resuelto en el diseño |
| Validación del test | *nutricionista a definir* | Pendiente |
| Cadena de frío | *a definir* | Pendiente |
