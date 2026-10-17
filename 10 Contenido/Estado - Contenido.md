---
tipo: estado
area: contenido
fecha_revision: 2026-10-11
---

# Estado - Contenido

> Nota corta que Claude lee al empezar cada sesión de esta área. Se actualiza con `/cerrar-sesion`.

## Qué es esta área
El contenido orgánico de Instagram y TikTok que lleva al test y al WhatsApp. Es el paso 2 de la estrategia acordada el 2026-10-07: **conocimiento → contenido orgánico → producto → anuncios solo sobre ángulos ganadores** ([[Estado - Negocio]]).

## Dónde estamos (2026-10-11)
- **La marca ahora se llama Biología Evolutiva** (decisión de Agus, 2026-10-11). Logo cargado en el sistema (`Empresa/Marca/logos/`). Ya cambiados: `marca.json`, Manual de marca, Brief, Tono de voz y el sello de las piezas ("Semana N de 18 · Biología Evolutiva"). **Sin cambiar todavía:** el usuario de Instagram, la web, el test y las notas del resto del vault.
- **Referencias analizadas (11 y 12/10/2026):** 19 capturas de estilo (`Inspiración/2026-10-11-referencias-de-marca.md`, con muestra de 4 láminas) y 18 cuentas de Instagram: formatos en `Investigación/2026-10-12-cuentas-de-referencia.md`, modelos de negocio en `20 Negocio/Documentos/Referencias de servicios y modelos (2026-10-12).md`, conocimiento en la bandeja (`13 Bandeja de entrada/2026-10-12 Instagram - 18 cuentas de referencia.md`, falta `/procesar-bandeja`).
- **Sistema de contenido con IA instalado** en `10 Contenido/Sistema de contenido/` (empezar por `LEEME.md` y `GUIA.md`). Lo armó la novia programadora de Agus (llegó como `sistema-contenido-ia.tar.gz`): marca, audiencias, tono, plan mensual, carruseles, reels, historias y reporte, con una skill por paso. **No se rediseña: se le carga la estrategia.**
- **Cargado desde el vault:** Brief, Personas (hipótesis), Competencia, Recorrido del cliente, Tono de voz (borrador), Manual de marca, `marca.json` (paletas de la web), Conocimiento (enlaza a las 19 semanas, el hilo y los maestros) y el Banco de ideas (19 semanas × 3 ganchos ya escritos).
- **Estrategia y automatizaciones:** [[Estrategia de contenido]] y [[Automatizaciones de contenido]].
- **Primera campaña lista para lanzar (12/10/2026):** [[Campaña - Huevos de campo (anuncio y automatización)]]: reel de la prueba del huevo, anuncio a WhatsApp con mensaje precargado y automatización del comentario "huevos". Falta de Agus: número de WhatsApp, datos del producto, Página de Facebook vinculada, método de pago y el clip sin subtítulos. Cuenta de Meta Ads conectada pero **sin Página ni Instagram vinculados**.
- **Formatos (14/10/2026):** sumada a [[Estrategia de contenido]] una propuesta de qué trabajo hace cada formato (reel = alcance, carrusel = profundidad, stories = cercanía y cierre), tomada de un reel de @javirodriguezformador. Pendiente que Agus la valide y pase el contenido completo del reel.
- **Todavía no hay ninguna pieza publicada ni programada.**

## Cómo se trabaja con este sistema
Las skills del sistema (`/configurar-marca`, `/adaptar-inspiracion`, `/investigar-contenido`, `/plan-mensual-contenido`, `/carrusel`, `/editar-video`, `/historias`, `/reporte-contenido`) **viven dentro de `10 Contenido/Sistema de contenido/.claude/skills/`**. Para usarlas hay que **abrir Claude en esa carpeta** (ahí está su `CLAUDE.md`). Desde la raíz del vault no aparecen.
Las del vault (`/generar-contenido`, `/crear-campana`, `/revisar-cumplimiento`) siguen igual y se usan para anuncios y para chequear claims.

## Próximos pasos
**Orden decidido por Agus (12/10/2026): primero la base del perfil** ([[Perfil de Instagram - la base]]: 3 fijados, destacadas, bio), **después el plan del mes 1.** Membresía y carta 01 ya están en `20 Negocio/Documentos/`.

Agus tiene que pasar (ver `Plan.md` dentro del sistema):
1. **Reels de referencia** (links o guardados) → `/adaptar-inspiracion`.
2. **Número de WhatsApp** y si el CTA principal es DM con palabra clave.
3. ~~Logo~~ cargado. Falta: qué significa "A/R/M" y si los colores de las piezas pasan a los del logo (negro + dorado).
4. **5 a 10 mensajes reales** para afinar Personas y Tono; prueba de los tres pies.
5. **¿Graba a cámara?** ¿Cuántas piezas por mes?
6. Decidir: si se cambia el usuario de Instagram al nombre nuevo y verificar "Biología Evolutiva" en la DNPI; TikTok `@agustin.tomas.rod` o cuenta de marca, y si el mes 1 abre con el reloj (propuesta) o con el azúcar.

Técnico: **listo (12/10/2026).** Python 3.13 (entorno `C:/Users/Usuario/.venvs/contenido`), Playwright, faster-whisper y FFmpeg instalados y probados con `probar-instalacion.py`; `aplicar-marca.py` corre y el contraste da OK en las 4 paletas. Usar siempre `C:/Users/Usuario/.venvs/contenido/Scripts/python.exe` en vez de `python`.

## Huecos conocidos
- Personas y Tono salen del sistema, no de mensajes reales.
- Sin precios, números de seguidores ni zonas de reparto confirmadas ([[Visión y objetivos]] sigue "a completar").
- Las 18 semanas están en `borrador`.
- El sistema usa publicación manual; **la automatización con Metricool es un agregado nuestro** (ver [[Automatizaciones de contenido]]).

## Documentos
- [[Estrategia de contenido]] · [[Automatizaciones de contenido]] · [[Dirección creativa]] (anuncios) · [[Claims permitidos]]
