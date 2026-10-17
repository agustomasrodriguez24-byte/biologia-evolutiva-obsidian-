---
name: importar-instagram
description: Importa al vault el "archivo de oro" de Instagram de Agus (posts que se manda al chat con @nutricionancestral.uy) a partir de la exportación de mensajes de Instagram, los ordena por tema y los deja en la bandeja para procesar. Usar cuando Agus dice "importá Instagram", "procesá el archivo de oro", "ya bajé la exportación de Instagram" o deja un ZIP de Meta en Descargas.
---

# Importar Instagram

Guía para Agus: [[Importar desde Instagram]] (`00 Sistema/`).

## Privacidad (no negociable)
La exportación trae **todas** las conversaciones de Agus. Se procesa **solo** el chat pedido (por defecto, el de `nutricionancestral`; el grupo con eselmomento13 solo si Agus lo pide). Nunca leer, citar ni resumir otras conversaciones. El ZIP no se mueve ni se copia al vault, y nunca va a git.

## Pasos
1. **Encontrá el archivo.** Buscá en `C:\Users\Usuario\Downloads` el ZIP más reciente de Meta (suele llamarse `instagram-...zip`). Si hay varios, preguntá cuál.
2. **Ubicá el chat sin leer nada más:**
   `uv run --python 3.13 .claude/skills/importar-instagram/extraer.py "<zip>" --chat nutricionancestral --listar`
   (`uv` está en `C:\Users\Usuario\AppData\Local\Microsoft\WinGet\Packages\astral-sh.uv_Microsoft.Winget.Source_8wekyb3d8bbwe\uv.exe` si no está en el PATH.) Si aparecen dos (el directo y el grupo), confirmá con Agus cuál o cuáles.
3. **Importaciones siguientes:** mirá en `00 Sistema/Importar desde Instagram.md` la fecha de la última importación y pasala con `--desde` para traer solo lo nuevo.
4. **Extraé** a un archivo temporal en el scratchpad: `... --chat <carpeta> --salida <scratchpad>/instagram.md`.
5. **Ordená por tema** leyendo ese archivo: Nutrición y cuerpo · Hábitos (luz, sueño, movimiento) · Mente · Marketing y ventas · Producción de contenido · IA y automatización · Descartado (prácticas sin respaldo o riesgosas, con el motivo). Si son muchos posts, trabajá por tandas.
6. **Escribí en la bandeja** (`13 Bandeja de entrada/`) con la plantilla Entrada, una nota por tema: `AAAA-MM-DD Instagram - <tema>.md`. Cada post con autor, link, idea clave y, para salud, la afirmación concreta a verificar.
7. **Referentes:** actualizá la tabla de referentes en `00 Sistema/Importar desde Instagram.md` (cuenta · tema · qué tomamos · confianza).
8. **Reels sin texto:** listá los que parezcan clave y pedile a Agus que resuma en una línea qué dicen, o que pase el link del video original si está en YouTube.
9. **Registrá** la fecha de esta importación en la guía y una línea en `00 Sistema/Registro de cambios.md`.
10. **Siguiente paso:** ofrecé correr `/procesar-bandeja` sobre las notas de salud (ahí se verifican contra fuentes y reciben nivel A–F) y llevar lo de marketing a `20 Negocio/Dirección creativa.md` (aprendizajes y referentes de formato).

## Reglas
- Lo que dicen los referentes entra como nivel E/F hasta verificarlo. Nunca se publica sin pasar por `/procesar-bandeja` y `/revisar-cumplimiento`.
- No inventar el contenido de un reel que no se pudo leer.
