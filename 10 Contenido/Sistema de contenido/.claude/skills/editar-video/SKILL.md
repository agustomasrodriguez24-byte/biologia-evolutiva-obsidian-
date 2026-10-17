---
name: editar-video
description: Edita los videos verticales de la marca a partir de los clips del celular en sus cuatro tipos — frases (tomas con frases por corte seco), info (una toma con texto fijo), inspiración (lo mismo en serif, poético) y a cámara (cortes por lo que dice, subtítulos, zooms, insertos, capítulos) — con el gancho, los gráficos, las capas animadas, los efectos de sonido y la portada en el mismo estilo y paletas que los carruseles. Usar cuando se pida editar, cortar, subtitular o armar un reel, un short o un video de una pieza del plan o de una adaptación.
---

# Editar video

**Módulo opcional.** Si `Empresa/Marca/marca.json` → `modulos.video` es `false`, avisar y preguntar
si se quiere activar (necesita la instalación de abajo).

**La marca manda:** antes de producir, leer `Empresa/Marca/Manual de marca.md`.

Produce **una carpeta por video**: `Áreas/Contenido/outputs/aaaa-mm/videos/NN-tema/`, donde **NN es el
número de la pieza en el plan del mes**. Adentro: `edl.json` (la decisión de edición, lo que se
corrige), `video-1.mp4`, `video-2.mp4`… (las versiones), `portada.png`, `notas.md` y `Publicar.md`. Los
clips van en `Áreas/Contenido/Material/Piezas/aaaa-mm/NN-tema/` (el mismo nombre) y lo intermedio en `trabajo/`.

