---
tipo: web
fecha_creacion: 2026-10-06
fecha_revision: 2026-10-06
relacionados:
  - "[[Especificación web]]"
  - "[[Hoja de ruta web]]"
  - "[[Referencias de diseño]]"
  - "[[Dirección creativa]]"
---

# Brief para desarrollo

> Documento para la programadora. Explica qué es Nutrición Evolutiva, qué hay que construir, cómo y con qué reglas. Versión publicada para compartir: ver *Estado - Web*.

## 1. Qué es Nutrición Evolutiva
Un sistema de salud basado en la biología humana y en la evidencia, con una tienda de alimentos y herramientas filtrados por ese conocimiento. Etapa 1: venta local en **Maldonado y Punta del Este**, con reparto propio. **No hay pasarela de pago**: el cliente pide por WhatsApp y el pago (transferencia, efectivo contra entrega o link de Mercado Pago) se coordina en forma personal.

**Lo que la web tiene que transmitir:** servicio premium, fundamentos reales, que sabemos lo que hacemos. Cada producto muestra su **nivel de evidencia (A–F)**, sus fuentes y lo que puede y no puede hacer. Esa honestidad es la marca.

**Frase guía:** *"El cuerpo sabe regularse. Nosotros le acercamos los ladrillos que necesita y te ahorramos el trabajo de buscarlos, filtrarlos y verificarlos."*

## 2. Cómo encaja todo
```
Obsidian (vault)  →  GitHub  →  Next.js en Vercel  →  cliente
  contenido y              código y      web pública         │
  conocimiento             versiones                         ├─► WhatsApp (venta)
                                                             └─► Supabase (test, contactos, pedidos)
                                     panel /admin  ◄─────────────┘
```
- **Contenido** (textos, claims, fichas, fuentes): sale del vault de Obsidian. Solo se publican notas con `estado: activo`. Hoy se copia a `src/data/productos.ts`; más adelante, un script lo genera al compilar.
- **Datos operativos** (precio, stock, visibilidad, contactos, respuestas del test, pedidos): viven en Supabase y se editan desde `/admin`.
- **Regla:** los textos de salud **nunca** se editan desde el panel; solo desde el vault, porque ahí pasan el control de claims.

## 3. Stack y cuentas
| Pieza | Elección | Notas |
|---|---|---|
| Framework | **Next.js 16** (App Router, TypeScript) | Proyecto ya creado (ver §4) |
| Estilos | CSS con tokens (portado del prototipo) + Tailwind v4 disponible | Mantener los tokens de §7 |
| Hosting | **Vercel** | Previews por cada PR |
| Código | **GitHub**, repositorio privado `aaavril/Nutricion-Evolutiva-Web` | Planificación con BMAD; flujo de git según su `CLAUDE.md` |
| Base de datos y login | **Supabase** (Postgres + Auth + RLS) | Región sugerida: São Paulo; validar con el abogado (Ley 18.331) |
| Dominio | **`.com.uy` principal + `.com` redirigiendo** | Verificar disponibilidad antes de comprar |
| Medición | Meta Pixel + Conversions API, Vercel Analytics | UTMs persistidas (§9) |
| Errores | Sentry o el monitoreo de Vercel | Alertas al mail de Agus |

**Las cuentas son de Agus** (GitHub, Vercel, Supabase, dominio, Meta). La programadora entra como colaboradora. Ninguna clave se comparte por chat: van a las variables de entorno de Vercel.

## 4. Estado actual del código
Hay un prototipo de código en Next.js 16 + TypeScript que compila sin errores. En el repo está en `docs/referencia-web-v0/`, **como referencia**: si se usa como base de la app se decide en el paso de arquitectura de BMAD.

| Ruta | Estado |
|---|---|
| `/` landing | Hecha, con el diseño del prototipo v0.3. Falta el video del hero |
| `/tienda` | Hecha, filtro por necesidad |
| `/producto/[slug]` | Hecha la versión básica de la ficha con botón de WhatsApp. **Hay que llevarla al nivel de landing premium (§6)** |
| `/test` | Marcador; falta todo (§8) |

Archivos clave: `src/data/productos.ts` (productos, copia del vault) · `src/lib/whatsapp.ts` (links y mensajes) · `src/app/globals.css` (tokens) · `.env.example`.

Correr en local: `npm install` y `npm run dev` → http://localhost:3000.

