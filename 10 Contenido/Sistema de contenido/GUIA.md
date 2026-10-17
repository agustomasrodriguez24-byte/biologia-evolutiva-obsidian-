# Guía para aplicar el sistema

**Cómo se pone en marcha este sistema para una marca nueva, de cero a la primera pieza publicada.**
Está pensada para alguien que no programa: casi todo se hace hablando con Claude, y cada paso dice
qué escribir.

**Tiempo total la primera vez:** unas 2 horas para dejarlo andando (pasos 1 a 5), y después el mes
corre solo con las skills.

---

## Qué es esto, en un minuto

Un repo (una carpeta) con **todo lo que necesita Claude para hacer el contenido de una marca como
lo haría alguien del equipo**: qué es el negocio, a quién le habla, cómo habla, cómo se ve, qué no se
puede decir, y un proceso de cinco pasos por mes con una skill para cada uno.

```
             ┌──────────── una vez ────────────┐
             │   /configurar-marca             │  negocio · audiencias · tono · diseño · conocimiento · módulos
             └───────────────┬─────────────────┘
                             ▼
  ┌─────────────────────────── cada mes ────────────────────────────┐
  │                                                                  │
  │  /adaptar-inspiracion ──┐   (todo el mes, cuando ves algo)       │
  │                          ▼                                        │
  │  1 /investigar-contenido → 2 /plan-mensual-contenido               │
  │                                   │                                │
  │             ┌─────────────────────┼─────────────────────┐          │
  │             ▼                     ▼                     ▼          │
  │        /carrusel           /editar-video          /historias       │
  │             └───────── 4 publicar (a mano) ─────────────┘          │
  │                                   ▼                                │
  │                       5 /reporte-contenido ──▶ el mes siguiente    │
  └──────────────────────────────────────────────────────────────────┘
```

**Lo que lo hace funcionar** es que cada skill lee lo mismo antes de escribir:
`Empresa/` (la verdad del negocio), `Empresa/Marca/` (tono y diseño) y lo que dejó la skill anterior.
Por eso las piezas suenan y se ven igual aunque las haga Claude, y por eso no se inventan datos.

---

## Paso 1 · Instalar (15 minutos)

1. **Copiá la carpeta `sistema-contenido-ia`** donde vayas a trabajar y renombrala con el nombre de
   la marca si querés (`contenido-mimarca`)
2. **Abrila con Claude** (Claude Code o Cowork, conectando la carpeta). Claude lee `CLAUDE.md` solo y
   las skills aparecen en la lista con la barra `/`
3. **Instalá lo que usan los scripts** (una vez por computadora). Pedile a Claude "instalá lo que
   necesita el sistema" o hacelo a mano:

| Para qué | Qué | Windows | Mac |
|---|---|---|---|
| Todo | Python 3.10+ | `winget install Python.Python.3.12` | `brew install python` |
| Carruseles e historias | Playwright (usa tu Chrome) | `pip install playwright` | ídem |
| Videos | FFmpeg | `winget install Gyan.FFmpeg` | `brew install ffmpeg` |
| Videos con voz | faster-whisper | `pip install faster-whisper` | ídem |
| Videos animados | Node.js 22 | `winget install OpenJS.NodeJS.LTS` | `brew install node` |

4. **Probá:** `python Áreas/Contenido/herramientas/probar-instalacion.py`. Dice OK o MAL en cada cosa
   y deja el resultado en `instalacion.txt` para que Claude lo lea

**Si no vas a hacer videos**, alcanza con Python y Playwright.

---

## Paso 2 · Cargar la marca (1 hora): `/configurar-marca`

Escribí **`/configurar-marca`** y pasale lo que tengas. Es una conversación por bloques; cada bloque
se escribe, se muestra y se aprueba antes de pasar al siguiente. Podés cortar y seguir otro día.

**Antes de arrancar, juntá esto** (no hace falta todo, pero cuanto más, menos preguntas):

- [ ] Link al Instagram y a la web
- [ ] El logo en PNG con fondo transparente (ideal: una versión para fondo oscuro y otra para claro)
- [ ] Lista de precios o catálogo
- [ ] **Capturas de cómo le contestás a clientes** por WhatsApp o mail (es lo que mejor muestra el tono)
- [ ] 10 preguntas que te hacen siempre, como te las escriben
- [ ] 3 cuentas que te gusten (cómo se ven o cómo hablan)
- [ ] Cualquier documento técnico del rubro (reglamentos, fichas, manuales)

Los siete bloques:

| # | Bloque | Qué te pregunta | Qué deja escrito |
|---|---|---|---|
| 1 | Negocio | Qué hacés, la promesa, qué te diferencia, **qué no se dice nunca**, el CTA | `Brief`, `Catálogo`, `Números`, `Objetivos` |
| 2 | Audiencias | A quién le vendés, qué te preguntan antes de comprar | `Personas`, `Recorrido del cliente`, la matriz |
| 3 | **Tono** | Casi nada: lo saca de tus mensajes reales | `Tono de voz` |
| 4 | **Design system** | El logo y los colores | `marca.json` (paletas), el muestrario exportado |
| 5 | Conocimiento | Qué cosas técnicas se explican siempre, quién las confirma | `Empresa/Conocimiento/` |
| 6 | **Módulos** | ¿Historias? ¿Video? ¿Alguien a cámara? ¿Qué redes? | `marca.json` (modulos) |
| 7 | Cierre | — | Un carrusel de prueba |

### Cómo se define el tono

**El tono no se define con adjetivos** ("cercano, profesional, divertido" se puede decir de cualquiera).
Se define así:

1. **Le pasás cómo hablás de verdad:** capturas de WhatsApp con clientes, pies que te gustaron de tu
   cuenta, un audio transcrito. Claude anota el trato (vos, tú, usted), el largo de las frases, las
   palabras que repetís, los emojis, cómo saludás y cómo cerrás
2. **Te propone** una línea ("como te lo explicaría un amigo que trabaja acá"), cuatro rasgos con su
   contrario (somos *cercanos*, no *chabacanos*), las palabras tuyas y las prohibidas
3. **La prueba de los tres pies:** escribe el mismo pie en tres versiones (más cercana, del medio, más
   sobria) y elegís cuál suena a vos y qué le cambiarías. **Eso define el tono más que cualquier
   respuesta**
4. Queda en `Empresa/Marca/Tono de voz.md`, con una sección fija, **Que no suene a IA**, que vale para
   cualquier marca: sin guion largo (—), sin "descubrí", sin preguntas retóricas en cadena, sin remates
   motivacionales. `revisar-texto.py` lo chequea solo en cada pie

**El tono se sigue afinando solo:** cada vez que corregís un pie, la corrección se suma a *Correcciones
que ya se hicieron*, y la próxima pieza no repite el error.

### Cómo se define el design system

**Todo el diseño sale de un solo archivo: `Empresa/Marca/marca.json`.** No se toca CSS.

1. **El logo:** dos PNG en `Empresa/Marca/logos/` con estos nombres exactos:
   `logo-fondo-oscuro.png` (el que se lee sobre oscuro) y `logo-fondo-claro.png`. Borrá el archivo
   `BORRAR-ESTO-al-poner-los-logos-reales.txt`
2. **Las paletas:** cuatro, de una sola familia de color cada una (una de todos los días, una para
   alternar, una clara, una oscura). Cada una tiene tres tipos de lámina: **base** (la mayoría),
   **clara** (una o dos, para cortar el ritmo) y **golpe** (una sola, la que más importa). Claude las
   arma desde los colores de tu logo y tu web y chequea que se lean
3. **Aplicar:** `python Áreas/Contenido/herramientas/aplicar-marca.py`. Genera los estilos, chequea el
   contraste (dice MAL si un texto no se lee) y avisa qué falta
4. **Ver cómo queda:** exportar el muestrario
   `python .claude/skills/carrusel/render.py "Áreas/Contenido/Templates/Muestrario carrusel/01-demo-elementos"`
   y abrir las PNG. Se ajusta en `marca.json` hasta que guste
5. **Las letras:** el sistema trae un kit (Switzer, Poppins, Caveat, Bricolage, Instrument Serif). Si
   tu marca usa otras, pedile a Claude "cambiá la letra de títulos por X": la skill `design-system`
   sabe dónde va cada cosa

Lo que **no** cambia entre marcas (y es lo que hace que funcione): una paleta por pieza, títulos
enormes, una sola lámina de golpe, la firma con el logo abajo a la izquierda, tres formas de poner
una foto.

### Elegir si querés historias (y los demás módulos)

En el bloque 6, Claude pregunta y deja la respuesta en `marca.json` → `modulos`:

```json
"modulos": { "historias": true, "video": true, "linkedin": false, "tiktok": false, "facebook": true }
```

| Módulo | Si está en `true` | Si está en `false` |
|---|---|---|
| `historias` | El plan lleva un recorrido de historias por semana (la mayoría juegos) y `/historias` las arma | La skill se mueve a `.claude/_desactivadas/` y nadie propone historias |
| `video` | El plan propone reels y `/editar-video` los edita | El mes se arma con carruseles; no hace falta instalar FFmpeg ni Node |
| `linkedin` | 2-3 piezas por mes para empresas, como PDF | No se proponen |
| `tiktok`, `facebook` | El mismo video y el mismo pie que Instagram | No se mencionan |

