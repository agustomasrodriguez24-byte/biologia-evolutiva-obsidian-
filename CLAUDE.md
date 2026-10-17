---
tipo: sistema
fecha_revision: 2026-10-03
---

# Nutrición Evolutiva: cerebro del proyecto

Este vault de Obsidian es la memoria compartida entre Agus y Claude. Todo lo que hace falta para retomar cualquier trabajo está acá: no hay que repetir contexto en el chat.

## El negocio en 5 líneas

**Nutrición Evolutiva** es un sistema de salud basado en la biología humana y la evidencia, con una tienda de alimentos y herramientas filtrados por ese conocimiento. Opera en Uruguay, con reparto propio. Son cuatro sistemas conectados:
1. **Gestión de documentos** (este vault): conocimiento con fuente y nivel de evidencia (A–F) + documentos de negocio. Alimenta todo el contenido.
2. **Web**: landing, catálogo, fichas de producto, test con captura de contacto, panel de administración. Más adelante: mapa del cuerpo, blog y buscador por suscripción.
3. **Datos y analítica**: respuestas de tests, perfiles, embudo.
4. **Ventas y clientes**: WhatsApp (V1), carrito y pagos (V2), CRM (V3), logística de reparto.

Flujo: bandeja → conocimiento → contenido → web → test → datos → perfil → venta → recompra. Detalle: [[Visión y objetivos]].

## Áreas: dónde está cada cosa

| Área | Carpetas | Estado actual (leer al empezar) |
|---|---|---|
| **Conocimiento** | `00 Sistema/` reglas · `01`–`16` notas por tipo · `17 Información madre/` (tesis por tema) · `90 Plantillas/` · `95 Paneles/` | [[Estado - Conocimiento]] |
| **Negocio** | `20 Negocio/`: visión, modelo, decisiones, riesgos, claims permitidos, `Documentos/` | [[Estado - Negocio]] |
| **Web** | `30 Web/`: especificación, hoja de ruta, arquitectura, referencias, prototipos (el código va en otra carpeta) | [[Estado - Web]] |
| **Operación** | `40 Operación/`: ventas, clientes, logística | [[Estado - Operación]] |
| **Contenido** | `10 Contenido/`: estrategia, automatizaciones y el **sistema de contenido con IA** (`Sistema de contenido/`, con sus propias skills: abrir Claude en esa carpeta) | [[Estado - Contenido]] |
| **Archivo** | `99 Archivo/`: bandeja ya procesada y material viejo | n/a |

## Cómo trabajamos

Método completo: [[Método de trabajo]] (un órgano por semana, de punta a punta). Filosofía y principios: [[Modelo Nutrición Evolutiva]].

1. **Una sesión de chat por tarea.** No hace falta seguir siempre en el mismo chat.
2. **Al empezar**: identificá el área de la tarea y leé su nota de **Estado** (es corta). Leé otras notas solo si la tarea las necesita. Si el área no está clara, preguntá.
3. **Durante**: guardá en el vault todo lo que sirva a futuro (decisiones, documentos, notas). El chat se pierde; el vault no.
4. **Al terminar**: usá `/cerrar-sesion` para actualizar el Estado del área, registrar decisiones y anotar los pendientes.

## Skills (se cargan solo cuando se usan)

