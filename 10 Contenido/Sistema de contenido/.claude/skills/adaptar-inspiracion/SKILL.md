---
name: adaptar-inspiracion
description: Toma un reel, carrusel o historia de otra cuenta que gustó (link, capturas, video o descripción), lo desarma (gancho, fórmula, estructura, ritmo, recursos) y lo convierte en una pieza propia con el tono, el diseño y los datos de la marca, lista para el plan o para producir. Usar cuando se pase inspiración, un link de Instagram o TikTok, capturas de un post, o se pida "hacé algo como esto", "adaptá este reel" o "quiero un carrusel así".
---

# Adaptar inspiración

**Convierte lo que viste afuera en una pieza tuya.** No copia: toma la estructura, el ritmo o el
ángulo, y todo lo demás (texto, dato, diseño, tono) es de la marca.

Produce **un archivo por adaptación**: `Áreas/Contenido/Inspiración/aaaa-mm-dd-tema.md`, con la ficha
de `Áreas/Contenido/Templates/Adaptación de inspiración.md`. Y, según lo que se decida, **una idea en el
banco**, **una pieza en el plan del mes** o **la pieza producida** con `/carrusel` o `/editar-video`.

---

## 0. Leer antes

1. `Empresa/Marca/Manual de marca.md` y `Empresa/Marca/Tono de voz.md`: lo de afuera se pasa a esto
2. `Empresa/Personas.md`: si la idea no toca un dolor de acá, no sirve, por linda que sea
3. `Áreas/Contenido/Contenido.md`: la matriz, para ubicar la idea en una celda
4. `Áreas/Contenido/Templates/Fórmulas de gancho.md` para nombrar el gancho
5. `Áreas/Contenido/Templates/Tipos de carrusel.md` y `Estilo de video.md` para traducir el formato
6. `Áreas/Contenido/Inspiración/Inspiración.md`: lo ya adaptado, para no repetir
7. `Empresa/Marca/marca.json` → `modulos`: si `video` es `false`, un reel se adapta a carrusel

## 1. Recibir la inspiración

Puede llegar de cuatro formas. **Se trabaja con la que haya, sin pedir las otras:**

| Llega | Qué hacer |
|---|---|
| **Link** de Instagram, TikTok, YouTube | Abrirlo con el navegador (el integrado; si no, Claude in Chrome). Mirar la pieza entera: en un carrusel, cada lámina; en un reel, pausar en cada corte y anotar el texto en pantalla y el segundo. Leer el pie. Mirar la grilla de la cuenta para calcular la mediana de vistas. Si pide iniciar sesión, pedir que se inicie en el navegador con una cuenta personal. **Nunca se piden credenciales** |
| **Capturas** (en el chat o en `Inspiración/entrada/`) | Mirar cada una en orden |
| **Video descargado** en `Inspiración/entrada/` | Sacar un cuadro por segundo con `ffmpeg -i video.mp4 -vf fps=1 cuadro-%02d.jpg` en una carpeta de trabajo (no en `Material/`) y mirarlos. Si tiene voz, transcribirla con faster-whisper. El video original no se usa en ninguna pieza |
| **Una descripción** | Trabajar con eso, y decir qué no se pudo ver |

