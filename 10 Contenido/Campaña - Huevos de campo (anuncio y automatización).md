---
tipo: contenido
formato: campana
estado: idea
producto: Maple de huevos de gallina libre
angulos: [origen-trazabilidad, honestidad, local]
fecha_inicio:
presupuesto_diario:
conceptos: []
fecha_creacion: 2026-10-12
fecha_revision: 2026-10-12
---

# Campaña - Huevos de campo (anuncio y automatización)

Sistema: [[Dirección creativa]] · Estrategia: [[Estrategia de contenido]] · Automatizaciones: [[Automatizaciones de contenido]] · Reel base: `Sistema de contenido/Áreas/Contenido/Inspiración/2026-10-12-reel-huevos.md`.

> **Estado: todo armado para que Agus solo cargue la tarjeta.** Faltan 4 datos suyos (ver *Antes de lanzar*). Nada se activa ni se gasta sin su confirmación.

## El circuito completo
```
Reel / anuncio  →  persona comenta "huevos"  →  respuesta automática por DM con un botón
   →  se abre WhatsApp con el mensaje ya escrito  →  la persona toca enviar
   →  a Agus le llega: "quiero un maple de huevos de gallina libre"  →  Agus confirma y reparte
```
Hay **dos entradas** al mismo mensaje: el comentario del reel orgánico y el anuncio con botón "Enviar mensaje por WhatsApp".

## Brief
- **Producto:** maple de huevos de gallina libre (el que se ve en el reel). **Falta el dato:** productor y origen, cantidad por maple, precio, días y zonas de entrega.
- **Objetivo:** mensajes de WhatsApp con pedido de maple.
- **Público:** Maldonado y Punta del Este, 25 a 55 años, que cuida lo que come. Audiencia abierta de Meta (no se fuerzan intereses; se mide y se ajusta).
- **Promesa máxima permitida:** "huevos de gallinas que viven en el campo" y lo que se ve en el video. **No** se promete efecto en la salud.
- **Destino:** WhatsApp con mensaje precargado.

## Ángulos elegidos
| Ángulo | Idea central | Por qué este |
|---|---|---|
| 4 · Origen y trazabilidad | "Así viven las gallinas que ponen estos huevos" | Es lo que muestra el reel y se puede verificar |
| 5 · Honestidad | "Hacé la prueba vos mismo: 3 segundos" | La prueba es el gancho y no promete de más |
| 8 · Local y personal | "Te lo llevamos en Maldonado y Punta del Este" | CTA a WhatsApp con reparto propio |

## La pieza (versión para anuncio)
**Hay que partir del clip sin subtítulos:** el video que pasó Agus los tiene quemados y con errores ("diversidad volutiva", "nutricionó"). Con el original, `/editar-video` arma esta versión de **30 a 40 s**:

| Tiempo | Imagen | Texto en pantalla | Voz |
|---|---|---|---|
| 0 a 3 s | Rompe el huevo de góndola | **"LA PRUEBA DEL HUEVO"** | "Te hago la prueba de un huevo común" |
| 3 a 12 s | La yema se desparrama; "no pasa los 3 segundos" | "NO AGUANTA" | Mismo audio, recortado |
| 12 a 20 s | Corte a las gallinas en el campo | "ASÍ VIVEN LAS NUESTRAS" | "Estos vienen de gallinas libres" |
| 20 a 33 s | Rompe el huevo de campo; yema firme; cuenta los segundos | "3… 4… 5… 6… 7" | "Mirá cuánto aguanta" |
| 33 a 38 s | A cámara | **"Maple de huevos de campo. Escribime 'huevos'"** | "Si querés un maple, comentame huevos" |

Sello al final (2 s): **"Semana 8 de 18 · Biología Evolutiva"**.

**Hooks alternativos (se graba una vez, cambian los primeros 3 s):**
- H1 · "LA PRUEBA DEL HUEVO"
- H2 · "¿Tu huevo pasa los 3 segundos?"
- H3 · "Esto es lo que comés cuando comprás huevos"

## Textos del anuncio
**Texto principal (versión corta, recomendada):**
> Hacé la prueba del huevo: cascá uno del almacén y uno de campo, y mirá cuánto aguanta la yema.
> Los nuestros vienen de gallinas que viven en el campo y te los llevamos a Maldonado y Punta del Este.
> Tocá el botón y pedí tu maple.

**Texto principal (versión larga):**
> Casi todos los huevos dicen "de campo" en el envase. La forma de saberlo es mirarlo: la yema firme, la clara que se sostiene, la prueba de los 3 segundos.
> Estos son huevos de gallinas libres, de [PRODUCTOR / ZONA], y llegan a tu casa los martes. Pedí tu maple por WhatsApp.

| Campo | Texto |
|---|---|
| **Título** | Huevos de gallina libre en Maldonado y Punta del Este |
| **Descripción** | Hacé la prueba de los 3 segundos |
| **Botón** | Enviar mensaje por WhatsApp |
| **Mensaje precargado** | `Hola! Vi tu reel y quiero un maple de huevos de gallina libre. ¿Cómo hago el pedido?` |