| Skill | Para qué |
|---|---|
| `/retomar <área>` | Arrancar una sesión: lee el estado del área y propone por dónde seguir |
| `/procesar-bandeja` | Integrar información nueva (texto, links, documentos, ChatGPT) en su lugar preciso, como borrador pendiente de revisión |
| `/importar-instagram` | Pasar al vault el "archivo de oro" de Instagram (chat con @nutricionancestral.uy) desde la exportación de mensajes; solo ese chat ([[Importar desde Instagram]]) |
| `/generar-contenido` | Blogs, anuncios, fichas con preguntas frecuentes, guiones y mensajes, solo desde el vault |
| `/crear-campana` | Dirección creativa: ángulos de venta, guiones con hooks, miniaturas, nombres y UTM; análisis de resultados de anuncios ([[Dirección creativa]]) |
| `/sincronizar-repo` | Subir al repo de GitHub de la web los cambios de las notas que tienen copia en `docs/`, con las reglas de git del repo |
| `/revisar-cumplimiento` | Revisar un texto contra los claims permitidos antes de publicarlo |
| `/evaluar-producto` | Pasar un producto por los criterios de la tienda y escribir su ficha de valor |
| `/evaluar-alimento` | Evaluar un alimento con la Matriz de Cobertura Nutricional |
| `/auditar` | Detectar huecos: notas sin fuente, evidencia débil, áreas vacías, pendientes de negocio y web |
| `/cerrar-sesion` | Dejar todo listo para la próxima sesión |

## Reglas que valen siempre

- **La verdad del sistema (decisión de Agus, 2026-10-08):** el sistema Nutrición Evolutiva se escribe **desde la verdad de Agus y de sus referentes** (Duarte y Academia Unani, Nutrillermo, Sanagustín, Juan Bola y los demás) y desde su experiencia con su propio cuerpo. En los textos del sistema (hilo de la vida, 18 semanas, mapas, contenido) **no se ponen choques con la evidencia, niveles A–F ni tablas de "esto no se comunica"**. Lo legal de lo que se publica vive aparte, en [[Claims permitidos]]. Única excepción de cuidado: no indicar dejar o cambiar medicación por cuenta propia.
- **Información madre**: todo lo que Agus pasa (videos, libros, posts, ideas, referentes) alimenta [[Información madre]], el cerebro maestro del sistema. Lo que Agus cree se registra sin censura y con su nivel; lo que se comunica lo decide la postura de cada tesis y [[Claims permitidos]].
- **Evidencia**: la escala A–F ([[Niveles de evidencia]]) queda como herramienta de consulta interna; no se usa para contradecir a los referentes en los textos del sistema.
- **No inventar fuentes, datos ni citas.** Si falta una fuente, se marca como pendiente.
- **El producto se subordina al conocimiento.** Todo texto comercial o de salud pasa por `/revisar-cumplimiento` ([[Claims permitidos]]).
- **Borrador → activo**: lo que entra por la bandeja queda en borrador hasta que Agus lo revisa. Solo lo `activo` se publica.
- **Fuente única de productos**: las notas de `08 Productos/` alimentan la web, los anuncios y WhatsApp.
- **Buscar antes de crear**: no duplicar notas.
- **No borrar**: marcar `estado: obsoleto` y enlazar la nota que la reemplaza.
- Las decisiones son de Agus. Claude recomienda con argumentos.
- Idioma: español rioplatense, claro y directo.

## Convenciones del conocimiento

- Cada tipo de nota tiene su carpeta y su plantilla: concepto `02` · mecanismo `03` · fuente `04` · intervención `05` · protocolo `06` · métrica `07` · producto `08` · experimento `09` · contenido `10` · hipótesis `11` · pregunta `12` · entrada `13` · alimento `14` · nutriente `15` · órgano `16` (eje del mapa del cuerpo) · tesis `17` (Información madre: síntesis por tema de referentes + evidencia) · mapa `19` ([[La mente de los maestros]]: la voz de los referentes sin filtro) · hábito `18` (una semana del [[Sistema de salud Nutrición Evolutiva]]: la unidad que alimenta web, test, contenido y productos). Qué lleva cada uno: [[Reglas por tipo]]. Propiedades: [[Guía de propiedades]].
- Pilares (`pilar`, lista): `biologia` `nutricion` `hidratacion` `cronobiologia` `movimiento` `mente` `metabolica` `digestiva` `entorno` `proposito`.
- Nombres en español y singular, sin prefijo de tipo. Excepciones: fuentes (`OMS - Alimentación saludable`) y protocolos (`Protocolo - Luz matutina`).
- Fechas `YYYY-MM-DD`. Enlaces `[[ ]]`, también dentro de propiedades (`"[[Nota]]"`).