## 5. Mapa del sitio
| Página | Ruta | Prioridad |
|---|---|---|
| Inicio | `/` | v1 |
| Tienda | `/tienda` | v1 |
| **Landing de producto** (destino de los anuncios) | `/producto/[slug]?angulo=` | v1, la más importante |
| Test gratuito | `/test` | v1 |
| Cómo elegimos (criterios y niveles de evidencia) | `/como-elegimos` | v1, construye confianza |
| Privacidad · Términos · Aviso de salud | `/privacidad` `/terminos` `/aviso-de-salud` | v1, obligatorias antes del test |
| Panel | `/admin` (con login) | v1 |
| Mapa del cuerpo y órganos | `/mapa`, `/organo/[slug]` | v3 |
| Blog | `/blog` | v2 |
| Buscador por suscripción | `/buscador` | v3 |

## 6. La landing de producto (la pieza clave)
Cada producto tiene su landing, que es el destino de sus anuncios. Tiene que verse como la de una marca premium y convertir en el celular.

**Message match por ángulo:** el parámetro `?angulo=<id>` cambia solo el titular y el subtítulo del hero, para que repitan la promesa del anuncio. Los textos de cada ángulo vienen del archivo del producto. Sin parámetro o con uno desconocido, se usa el titular por defecto.

**Secciones, en orden:**
1. **Hero**: titular (según ángulo), beneficio, sello de evidencia, foto o video del producto, precio, botón **"Pedir por WhatsApp"**.
2. **Barra de confianza**: reparto propio en Maldonado y Punta del Este · pago a coordinar · ficha de valor y video de regalo · fuentes citadas.
3. **Para qué te sirve**: la necesidad, en simple.
4. **Cómo encaja en tu biología**: la cadena visual órgano → lo que necesita → mecanismo → hábito → producto.
5. **Cómo usarlo**: pasos, empezando por el hábito gratuito.
6. **Qué podés esperar y qué no**: bloque destacado de honestidad. Es el diferencial.
7. **Origen y trazabilidad**: proveedor, zona, cómo se produce, fotos.
8. **La evidencia**: tabla de afirmaciones con su nivel y su fuente.
9. **Preguntas frecuentes** (acordeón).
10. **Para quién no es.**
11. **Cierre**: CTA final.
- **En el celular**: barra fija abajo con precio y "Pedir por WhatsApp".
- **El mensaje de WhatsApp** lleva el producto y un código de referencia del anuncio (ej. `Ref: LENTES-SIT-H2`) para atribuir la venta.

## 7. Diseño
**Dirección:** estructura de Promix, colores profundos, explicación clara al estilo Mill. Premium, sobrio, con la evidencia como protagonista visual.

**Tokens actuales** (en `globals.css`, con modo oscuro):
| Token | Claro | Uso |
|---|---|---|
| `--bg` | `#f5f0e6` | Fondo |
| `--surface` | `#fffdf8` | Tarjetas |
| `--ink` | `#1d221f` | Texto |
| `--deep` / `--deep-2` | `#1b2a23` / `#12382a` | Bandas oscuras, botones |
| `--accent` | `#b5601f` | Ámbar, acentos |
| `--ev-a` … `--ev-f` | verde → rojo | Sellos de evidencia |

**Tipografías:** Petrona (titulares), Figtree (texto), JetBrains Mono (datos y niveles).

**Referencias para estudiar** (tomar ideas, no copiar):
| Marca | Qué mirar |
|---|---|
| Promix Nutrition | Estructura de home, menú por necesidad, tarjetas |
| Mill | Explicaciones simples con pasos y elección de objetivo |
| Ritual | Trazabilidad: de dónde viene cada ingrediente |
| Seed | Ciencia presentada con elegancia, citas visibles |
| AG1 | Landing de producto larga: beneficios, uso, FAQ, comparativas |
| Thorne / Momentous | Señales de credibilidad y rigor |

**Reglas:** mobile first (la mayoría del tráfico viene de Meta, desde el celular) · fotos reales de producto en contexto · nada de imágenes de stock genéricas · accesibilidad AA · respetar `prefers-reduced-motion`.

## 8. Test gratuito
- **Contenido pendiente**: las preguntas y la lógica se están diseñando y las valida un nutricionista. Construir el **motor** con las preguntas en un archivo de configuración (JSON/TS), así se cambian sin tocar el código.
- **Flujo:** objetivo → preguntas (una por pantalla, barra de progreso) → **resultado básico en pantalla** → oferta del plan completo por WhatsApp a cambio del contacto.
- **Consentimiento (Ley 18.331):** casilla **sin marcar por defecto**, con enlace a la política de privacidad. Se guarda la fecha, la versión de la política y el texto aceptado. Sin consentimiento no se guardan las respuestas.
- Pedir solo lo necesario: nombre, WhatsApp o email.
- Las respuestas, el resultado y la versión del test se guardan en Supabase, con las UTM de origen.