*`[PRODUCTOR / ZONA]` y "los martes" se confirman antes de publicar; si no están verificados, se sacan.*

## La automatización del comentario
**Qué hace:** cuando alguien comenta "huevos" (o "huevo") en el reel, le llega un mensaje directo con un botón que abre WhatsApp con el pedido ya escrito.

**Herramienta:** ManyChat (plan gratis alcanza para empezar). **La cuenta y la conexión con Instagram las tiene que hacer Agus**: yo no creo cuentas. Yo dejo la configuración escrita acá:

| Campo en ManyChat | Valor |
|---|---|
| **Disparador** | Comentario en la publicación (el reel) o en cualquier publicación |
| **Palabras clave** | `huevos`, `huevo` (sin distinguir mayúsculas) |
| **Respuesta al comentario** | "Te lo mandé por mensaje 🥚" (una variante por comentario para no repetirse) |
| **Mensaje directo** | "Hola! Gracias por escribir. Tocá el botón y se te abre WhatsApp con tu pedido ya escrito. Entregamos en Maldonado y Punta del Este." |
| **Botón** | "Pedir mi maple" → `https://wa.me/59893897963?text=Hola!%20Vi%20tu%20reel%20y%20quiero%20un%20maple%20de%20huevos%20de%20gallina%20libre.%20%C2%BFC%C3%B3mo%20hago%20el%20pedido%3F` |
| **Etiqueta** | `huevos-reel-1` (para contar cuántos llegaron por esta vía) |

`59893897963` es el número de Agus (093 897 963) **sin el +**, con el 598 al principio. **Número dado por Agus el 12/10/2026.**

**En WhatsApp Business** (lo configura Agus en la app, Herramientas para el negocio):
- **Mensaje de bienvenida** para cuando llega ese primer mensaje: "Hola! Gracias por el pedido. Un maple son [N] huevos a $[PRECIO]. Entregamos en [ZONAS] los [DÍAS]. ¿Para qué dirección?"
- **Etiqueta** "Huevos" para ver cuántos pedidos salieron de esto.

## Antes de lanzar (lo que falta)
| # | Qué | Quién |
|---|---|---|
| 1 | ~~Número de WhatsApp Business~~ **Cargado: 093 897 963** (falta confirmar que es el de WhatsApp Business) | Agus |
| 2 | **Producto:** productor, cantidad por maple, precio, días y zonas | Agus |
| 3 | **Página de Facebook** vinculada a la cuenta de anuncios (hoy hay 0) y a Instagram | Agus, en Business Manager (te guío) |
| 4 | **Método de pago** en la cuenta de anuncios | Agus (yo no cargo datos de pago) |
| 5 | Clip **sin subtítulos** del reel | Agus |
| 6 | Cuenta de ManyChat conectada a Instagram | Agus |

## Presupuesto y reglas (propuesta, decide Agus)
Siguiendo [[Dirección creativa]]: **3 hooks × mismo presupuesto chico durante 3 a 5 días**, segmentado a Maldonado y Punta del Este.
- **Sugerido:** unos USD 3 a 5 por día por hook. Agus pone el tope y la fecha final.
- **Cortar** el hook que quede en el tercio peor de hook rate y de clics, o cuyo costo por mensaje supere el doble del promedio.
- **Escalar** al ganador de a +20 o 30 % cada 2 o 3 días, mientras el costo por pedido se sostenga.
- **Nombres:** `HUEVOS_ORIGEN_REEL_H1_V1`, `…_H2_V1`, `…_H3_V1`.
- La campaña se crea **pausada** en Adspirer y solo se activa con el OK explícito de Agus en el chat.

## Afirmaciones y respaldo
| Afirmación | Nota | Nivel |
|---|---|---|
| "Huevos de gallinas libres / que viven en el campo" | Falta la ficha del producto y del productor | Pendiente de verificar |
| "Mirá cuánto aguanta la yema" (la prueba de los 3 segundos) | Es una demostración, no un claim de salud | Sin claim |
| "Te lo llevamos en Maldonado y Punta del Este" | [[Logística]], falta confirmar zonas | Pendiente |
| *(no se dice)* "mejor para la salud", "más nutritivo", "los del súper son mentira" | Fuera de [[Claims permitidos]] | Prohibido |

**Revisión de cumplimiento:** textos escritos con la lista de [[Claims permitidos]]. Corre `/revisar-cumplimiento` antes de cargarlos.

## Anuncios publicados
| Nombre | Destino | Fecha |
|---|---|---|

## Resultados
| Anuncio | Impresiones | Hook rate | CTR | Mensajes WA | Costo/mensaje | Pedidos | Costo/pedido | Decisión |
|---|---|---|---|---|---|---|---|---|

## Aprendizajes
<!-- Pasarlos también a la tabla de Aprendizajes de Dirección creativa -->
