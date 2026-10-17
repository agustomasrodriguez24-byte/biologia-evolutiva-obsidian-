# CLAUDE.md · Sistema de contenido con IA

Este repo es el **cerebro del contenido** de una marca: qué es el negocio, a quién le habla, cómo
habla, cómo se ve, y el proceso del mes (investigar, planificar, producir, publicar, medir) con una
skill para cada paso.

**Si la marca todavía no está cargada** (Empresa/Marca/marca.json tiene `{{NOMBRE DE LA MARCA}}`),
lo primero es `/configurar-marca`. Ninguna otra skill produce algo publicable sin eso.

---

## Regla número uno: no se inventa nada

**Antes de escribir una sola línea de cara al público, leer [Empresa/Brief.md](Empresa/Brief.md).** Y
antes de diseñar o escribir cualquier pieza, el [Manual de marca](Empresa/Marca/Manual%20de%20marca.md):
manda sobre cualquier otra guía.

| Dato | Dónde está |
|---|---|
| Qué es el negocio, qué puede prometer y qué no se dice nunca | [Empresa/Brief.md](Empresa/Brief.md) |
| **Cualquier número que cambia con el tiempo** (años, clientes, reseñas, seguidores) | [Empresa/Números.md](Empresa/Números.md) |
| Productos, servicios, precios, requisitos | [Empresa/Catálogo.md](Empresa/Catálogo.md) |
| A quién le hablamos, con qué dolores | [Empresa/Personas.md](Empresa/Personas.md) |
| Qué se quiere mover este trimestre | [Empresa/Objetivos.md](Empresa/Objetivos.md) |
| El recorrido del cliente, de la duda a la compra | [Empresa/Recorrido del cliente.md](Empresa/Recorrido%20del%20cliente.md) |
| La competencia y las cuentas para mirar | [Empresa/Competencia.md](Empresa/Competencia.md) |
| **La base de conocimiento técnico del rubro** (normas, reglas, datos que se afirman en una pieza) | [Empresa/Conocimiento/Conocimiento.md](Empresa/Conocimiento/Conocimiento.md) |
| La marca: estrategia, voz, logo, colores, letras, fotos | [Empresa/Marca/Manual de marca.md](Empresa/Marca/Manual%20de%20marca.md) |
| Cómo se escribe | [Empresa/Marca/Tono de voz.md](Empresa/Marca/Tono%20de%20voz.md) |
| **La ficha que leen los scripts** (cuenta, CTA, hashtags, prohibidos, paletas, módulos) | `Empresa/Marca/marca.json` |
| El área de contenido entera: estrategia, el mes paso a paso, dónde va cada archivo | [Áreas/Contenido/Contenido.md](Áreas/Contenido/Contenido.md) |

Un precio inventado se le cobra a alguien. Una cifra inventada es publicidad engañosa. **Si el dato
no está, se pregunta y se anota en [Plan.md](Plan.md)** como `[CONFIRMAR con <quién>]`.

**Toda afirmación técnica** (una norma, una regla, un dato del rubro) sale de
`Empresa/Conocimiento/`, con su fuente. Si no está ahí, no se afirma.

---

## Base vs. resultados

**Documentos base:** la verdad sobre el negocio y la estrategia. Cambian poco, se corrigen, no se
regeneran. Viven en `Empresa/` y en `Áreas/Contenido/Contenido.md`. **Nunca llevan fecha en el nombre.**

**Documentos resultado:** lo que se produce. Llevan fecha en el nombre (`aaaa-mm`), se acumulan, no
se pisan: `Investigación/`, `Plan mensual/`, `Reportes/`, `outputs/`.

**Lo que ya sabemos** (en `Contenido.md`) solo lleva lo que tiene evidencia. Lo que falló, también.

---

## Las skills

| Skill | Cuándo | Deja |
|---|---|---|
| `/configurar-marca` | Una vez al empezar, y cada vez que cambia la marca | `Empresa/` completo, `marca.json`, `marca.css` |
| `/adaptar-inspiracion` | Cuando hay un reel o carrusel de otra cuenta que te gustó | `Inspiración/aaaa-mm-dd-tema.md` + idea en el banco o pieza en el plan |
| `/investigar-contenido` | La última semana del mes | `Investigación/aaaa-mm.md` |
| `/plan-mensual-contenido` | Justo después | `Plan mensual/aaaa-mm.md` |
| `/carrusel` | Antes de cada fecha | `outputs/aaaa-mm/carruseles/NN-tema/` |
| `/editar-video` | Antes de cada fecha (módulo video) | `outputs/aaaa-mm/videos/NN-tema/` |
| `/historias` | Una vez por semana (módulo opcional) | `outputs/aaaa-mm/historias/NN-tema/` |
| `/reporte-contenido` | El día 1 | `Reportes/aaaa-mm-dd.md` |
| `design-system` | La leen las otras: no se llama sola | — |

**Módulos opcionales:** `marca.json` → `modulos`. Si `historias` es `false`, ninguna skill propone
historias y el plan no lleva la sección 4. Si `video` es `false`, el plan arma el mes con carruseles.

**Una skill produce una cosa y la deja en un lugar.** Si se mueve un archivo, revisar las skills que
lo nombran.

---

## Convenciones

- **Idioma y trato:** los de `marca.json` (`idioma`, `trato`). Por defecto español rioplatense, voseo
- **Fechas `dd/mm/aaaa`** dentro de los documentos. Nunca fechas relativas ("la semana pasada")
- **Los links entre documentos van relativos** (`[Brief](Empresa/Brief.md)`): el repo se puede leer en Obsidian
- **Un dato que falta se escribe "Falta el dato"** y va a [Plan.md](Plan.md). Nunca se estima
- **Nada de guion largo (—)** en lo que se publica → [Tono de voz](Empresa/Marca/Tono%20de%20voz.md)
- **Los colores y el logo no se cambian en el CSS:** se cambia `marca.json` y se corre
  `python Áreas/Contenido/herramientas/aplicar-marca.py`
- **Un commit por cosa terminada**, si el repo está en git. Las fotos y los videos no se suben (`.gitignore`)

---

## Instalación de Biología Evolutiva (11/10/2026)

- **La marca se llama Biología Evolutiva** (decisión de Agus, 11/10/2026; antes Nutrición Evolutiva). Las notas del vault que llevan el nombre viejo en el título (por ejemplo [[Sistema de salud Nutrición Evolutiva]]) no se renombran: se enlazan igual.

- **Este sistema vive dentro del vault de Obsidian** (`10 Contenido/Sistema de contenido/`). La verdad del contenido está en las notas del vault (`../../18 Sistema de salud/`, `../../19 La mente de los maestros/`, `../../20 Negocio/`); `Empresa/Conocimiento/Conocimiento.md` las **enlaza**, no las copia.
- **Contexto de área:** `../Estado - Contenido.md` · estrategia: `../Estrategia de contenido.md` · automatizaciones: `../Automatizaciones de contenido.md`.
- **Regla de la marca:** se escribe desde la verdad de Agus y sus maestros, citándolos por nombre. La capa legal (Uruguay, MSP) vive solo en `Empresa/Brief.md` y `marca.json` → `prohibido`.
- **Publicar:** Metricool (brand `agustin.nutricion.evolutiva`, id 7297706; IG + TikTok). Claude programa **para revisión**; nada sale sin el OK de Agus en el chat.
- **Sello obligatorio en toda pieza:** "Semana N de 18 · Biología Evolutiva" (ver `Áreas/Contenido/Contenido.md`).
- **Skills:** para usar las de esta carpeta, abrir Claude **en esta carpeta**.