**Para activar historias después:** pedile a Claude "activá historias" (vuelve la carpeta a
`.claude/skills/historias/` y pone `true`). **Para desactivarlas:** "desactivá historias".

**¿Conviene?** Las historias no traen gente nueva: hacen que la que ya te sigue confíe, juegue y te
escriba. Suman unos 20 minutos por semana. Si recién arrancás y solo podés con una cosa, empezá sin
historias y sumalas al segundo mes.

---

## Paso 3 · Cargar el material (lo que tarde)

**Fotos y videos reales en `Áreas/Contenido/Material/`.** El sistema no usa fotos de stock ni video
generado con IA: muestra lo que es tuyo.

- **La forma fácil:** tirá todo en `Material/desordenado/` y pedile a Claude **"ordená el material"**.
  Lo mira, le pone un nombre que dice lo que se ve, lo reparte por tema y arma el inventario
- **Lo que más se usa:** fotos horizontales con buena luz, el lugar, las manos haciendo lo que hacés,
  el producto de cerca, el equipo trabajando
- **Caras de clientes, solo con permiso escrito**

---

## Paso 4 · Pasar inspiración: `/adaptar-inspiracion`

**Cuando veas un reel o un carrusel que te gusta, pasáselo a Claude.** Cualquiera de estas formas:

```
/adaptar-inspiracion https://www.instagram.com/reel/XXXXXXX
me gusta cómo arranca: el error más grande al final y lo anuncia en el segundo 2
```

- **El link** (Claude lo abre con el navegador; si pide iniciar sesión, iniciás vos)
- **Capturas** de cada lámina o de los momentos del reel, adjuntas o en `Inspiración/entrada/`
- **El video descargado**, en `Inspiración/entrada/`
- **Tu descripción**, si no tenés nada más

Y una línea de **qué te gustó**: el gancho, el ritmo, el diseño, el tema.

**Qué hace Claude:**

1. **La desarma:** el gancho exacto y qué fórmula es (hay 26 catalogadas), qué se ve en el segundo 0,
   la estructura lámina por lámina o corte por corte, el ritmo, los recursos (subrayado, lista, ✓/✗),
   el pilar y, si se ven las vistas, cuánto le rindió a esa cuenta contra su promedio
2. **Te dice qué se toma y qué no:** se toma la estructura, el ritmo, el ángulo; **nunca** el texto, el
   audio, las imágenes, el diseño ni los datos sin verificar
3. **Escribe la tuya**, completa: para qué audiencia, en qué formato (un reel se puede volver
   carrusel y al revés), el gancho, las láminas o las frases, el pie, qué tomas hacen falta
4. **Te pregunta a dónde va:** al banco de ideas para otro mes, al plan de este mes, o a producir ya

**Una tanda de Guardados de Instagram** es la mejor inspiración que hay: pasá varias juntas y Claude
además te dice qué se repite entre ellas.

Al cerrar el mes, el reporte compara las piezas adaptadas contra las propias, para saber si vale la pena.

---

## Paso 5 · El primer mes

| Cuándo | Escribís | Qué pasa |
|---|---|---|
| Antes de empezar | (exportás los números) | Meta Business Suite → Estadísticas → Contenido → últimos 90 días → Exportar. Guardá el .csv en `Empresa/Datos y feedback/Crudos/` como `aaaa-mm-instagram.csv` |
| Última semana del mes | `/investigar-contenido` | Mira qué te funcionó (con números), qué le funciona a la competencia y a cuentas vecinas, y deja qué repetir, qué probar y qué dejar |
| Justo después | `/plan-mensual-contenido` | Te pregunta qué te inspira este mes, te propone 15-18 ideas, elegís, y escribe pieza por pieza: gancho, pie listo para pegar, láminas o frases, tomas |
| Antes de cada fecha | `/carrusel pieza 3` | Elige el tipo, te muestra las láminas antes de diseñar, exporta las PNG y deja el `Publicar.md` |
| | `/editar-video pieza 4` | Con los clips en `Material/Piezas/aaaa-mm/04-tema/`: propone los cortes, te muestra 15 segundos, arma el video, la portada y el `Publicar.md` |
| | `/historias fila 2` | Arma el recorrido con el lugar de cada sticker y qué poner en cada uno |
| El día del plan | (publicás a mano) | Abrís el `Publicar.md` de la pieza: pie, hashtags, música, portada. Copiar y pegar |
| El día 1 | `/reporte-contenido` | Qué se publicó, cómo rindió cada pieza, qué queda para el mes siguiente |

**Cada pieza tiene un número** en el plan, y ese número es el de su carpeta en `outputs/`.

---

## Qué hay en la carpeta