## 9. Datos (Supabase)
| Tabla | Campos principales |
|---|---|
| `productos_operacion` | `slug`, `precio`, `stock`, `visible`, `actualizado` |
| `contactos` | `id`, `nombre`, `whatsapp`, `email`, `consentimiento` (fecha, versión), `utm_*`, `angulo`, `creado` |
| `respuestas_test` | `id`, `contacto_id`, `version_test`, `respuestas` (jsonb), `resultado`, `creado` |
| `pedidos` | `id`, `contacto_id`, `items` (jsonb), `total`, `forma_pago`, `estado`, `fecha_entrega`, `ref_anuncio`, `creado` |

- **RLS activado en todas las tablas.** El público solo inserta a través de acciones del servidor validadas (zod). Leer y editar es solo para el rol admin.
- **El panel `/admin`:** login de Supabase (solo Agus) · precio, stock y visibilidad · contactos y respuestas del test · **carga de pedidos de WhatsApp con su `ref_anuncio`**. Esto último cierra el círculo entre el peso invertido y la venta.
- **Derecho de borrado:** desde el panel se puede eliminar a un contacto y todas sus respuestas.

## 10. Medición
- **Eventos:** `ViewContent` (landing) · `ClickWhatsApp` (personalizado) · `Lead` (test con contacto) · `Purchase` (al cargar un pedido en el panel, enviado por Conversions API desde el servidor).
- **UTM:** se guardan al entrar (cookie propia, 30 días) y viajan con el lead, el pedido y el código de referencia del mensaje de WhatsApp.
- **Banner de cookies** con opción de rechazar; el píxel carga solo con consentimiento.
- Convención de nombres de anuncios: ver [[Dirección creativa]].

## 11. Seguridad y robustez
- Claves solo en variables de entorno de Vercel. La `service_role` de Supabase **nunca** llega al navegador.
- Validación en el servidor de todo lo que envía el usuario · trampa anti-spam (honeypot) y límite de envíos en formularios.
- Cabeceras de seguridad (CSP, HSTS), HTTPS forzado.
- **Flujo de git:** el que define el `CLAUDE.md` del repositorio. Hoy: commits directos a `main`. Al salir a producción se pasa a trabajar en `dev`, con `main` solo para lo publicado y preview de Vercel que **Agus aprueba** antes de publicar.
- Dependabot activo · backups de Supabase · monitoreo de errores y de disponibilidad.
- Páginas estáticas siempre que se pueda: si Supabase cae, la tienda y las landings siguen funcionando.

## 12. Rendimiento y SEO
- **Core Web Vitals:** LCP < 2,5 s, CLS < 0,1, INP < 200 ms, medidos en celular.
- `next/image`, fuentes con `next/font`, generación estática de las landings.
- Metadatos e imagen para compartir (Open Graph) por producto · `sitemap.xml` · `robots.txt` · `lang="es"`.
- Datos estructurados de producto **sin afirmaciones de salud**.

## 13. Reglas de contenido (no negociables)
1. No se publica nada en `borrador`: en producción solo productos `activo` (ya implementado).
2. Ningún texto promete curar, tratar ni garantizar resultados.
3. El aviso de salud va en el pie y en cada landing.
4. Si falta un texto, se deja el espacio marcado y se avisa. **No se inventa contenido de salud.**

## 14. Entregas
| # | Entrega | Incluye |
|---|---|---|
| M0 | Cuentas y accesos | GitHub, Vercel, Supabase y dominio a nombre de Agus; colaboradora invitada |
| M1 | Base en línea | Repo en GitHub, deploy en Vercel, dominio conectado, previews |
| M2 | Landing de producto premium | §6 completa, con ángulos y barra de WhatsApp fija en el celular |
| M3 | Home, tienda y confianza | Pulido de home y tienda, `/como-elegimos`, páginas legales |
| M4 | Test y datos | Motor del test, consentimiento, Supabase con RLS |
| M5 | Panel y medición | `/admin`, eventos, UTM, Conversions API |
| M6 | Control y lanzamiento | Lista de control final, Core Web Vitals, prueba en celulares reales |

**Lista de control antes de lanzar:** links de WhatsApp con el número real · ningún borrador visible · consentimiento probado · eventos vistos en Meta · Lighthouse en celular ≥ 90 · prueba en iPhone y Android · páginas legales publicadas · backups activos.

## 15. Qué aporta Agus
Fotos de producto y de origen · logo e identidad · textos aprobados desde el vault · precios · número de WhatsApp Business · accesos a las cuentas · aprobación de cada preview.

## 16. Pendiente de definir
Logo e identidad final · video del hero · preguntas del test · textos legales (con abogado) · catálogo de lanzamiento (alimentos del núcleo) · precios.
