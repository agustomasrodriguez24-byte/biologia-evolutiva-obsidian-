---
name: procesar-bandeja
description: Integra información nueva al conocimiento de Nutrición Evolutiva en su lugar preciso, con fuente y nivel de evidencia, y archiva lo procesado. Usar cuando el usuario pega información (de ChatGPT, un paper, un video, una idea), dice "procesá la bandeja" o deja archivos en 13 Bandeja de entrada.
---

# Procesar la bandeja

Reglas de fondo: `00 Sistema/Flujo de ingreso.md`, `00 Sistema/Niveles de evidencia.md` y `00 Sistema/Reglas por tipo.md`. Leelas la primera vez en la sesión.

## Entrada
- **Texto pegado en el chat**: primero guardalo como entrada en `13 Bandeja de entrada/` con la plantilla `90 Plantillas/Entrada.md` (`origen: chatgpt`, `conversacion` o el que corresponda). Así queda el original.
- **Archivos en la bandeja**: procesá las entradas con `estado: pendiente`, de la más vieja a la más nueva. Si son muchas, de a 5 por tanda, y preguntá si seguir.
- **Link**: abrilo y leelo (WebFetch). Guardá una entrada con `url`, resumen, fuente, autor, fecha de publicación y tipo de fuente. Si no se puede abrir, pedí el texto o el archivo.
- **Documento** (PDF, Word, Markdown): leelo y creá la entrada. Si es un documento de negocio o de la web y no de conocimiento, guardalo en `20 Negocio/Documentos/` o en `30 Web/` e integralo en las notas de esa área.
- **Exportación de ChatGPT** (`conversations.json`): listá las conversaciones por título, pedí a Agus que elija cuáles importar y creá una entrada por conversación.

- **Video de YouTube**: bajá la transcripción con `uvx --python 3.13 yt-dlp --skip-download --write-subs --write-auto-subs --sub-langs "es-orig,es,es-ES,es-419" --sub-format vtt` (uv en `C:\Users\Usuario\AppData\Local\Microsoft\WinGet\Packages\astral-sh.uv_Microsoft.Winget.Source_8wekyb3d8bbwe\`), convertila a texto con marcas de minuto y creá una entrada `AAAA-MM-DD Video - <referente> - <tema>.md` con las afirmaciones y su minuto. Audiolibros u obras con derechos de autor: no se transcriben; se resumen con palabras propias.

## Información madre (siempre)
Todo lo que Agus pasa **alimenta la [[Información madre]]** (`00 Sistema/Información madre.md` y `17 Información madre/`). Por cada entrada:
- Actualizá la **tesis** que corresponda (o creá una nueva con `90 Plantillas/Tesis.md`): sumá al referente, ubicá cada idea en *Coincide con la evidencia*, *En debate* o *La evidencia dice otra cosa*, y revisá la *Postura Nutrición Evolutiva*.
- Si es un referente nuevo, sumalo a la tabla de referentes de la nota central.
- Lo que Agus cree se registra **siempre, sin censura**, con su nivel. Lo que se comunica en público lo decide la postura de la marca y [[Claims permitidos]].

## Por cada entrada
1. Separá las **afirmaciones** (una por línea). El texto de ChatGPT no es una fuente: es una afirmación a verificar. Si no trae fuente verificable, la afirmación queda con nivel pendiente y se crea una pregunta abierta para buscarla. No asignes A ni B sin una fuente real.
2. **Buscá antes de crear**: grep en el vault por el concepto y sus sinónimos.
3. Ubicá el **lugar preciso**: pilar → subpilar → concepto → ¿propiedad, mecanismo, evidencia, intervención, protocolo, fuente, hipótesis?
4. Decidí: confirma / amplía / matiza / contradice / reemplaza / es nuevo. Actualizá la nota existente o creá una con la plantilla de su tipo. **Toda nota creada desde la bandeja queda en `estado: borrador` (pendiente de revisión).** Solo Agus la pasa a `activo`. Si actualizás una nota `activo` con información nueva sin revisar, marcá el agregado como *(pendiente de revisión)*.
5. Si contradice algo: sección `## Debate / evidencia contradictoria` + **CONFLICTO DE EVIDENCIA**.
6. Revisá si cambia algún protocolo, producto o contenido enlazado.
7. Lo que no se pueda resolver va a `12 Preguntas abiertas/`.
8. Las ideas de **negocio, web u operación** que aparezcan no van al conocimiento: guardalas en `20 Negocio/`, `30 Web/` o `40 Operación/` y anotalas en el Estado del área.

## Cierre
1. Completá la sección *Procesamiento* de la entrada, poné `estado: procesada` y **movela a `99 Archivo/Bandeja/`**. Si no aportó nada, usá `estado: descartada` y anotá el motivo.
2. Actualizá `fecha_revision` en cada nota tocada y agregá una línea en `00 Sistema/Registro de cambios.md`.
3. Reportá una tabla: nota · acción (creada/actualizada) · tipo de cambio · nivel de evidencia. Agregá también las preguntas abiertas creadas.
