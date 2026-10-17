---
tipo: negocio
area: contenido
estado: borrador
fecha_creacion: 2026-10-12
fecha_revision: 2026-10-12
relacionados:
  - "[[Campaña - Huevos de campo (anuncio y automatización)]]"
  - "[[Automatizaciones de contenido]]"
  - "[[Estado - Negocio]]"
---

# Automatización n8n - comentario a WhatsApp

> Reemplaza a ManyChat. Cuando alguien comenta **"huevos"** en un reel, n8n le manda un DM con un botón que abre WhatsApp con el pedido ya escrito (`wa.me/59893897963`) y le responde el comentario. El flujo ya está armado: `comentario-huevos-a-whatsapp.json` (en esta carpeta). **No está activo ni conectado todavía.**

## Qué hace el flujo
```
Comentario en Instagram → Meta avisa al webhook de n8n → ¿dice "huevo"? 
   → DM al que comentó (botón "Pedir mi maple" → WhatsApp) → respuesta pública "Te lo mandé por mensaje"
```
Ocho nodos: verificación de Meta (GET), recepción (POST), filtro por palabra, DM con botón, respuesta al comentario. El mensaje precargado dice: *"Hola! Vi tu reel y quiero un maple de huevos de gallina libre. ¿Cómo hago el pedido?"*

## Lo que hace falta (en este orden)
| # | Paso | Quién | Estado |
|---|---|---|---|
| 1 | **Un n8n con dirección pública https**: el VPS ya decidido (Hostinger KVM 1, plantilla n8n, San Pablo, unos USD 5 a 7 por mes) | Agus contrata y paga | Pendiente |
| 2 | Pegar la **clave pública SSH** en el panel del VPS (abajo) | Agus | Pendiente |
| 3 | **App en Meta for Developers** con el producto Instagram, y la cuenta `@agustin.nutricion.evolutiva` como cuenta profesional conectada | Agus | Pendiente |
| 4 | Pedir permisos `instagram_manage_comments` e `instagram_manage_messages`, y suscribir el webhook a **comments** con la URL de n8n + un token de verificación que inventa Agus | Agus (te guío) | Pendiente |
| 5 | En n8n: **importar el JSON**, cambiar los 2 `REEMPLAZAR_…`, y crear la credencial *Header Auth* con el token de Instagram | Agus (te guío) | Pendiente |
| 6 | Probar con un comentario desde otra cuenta; recién ahí **activar** el flujo | Agus + Claude | Pendiente |

### Clave pública SSH (la que ya generaste)
Esta es la **pública** y se puede pegar en el panel del VPS. La privada (`~/.ssh/n8n_servidor`) **nunca** se comparte ni se pega en ningún lado.
```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEoIVgl3nfxwLaQ2NrbljQ4AtOcnimb2wtCrbobP5X1Z agus-n8n-servidor
```

## Lo que hay que reemplazar en el JSON
| Dónde | Qué poner |
|---|---|
| Nodo *Token correcto?* → `REEMPLAZAR_TOKEN_DE_VERIFICACION` | Un texto inventado por Agus (el mismo que pone en Meta al suscribir el webhook) |
| Nodo *Filtrar palabra huevos* → `REEMPLAZAR_ID_DE_INSTAGRAM` | El ID numérico de la cuenta de Instagram (sale en el panel de la app de Meta) |
| Credencial *Header Auth* | `Authorization` = `Bearer <token de acceso de Instagram>`. **Se carga en n8n; no se pega en el chat ni en el vault** |

## Lo que tenés que saber antes (honesto)
- **Limitación grande:** mientras la app de Meta esté en modo desarrollo, el flujo funciona **con cuentas que tienen rol en la app** (la tuya y las de prueba). Para que le llegue el DM a **cualquier persona**, Meta exige **App Review** de esos dos permisos (política de privacidad, video de demostración). Suele llevar días y puede ser rechazado. Esto lo tengo que verificar con la documentación de Meta vigente antes de que contrates nada.
- **Por eso ManyChat existe:** su app ya pasó esa revisión. Es el atajo si no querés pasar por el review.
- **La respuesta del comentario** va con el texto "Te lo mandé por mensaje"; si Instagram lo marca como repetitivo, se rota la frase.
- **Ventana de mensajes:** un DM de respuesta a un comentario solo se puede mandar **una vez por comentario y dentro de los 7 días**.
- **Esto no es obligatorio para vender:** el anuncio con botón de WhatsApp y el comentario fijado con el link funcionan hoy, sin nada de esto.

## Alternativas, de menor a mayor esfuerzo
1. **Sin automatización:** comentario fijado con `wa.me/59893897963` + el botón del anuncio. Costo 0, listo hoy.
2. **ManyChat** (plan gratis de entrada): sin App Review propio; la cuenta la crea Agus.
3. **n8n en el VPS** (este flujo): control total, pero con App Review de Meta.

## Después de esto: lo que n8n ya tenía previsto
Reporte semanal de Instagram y anuncios, planilla de pedidos y caja, lead del test → WhatsApp, recordatorio de recompra ([[Estado - Negocio]]). Este flujo queda como el primero de la lista.
