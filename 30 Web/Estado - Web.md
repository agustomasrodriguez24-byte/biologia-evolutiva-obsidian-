---
tipo: estado
area: web
fecha_revision: 2026-10-04
---

# Estado - Web

> Nota corta que Claude lee al empezar cada sesión de esta área. Se actualiza con `/cerrar-sesion`.

## Dónde estamos
- **Código de la v1 en marcha.** Proyecto Next.js 16 en `C:\Users\Usuario\Downloads\nutricion evolutiva\web` (fuera del vault). Compila sin errores. Para verlo: preview "web" de Claude (`.claude/launch.json`) o `npm run dev` en esa carpeta → http://localhost:3000.
- Hecho: landing (diseño del v0.3), tienda con filtro por necesidad (`/tienda`), ficha de producto (`/producto/[slug]`) con botón "Pedir por WhatsApp" que arma el mensaje, y página del test como marcador (`/test`). Footer con formas de pago y zona de reparto.
- Productos: `src/data/productos.ts`, copia de las notas de `08 Productos/`. Por ahora solo los lentes. **En producción solo se muestran productos con `estado: activo`**; en desarrollo se ven los borradores con una etiqueta.
- Stack decidido: Next.js + Supabase + Vercel. Supabase y Vercel todavía no están conectados.
- Referencias: prototipo `30 Web/Prototipos/v0.3 prototipo.html` · [[Especificación web]] · [[Hoja de ruta web]] · [[Arquitectura del flujo]] · [[Referencias de diseño]].

- **Brief para la programadora:** [[Brief para desarrollo]] (fuente en el vault). Versión para compartir: https://claude.ai/artifact/CX77uVkWgV6YntbtuqV9zW (privada; Agus la comparte desde el menú Compartir). Si el brief cambia, se actualiza la nota y se republica la página.
- Decidido: dominio `.com.uy` + `.com`; la programadora continúa el proyecto `web/` en GitHub.

- **BMAD (2026-10-07):** el software se construye siguiendo la guía de BMAD de Avril, en sesiones de Claude Code abiertas **en la carpeta del repo** (ahí están las skills `bmad-*`). Se saltea el brainstorming; se arranca por `bmad-product-brief` con `docs/` como base. Los documentos quedan en `documentos/` del repo.

## Próximos pasos
0. **Repositorio:** https://github.com/aaavril/Nutricion-Evolutiva-Web (privado, de Avril). Copia local: `C:\Users\Usuario\Downloads\nutricion evolutiva\Nutricion-Evolutiva-Web`. **Trabajan con BMAD** (documentos primero: brief → PRD → UX → arquitectura → épicas → build) y con las reglas de git del `CLAUDE.md` del repo: commits chicos en español directo a `main`, pull antes de empezar, sin mencionar a Claude, y avisar qué hace cada comando antes de correrlo. Su mención a "datos de pacientes de una nutricionista" **no aplica** a este proyecto y se ignora (confirmado por Agus el 2026-10-06). 2026-10-06: subidos `docs/` (brief, especificación, diseño, dirección creativa, modelo, claims, criterios, prototipo v0.3) y `docs/referencia-web-v0/` (prototipo de código, como referencia). **Cuando cambie una de esas notas en el vault, hay que actualizar su copia en `docs/` y subirla.** Pendiente: cuentas de Vercel y Supabase, y compra de los dominios.
1. Agus carga su número de WhatsApp Business en `web/.env.local` (`NEXT_PUBLIC_WHATSAPP_NUMERO`, ver `.env.example`).
2. Diseñar el test: preguntas, lógica de recomendación y validación nutricional. Después, programarlo en `/test` con captura de contacto y consentimiento.
3. Agus crea las cuentas de Supabase y Vercel → conectar la base (contactos del test, productos, stock) y el panel de administración.
4. Pasar productos a `activo` en el vault (los lentes están en borrador) y conseguir fotos.
5. Medición: UTMs y píxel.

## Huecos conocidos
*Auditoría 2026-10-06.*
- **En producción el catálogo saldría vacío**: no hay ningún producto `activo`.
- El test no tiene diseño ni lógica documentada (pregunta → interpretación → recomendación), ni validador. El test viejo de 28 preguntas no apareció.
- Supabase y Vercel sin cuentas; sin medición (UTMs, píxel).
- Panel de administración (productos, stock, respuestas) sin empezar.
- Las zonas del mapa (v3) no tienen fuente en el vault.
- Dominio, logo e identidad visual definitiva.
- Video de inicio de la landing (hoy hay un marcador).
- Política de privacidad y consentimiento (Ley 18.331), necesaria antes de publicar el test.
- La copia de productos del vault a `productos.ts` es manual; más adelante se puede automatizar.

## Última sesión
2026-10-04: decidido código propio (Next.js + Supabase + Vercel), etapa 1 local sin pasarela y formas de pago. Proyecto creado con landing, tienda, ficha y WhatsApp.