```
sistema-contenido-ia/
├── CLAUDE.md            las reglas que Claude lee siempre (no inventar, dónde está cada dato)
├── GUIA.md              esta guía
├── Plan.md              lo pendiente y las preguntas, en un solo lugar
├── Empresa/             LA VERDAD DEL NEGOCIO (lo llena /configurar-marca)
│   ├── Brief.md             qué es, qué se promete, qué NO se dice nunca
│   ├── Catálogo.md          productos y precios
│   ├── Personas.md          audiencias y sus dolores, en sus palabras
│   ├── Números.md           toda cifra, con fecha y fuente
│   ├── Objetivos.md         qué se quiere mover y cuánto se puede producir
│   ├── Recorrido del cliente.md
│   ├── Competencia.md       cuentas para mirar
│   ├── Conocimiento/        la base técnica del rubro: todo dato que se afirma, con fuente
│   ├── Datos y feedback/Crudos/   los exports de Instagram
│   └── Marca/
│       ├── Manual de marca.md   la marca entera
│       ├── Tono de voz.md       cómo se escribe
│       ├── marca.json           LA FICHA: cuenta, CTA, hashtags, prohibidos, paletas, letras, módulos
│       └── logos/               los dos PNG del logo
├── Áreas/Contenido/
│   ├── Contenido.md         la guía del área: matriz, mezcla, el mes paso a paso
│   ├── Banco de ideas.md    la materia prima
│   ├── Inspiración/         lo que viste afuera y se adaptó
│   ├── Material/            tus fotos y videos (no va a git)
│   ├── Investigación/ · Plan mensual/ · Reportes/ · outputs/     lo que se produce cada mes
│   ├── Templates/           lo que abren las skills (estilo, tipos de carrusel, fórmulas de gancho…)
│   └── herramientas/        scripts y fuentes
└── .claude/skills/          las nueve skills
```

**Las nueve skills:**

| Skill | Para qué |
|---|---|
| `configurar-marca` | Cargar o cambiar la marca: negocio, audiencias, tono, diseño, conocimiento, módulos |
| `design-system` | Cómo se definen y cambian colores, logo y letras (la usan las demás) |
| `adaptar-inspiracion` | Convertir un reel o carrusel de otra cuenta en una pieza tuya |
| `investigar-contenido` | Qué funcionó en tu cuenta y afuera, con números |
| `plan-mensual-contenido` | El plan del mes, pieza por pieza |
| `carrusel` | Diseñar y exportar un carrusel |
| `editar-video` | Editar un reel desde los clips del celular |
| `historias` | Un recorrido de historias con juegos (opcional) |
| `reporte-contenido` | Cómo rindió el mes |

---

## Las reglas que sostienen todo

1. **No se inventa nada.** Precios de `Catálogo`, cifras de `Números`, datos técnicos de
   `Conocimiento`. Lo que falta queda `[CONFIRMAR con <quién>]` y va a `Plan.md`
2. **Lo que no se dice** está en `Brief.md` y en `marca.json` → `prohibido`. `revisar-texto.py` lo
   marca en cada pie
3. **Base vs. resultados:** lo de `Empresa/` se corrige y no lleva fecha; lo que se produce lleva
   fecha (`aaaa-mm`) y se acumula
4. **Los colores se cambian en `marca.json`**, nunca en el CSS
5. **Lo que se aprende se escribe:** en *Lo que ya sabemos* (Contenido.md), *Lo que ya decidimos*
   (Estilo de video) y *Correcciones* (Tono de voz). Así el sistema mejora en vez de repetir errores

---

## Problemas comunes

| Pasa esto | Es por | Se arregla |
|---|---|---|
| Las láminas salen con colores de ejemplo | No se corrió `aplicar-marca.py` | Correrlo después de cada cambio en `marca.json` |
| Sale "LOGO" en la firma | Están los logos de ejemplo | Poner los tuyos en `Empresa/Marca/logos/` con los nombres exactos |
| La firma dice `@tucuenta` | El `index.html` se copió sin cambiar la firma | Pedirle a Claude que la cambie por la de `marca.json` |
| `render.py` no encuentra Chrome | Falta Playwright o Chrome | `pip install playwright` |
| El video sale sin animaciones | Falta Node.js 22 | Instalarlo, o usar el motor simple (`"animado": false`) |
| Los subtítulos escriben mal un nombre | El transcriptor no lo conoce | Sumarlo a `vocabulario_transcripcion` y `correcciones_transcripcion` en `marca.json` |
| `revisar-texto.py` dice que faltan hashtags | Los de `marca.json` son de ejemplo | Poner los tuyos en `hashtags_marca` |
| Claude propone historias y no las querés | `modulos.historias` está en `true` | "Desactivá historias" |
