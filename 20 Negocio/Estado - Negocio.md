---
tipo: estado
area: negocio
fecha_revision: 2026-10-03
---

# Estado - Negocio

> Nota corta que Claude lee al empezar cada sesión de esta área. Se actualiza con `/cerrar-sesion`.

## Dónde estamos
- Visión con 4 sistemas y orden de construcción: [[Visión y objetivos]]. Modelo: [[Modelo de negocio]].
- Riesgos legales, de datos y de calidad mapeados: [[Riesgos y cumplimiento]]. Borrador de [[Claims permitidos]].
- Decisiones: [[Decisiones]] (hay **pendientes de Agus**).
- **Dirección creativa** (2026-10-06): [[Dirección creativa]] con 8 ángulos de venta, estructura de guion con 3 hooks, briefs de miniaturas, nombres y UTM, reglas de presupuesto y biblioteca de aprendizajes. Skill `/crear-campana`, plantilla Campaña.
- Documento de origen guardado en `20 Negocio/Documentos/`.
- **Contenido (2026-10-11):** sistema de contenido con IA instalado en `10 Contenido/Sistema de contenido/`. Ver [[Estado - Contenido]], [[Estrategia de contenido]] y [[Automatizaciones de contenido]].

- **Herramientas conectadas (2026-10-07):** Adspirer → cuenta publicitaria de Meta "Agustin Tomas Rodriguez" (plan gratis: 15 usos por mes; usar 1 por semana para el reporte y el resto para acciones, siempre con confirmación de Agus antes de gastar o publicar). Metricool → **conectado el 2026-10-11** (Instagram `agustin.nutricion.evolutiva` y TikTok `agustin.tomas.rod`); ver [[Automatizaciones de contenido]].
- **n8n (2026-10-07):** se monta ya en un VPS propio (sugerido: Hostinger KVM 1 con la plantilla de n8n, centro de datos en San Pablo). Clave SSH generada en la compu de Agus: `~/.ssh/n8n_servidor` (la pública se pega en el panel del VPS; la privada nunca sale de la compu). Pendiente: que Agus contrate el VPS y pase la IP. Primeros flujos previstos: reporte semanal de Instagram y anuncios, planilla de pedidos y caja, lead del test → WhatsApp, recordatorio de recompra.
- **Estrategia acordada (2026-10-07):** conocimiento → contenido orgánico (cada carrusel prueba un ángulo gratis) → producto (primera venta por WhatsApp e Instagram, aun sin web) → anuncios solo sobre ángulos ganadores y con producto y landing listos. Semana tipo: lunes conocimiento · martes contenido · miércoles producto · jueves BMAD con Avril · viernes métricas.

## Próximos pasos
1. Completar los huecos de [[Visión y objetivos]] (país: Uruguay, confirmado; web v1 con código propio, decidido; etapa 1 local en Maldonado y Punta del Este).
2. Conseguir validación profesional: regulatoria (claims, MSP) y nutricional (lógica del test).
3. Definir el surtido inicial y los proveedores.

## Huecos conocidos
*Auditoría 2026-10-06.*
- Público objetivo, objetivos a 3 y 12 meses, precios, márgenes, presupuesto y métricas de éxito (todo "a completar" en [[Visión y objetivos]]).
- [[Visión y objetivos]] no menciona la etapa 1 local (Maldonado y Punta del Este).
- Quién valida los claims (MSP) y la lógica del test (nutricionista): sin responsable en [[Riesgos y cumplimiento]].
- [[Claims permitidos]] sigue en borrador.
- Asesoría legal por la Ley 18.331 (datos de salud), necesaria antes de guardar respuestas del test.
- Surtido de lanzamiento y proveedores sin definir; hoy hay un solo producto (lentes, evidencia C, borrador).
- Decidido 2026-10-06: capa de órganos, clasificación única de objetivos, marco propio declarado y catálogo con alimentos del núcleo. Falta ejecutarlo. Sigue pendiente el alcance del primer test.

## Documentos
- [[Plan integral del sistema (original 2026-10-03)]]

## Última sesión
2026-10-03: área creada e integración del plan integral (4 sistemas, riesgos, claims, área Operación).