**El método es el de [tenfold](https://guides.tenfoldmarketing.com/video-edit), adaptado:** mirar los
clips, elegir las mejores tomas, escribir la lista de cortes, armar, revisar, corregir. Funciona en
Windows, transcribe en español, usa la marca de `marca.json`, y cubre también el short sin voz.

**Cuatro tipos** (la pieza del plan dice cuál) → `Templates/Estilo de video.md`, *Los cuatro tipos*:
**Frases** (`frases`), **Info** (`info`), **Inspiración** (`inspiracion`) y **A cámara** (`instructor`).

**Claude decide, el script ejecuta.** `Áreas/Contenido/herramientas/video.py` corta, encuadra, pega,
subtitula y mezcla. Qué toma va, dónde empieza y qué dice la placa lo decide Claude mirando las hojas de
contacto y la transcripción, y lo deja en `edl.json`. **La cuenta, las paletas y el logo los toma solo
de `marca.json`.**

---

## 0. Leer antes de cortar

1. **La pieza** en el plan del mes (o la ficha de `Inspiración/`): tipo de video, gancho, tomas, pie y
   **su ficha de video** (tipo, paleta, largo y el texto en pantalla ya escrito). El `edl.json` se arma
   con eso, **tal cual está en el plan**. Si la pieza no la trae, escribirla primero y mostrarla
2. `Áreas/Contenido/Templates/Estilo de video.md`: la marca en video, el formato de `edl.json` y cómo
   se filma
3. **Las decisiones que ya se aprobaron:** *Lo que ya decidimos* de `Estilo de video.md` y las
   `notas.md` de los últimos videos en `outputs/`. **Cada video arranca de ahí, no de cero**
4. `Empresa/Conocimiento/` si el video afirma algo técnico: **el dato sale de ahí, con su fuente**

**Una vez por máquina:** `ffmpeg` (Windows: `winget install Gyan.FFmpeg`; Mac: `brew install ffmpeg`),
`pip install playwright faster-whisper`, y **Node.js 22** (`winget install OpenJS.NodeJS.LTS`) para las
capas animadas. Después: `python Áreas/Contenido/herramientas/probar-instalacion.py` dice qué falta.

**Dos motores, y por defecto va el animado:**

| | Qué hace | Cuándo |
|---|---|---|
| **Animado** (`"animado": true`) | `video.py` corta, encuadra, subtitula y mezcla con FFmpeg, y **HyperFrames** pone encima el gancho, los gráficos, listas, ✓/✗, círculos y capítulos, cada uno con su efecto de sonido | **Siempre**, salvo que falle |
| **Simple** (sin `animado`) | Todo con FFmpeg, con las placas quietas | Si HyperFrames falla o no está Node. También la vista previa |

Si HyperFrames falla, la composición queda en `trabajo/hyperframes/index.html`: se mira con
`npx hyperframes preview` desde esa carpeta, se corrige y se vuelve a armar.

## 1. Juntar el material

1. Pedir que copien los clips en `Áreas/Contenido/Material/Piezas/aaaa-mm/NN-tema/` (el mismo nombre que
   la carpeta del video; `video.py` los busca ahí solo). Tomas de archivo, de `Material/Videos/`.
   **Audio grabado aparte** (.wav, .m4a, .mp3) va en esa misma carpeta: `preparar` lo sincroniza solo
   si se grabó al mismo tiempo (mirar la confianza en `trabajo/sincro.json`). Lo que no coincide con
   ningún clip es **voz en off** y va en el edl como `"voz"`. **Los clips originales no se tocan nunca**
2. Copiar `Templates/Notas de video.md` a `notas.md` y llenar el **brief** con la pieza
3. Música, solo si va en el video y no "elegida en IG al publicar": **solo con licencia**

## 2. Preparar y mirar

```
python Áreas/Contenido/herramientas/video.py preparar Áreas/Contenido/outputs/aaaa-mm/videos/NN-tema               # sin voz
python Áreas/Contenido/herramientas/video.py preparar Áreas/Contenido/outputs/aaaa-mm/videos/NN-tema --transcribir # con voz
```

Deja `trabajo/hojas/<clip>.jpg` (un cuadro cada tanto, con el segundo arriba) y, con `--transcribir`,
`trabajo/transcripcion.txt`. **Mirar cada hoja:** qué toma sirve, dónde está estable, qué tapa.

## 3. Decidir los cortes → `edl.json`

**Frases, info e inspiración** (sin nadie a cámara):

- **Largo:** frases 8-20 s (unos 3 s por frase); info e inspiración 5-10 s, una sola toma
- **El texto sale de la ficha del plan.** Frases de 4 a 10 palabras; info en 2-4 renglones con un
  `kicker`; inspiración en 2-4 versos. Una o dos partes en `resalta`, nunca más
- Tomas de 1,5 a 3 segundos. **El primer segundo es el más estable y más claro** de todo el material
- Frases puede llevar título (`gancho`), arriba todo el video, **seis palabras o menos**
- **El primer cuadro ya se mueve**
- Sin subtítulos ni audio original. Con voz en off: `voz` en el edl

**A cámara:**

- Leer la transcripción entera y **armar el guion con la mejor toma de cada frase** (casi siempre la
  última que se dijo completa). Si dos son iguales, la de mejor cuadro
- **Cortar justo:** `desde` = inicio de la primera palabra menos 0,1 s; `hasta` = fin de la última
  más 0,15 s. Sin silencios ni "eh"
- Título centrado (`gancho`, diseño `marcador`), los primeros 2-3 segundos
- Subtítulos siempre, **de a una palabra y centrados**; lo de `destacar` sobre el rectángulo de acento.
  Las palabras mal transcritas se corrigen en `"correcciones"` (y si se repiten en todos los videos,
  en `marca.json` → `correcciones_transcripcion`)
- **Sin placa de cierre**: el CTA va en el pie. Música baja (0,10-0,15), nunca encima de la voz

**Un gráfico** (`"graficos"`) muestra el dato cuando decirlo no alcanza. Uno por video alcanza.

**Antes de armar, mostrar el guion de cortes** en una tabla corta (n°, clip, de-a, qué se dice o qué
se ve). Se aprueba o se corrige. Es más barato que reeditar un video renderizado.

## 4. Armar y revisar

**Primero una vista previa corta**, después el video entero:

```
python Áreas/Contenido/herramientas/video.py armar   <proyecto> --vista-previa 15
python Áreas/Contenido/herramientas/video.py revisar <proyecto>
python Áreas/Contenido/herramientas/video.py armar   <proyecto>
python Áreas/Contenido/herramientas/video.py revisar <proyecto>
```

`armar` deja `video-N.mp4` (nunca pisa una versión) y guarda el `edl.json` de cada versión en
`trabajo/versiones/`. `revisar` deja `trabajo/revision.jpg`: un cuadro de cada corte y placa, con **lo
que tapa Instagram en rojo**. Chequear:

- [ ] Ningún texto ni cara importante en la zona roja
- [ ] El primer cuadro ya engancha: nada de arranque en negro ni toma movida
- [ ] Subtítulos fieles, sin `—`, con los nombres propios bien
- [ ] El gancho es el del plan, palabra por palabra, y **lo que promete se entrega antes de la mitad**
- [ ] Volumen entre -16 y -13 LUFS (lo dice `revisar`)
- [ ] Nada de lo prohibido, ningún precio sin verificar
- [ ] El gráfico se lee y explica, no decora

Corregir en `edl.json`, volver a `armar`. **No se edita a mano.**

### La portada

Cada video lleva `portada.png`: un cuadro del video arriba, a media pantalla, y el título enorme abajo
sobre el color de la paleta, con la firma de la marca. En el `edl.json`:

```json
"portada": {
  "titulo": "El título en 4-6 palabras",
  "resalta": "palabras",
  "kicker": "opcional, chiquito arriba",
  "sticker": "opcional",
  "clip": "Material/Piezas/aaaa-mm/NN-tema/toma3.mp4",
  "segundo": 4.2,
  "foto": "opcional: una foto en vez de un cuadro",
  "paleta": "la misma del video",
  "al_inicio": 0
}
```

```
python Áreas/Contenido/herramientas/video.py portada <proyecto>
```

**El cuadro:** una cara con expresión, las manos, el producto. Nunca un cuadro movido. Lo importante,
en el centro 3:4 (lo que muestra la grilla). **Se sube como portada** (Editar portada → Agregar desde
la galería).

**El video se mira en el celular, hasta el final.** Lo que se vea, se marca **con el segundo y qué
cambiar** ("0:06 el subtítulo más abajo"). Se anota en *Revisiones* de `notas.md`, se corrige en
`edl.json` y se vuelve a armar.

## 5. Al terminar

1. `Publicar.md` en la carpeta (pie pasado por `revisar-texto.py`, música, portada)
2. En el plan del mes: la ruta, qué `video-N.mp4` se aprobó y el estado a **Producida**
3. **Guardar lo que el próximo video tiene que heredar:** en `notas.md`, qué se aprendió; si es una
   regla para todos, a *Lo que ya decidimos* en `Estilo de video.md`. Si quedó como modelo, a *Videos
   propios que sirven de modelo*
4. Si se filmó una toma reutilizable, anotarla en `Banco de ideas.md`, sección 14
5. **Los .mp4 y el material no se suben a git** (pesan)