**Si no dijo qué le gustó, se pregunta en una línea** ("¿qué te gustó: el gancho, el ritmo, el
diseño o el tema?"), salvo que sea obvio. Ayuda a no adaptar lo que no importa.

**Varias inspiraciones juntas** (por ejemplo, una tanda de Guardados): una ficha por pieza, y al final
un resumen de qué se repite entre ellas.

## 2. Desarmarla

Llenar la sección 2 de la ficha, **con lo que se ve, no con lo que se supone**:

- El **gancho en pantalla** tal cual, la **primera línea del pie**, y **qué fórmula** es (número de
  `Fórmulas de gancho.md`). Si no entra en ninguna, "nueva" y se describe el molde
- **Qué se ve en el segundo 0** (o la portada): ¿se mueve? ¿hay una cara? ¿cuántas palabras?
- **La estructura**, lámina por lámina o corte por corte, con los segundos
- **El ritmo:** segundos por toma, cuándo entrega lo que prometió el gancho
- **Los recursos visuales**, traducidos a lo que tiene el sistema: subrayado, lista que aparece, ✓/✗,
  número enorme, foto a media lámina, tachado. **Si usa algo que el sistema no tiene, se dice**
- **El pilar** que cumple en nuestra matriz y **qué acción busca**
- **El múltiplo**, si se ven las vistas: vistas de la pieza sobre la mediana de la cuenta. Más de 2x
  es una señal; menos de 1,5x, un día normal. **Una pieza linda que no le funcionó a nadie se adapta
  igual si gustó, pero se dice que no hay evidencia**

## 3. Decidir qué se toma

Tabla de la sección 3: **qué se toma, qué no, y por qué.** Siempre:

- **Se toma:** estructura, ritmo, ángulo, fórmula del gancho, recursos visuales
- **No se toma nunca:** el texto tal cual, el audio, las fotos o el video, el diseño (colores,
  letras), los datos sin verificar, las promesas que la marca no puede hacer (`Empresa/Brief.md`,
  *Lo que NO se dice*)
- **Si la idea pide algo que no hay** (un dato que no está en `Empresa/`, una toma que no está en
  `Material/`, alguien a cámara), se dice: o se consigue, o se adapta a lo que hay

**Presentarlo en un mensaje corto antes de escribir la pieza:**

```
De: @cuenta · reel · 1,2 M vistas (4x su mediana)
Fórmula: #11 Lista con favorita · Pilar: Autoridad
Lo que la hace funcionar: el peor error va último y se anuncia en el segundo 2
Tomamos: la estructura de 3 errores + el anuncio · el texto que aparece con cada corte
No tomamos: el dato del 80% (sin fuente) · el audio
La nuestra: Audiencia 1 · Autoridad · Frases, 15 s (o Carrusel tipo Lista, 6 láminas)
Hace falta: 3 tomas de Material/Videos/Lugar (están) · confirmar el error 3 en Conocimiento
```

Se elige el **formato nuestro**: un reel se puede adaptar a reel (Frases, Info, Inspiración, A
cámara) o a carrusel; un carrusel, a carrusel o a reel de Frases. Si hay dos que andan, se proponen
los dos y se elige.

## 4. Escribir la nuestra

Sección 4 de la ficha, **completa y lista para producir**, con las mismas reglas que una pieza del plan
(`.claude/skills/plan-mensual-contenido/SKILL.md`, fase 3):

- Audiencia, pilar, producción, formato y tipo
- Gancho con su fórmula, en pantalla seis palabras o menos
- Las láminas escritas (con el esqueleto de su tipo) o las frases/el guion del video (con la ficha de
  video), con lo que va en color
- El pie completo, pasado por `revisar-texto.py --texto "..."`
- Las tomas o fotos: primero las que ya están en `Material/`
- Los datos a confirmar → `Plan.md`

**La prueba antes de mostrarla:** si se pone al lado de la original, ¿alguien diría que es una copia?
Si sí, falta cambiar más (el ángulo, el ejemplo, el orden). ¿Suena a la marca o a la otra cuenta?

## 5. A dónde va

Preguntar en una línea, con la recomendada primero:

1. **Al banco de ideas** (en su celda, con `(✨ inspiración aaaa-mm-dd)`): para un mes que viene
2. **Al plan del mes**, como pieza nueva o en lugar de una que no se produjo: se agrega con el número
   que sigue y en el calendario
3. **Producirla ya:** se sigue con `/carrusel` o `/editar-video` usando la pieza escrita

Siempre, además:

- Fila en *Adaptaciones hechas* de `Inspiración/Inspiración.md`
- Si la cuenta no estaba, a `Empresa/Competencia.md`, en su grupo
- Si la fórmula era nueva, a *Fórmulas nuevas* de `Fórmulas de gancho.md`
- Si es un video que sirve de referencia de ritmo, a *Videos de referencia* de `Estilo de video.md`

## Reglas que no se rompen

- **No se copia.** Ni el texto, ni el audio, ni las imágenes, ni el diseño
- **No se nombra ni se critica a la cuenta original** en lo que se publica
- **Ningún dato se traslada** sin verificar contra `Empresa/`
- **Es leer, no raspar:** se miran pocas piezas, a ritmo de persona. Nada de bajar en lote
- **Al cerrar el mes, el reporte compara** las piezas adaptadas contra el resto: así se sabe si vale la pena
