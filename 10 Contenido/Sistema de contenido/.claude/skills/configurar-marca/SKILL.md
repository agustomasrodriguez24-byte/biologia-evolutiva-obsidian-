---
name: configurar-marca
description: Carga una marca nueva en el sistema de contenido — negocio, audiencias, tono de voz, design system (paletas, letras, logo), base de conocimiento y qué módulos se usan (historias, video, LinkedIn) — en una conversación por bloques, y deja todo escrito en Empresa/ y en marca.json. Usar al instalar el sistema, cuando se pida definir o cambiar el tono, los colores, el logo o la marca, o activar o desactivar historias.
---

# Configurar la marca

**Es la primera skill que se corre y la única que escribe los documentos base desde cero.** Las demás
leen lo que esta deja. Si se corre de nuevo con la marca ya cargada, **no se pisa nada**: se pregunta
qué bloque se quiere cambiar y se trabaja solo ese.

**Es conversacional, por bloques.** Cada bloque se pregunta, se escribe, se muestra y se aprueba
antes de pasar al siguiente. Nunca se manda un cuestionario de cuarenta preguntas de golpe: se
contesta mal y se corrige todo dos veces.

| # | Bloque | Deja | Tiempo |
|---|---|---|---|
| 1 | El negocio | `Empresa/Brief.md`, `Catálogo.md`, `Números.md`, `Objetivos.md` | 10 min |
| 2 | Las audiencias | `Empresa/Personas.md`, `Recorrido del cliente.md`, la matriz en `Contenido.md` | 10 min |
| 3 | El tono | `Empresa/Marca/Tono de voz.md`, `prohibido` en `marca.json` | 15 min |
| 4 | El design system | `paletas`, `fuentes` y logos en `marca.json`, `Manual de marca.md` sección 5 | 15 min |
| 5 | El conocimiento | `Empresa/Conocimiento/` | 10 min + lo que se cargue |
| 6 | Módulos y canales | `modulos` en `marca.json`, canales en `Contenido.md` | 5 min |
| 7 | Cierre | `aplicar-marca.py`, un carrusel de prueba, `Plan.md` | 5 min |

Se puede hacer en una sesión o en varias: al arrancar, mirar qué bloques ya están (los archivos sin
`{{`) y seguir desde el primero que falte.

---

## 0. Antes de preguntar nada

1. Leer `CLAUDE.md` y `Empresa/Marca/marca.json` para saber qué ya está cargado
2. **Pedir material antes que respuestas.** En el primer mensaje, una sola vez:

   > Para arrancar, pasame lo que tengas (no hace falta todo):
   > - El link a tu Instagram y a tu web
   > - Tu logo (PNG con fondo transparente, si tenés)
   > - Algún documento que ya exista: lista de precios, presentación, brief, manual de marca
   > - Capturas o textos de cómo le contestás a clientes (WhatsApp, mails): **es lo que mejor
   >   muestra tu tono**
   > - 3 cuentas que te gusten como se ven o como hablan (de tu rubro o no)

3. Con lo que llegue, **completar todo lo posible antes de preguntar**: la web y el Instagram dicen
   el rubro, los servicios, el tono que ya usa, los colores. Si hay navegador, mirarlos. Las preguntas
   son para lo que no se puede deducir
4. **No se inventa nada.** Lo que no se sabe queda `{{...}}` o `Falta el dato` y va a `Plan.md`

## 1. El negocio

Preguntar en un solo mensaje, corto:

1. ¿Qué hacés, para quién y dónde? (una frase)
2. ¿Qué es lo único que te comprometés a cumplir siempre? (la promesa)
3. ¿Qué te diferencia, con algo que se pueda probar? (años, clientes, reseñas, algo que nadie más hace)
4. ¿Qué **no** se puede decir nunca? (promesas que no se cumplen, descuentos internos, temas sensibles)
5. ¿Cuál es el único CTA? (WhatsApp, link, DM) y el número o usuario
6. ¿Qué querés que logre el contenido este trimestre? ¿Quién escribe, quién filma, quién publica?

Escribir `Brief.md`, `Objetivos.md`, lo que se pueda de `Catálogo.md` (precios **solo si los dio**) y
`Números.md` (cada número con su fuente). Completar en `marca.json`: `nombre`, `cuenta`, `descriptor`,
`rubro`, `ciudad`, `cta`, `hashtags_marca` (tres: marca, rubro, ciudad o similar), y cada ítem de *Lo
que NO se dice* como `prohibido` (un `patron` regex en minúsculas y su `motivo`).

## 2. Las audiencias

1. ¿A quién le vendés? Si hay más de un tipo de cliente, ¿cuáles? (dos o tres como mucho)
2. Para cada uno: **¿qué te dicen o preguntan antes de comprar, tal cual lo escriben?** Pedir
   mensajes reales si los hay: de ahí salen los dolores y los ganchos
3. ¿Cuál de esas audiencias te gustaría que te compre más y hoy casi no le hablás?

Escribir `Personas.md` (con las frases tal cual) y `Recorrido del cliente.md`. En `Contenido.md`:
nombres de las audiencias en la matriz, una línea por celda, y la mezcla del mes ajustada al volumen
real de `Objetivos.md`. **La audiencia que menos contenido tiene queda marcada "nunca cero".**

## 3. El tono

**El tono no se pregunta en abstracto** ("¿sos formal o informal?" no sirve). Se saca de cómo habla
la marca de verdad y se confirma con ejemplos.

1. **Leer** los mensajes, pies y textos que pasó. Anotar: trato (vos, tú, usted), largo de frase,
   palabras que repite, emojis, cómo saluda, cómo cierra
2. **Proponer** en un mensaje: la línea "En una línea", cuatro rasgos de personalidad con su
   contrario (para el `Manual de marca.md`, sección 3), las palabras nuestras y las prohibidas
3. **La prueba de los tres pies:** escribir el mismo pie corto en tres versiones (más cercana, la del
   medio, más sobria) sobre un tema real del negocio, y preguntar cuál suena a la marca y qué
   cambiaría. **La elegida y sus correcciones definen el tono**, más que cualquier respuesta
4. Escribir `Tono de voz.md`: *En una línea*, *La semilla* (tres párrafos con el arco del cliente),
   *Las reglas*, *Palabras nuestras*, *Lo que no hacemos* con ejemplos del rubro. **La sección *Que no
   suene a IA* no se borra ni se afloja.** En *Chequeo rápido*, el nombre de alguien del equipo
5. Si el idioma o el trato no son español rioplatense con voseo, cambiar `idioma` y `trato` en
   `marca.json` y avisar que los ejemplos de las skills están en voseo pero se escriben en el trato
   de la marca
6. Llenar la columna *Ejemplo de tu marca* de `Templates/Fórmulas de gancho.md` en las 10 fórmulas
   más útiles para el rubro (las del pilar Autoridad y Espejo primero)

## 4. El design system

Leer `.claude/skills/design-system/SKILL.md`: tiene el método completo. En corto:

1. **Logo:** pedir dos PNG con fondo transparente, uno para fondo oscuro y uno para fondo claro.
   Guardarlos como `Empresa/Marca/logos/logo-fondo-oscuro.png` y `logo-fondo-claro.png`, recortados
   sin aire alrededor, y **borrar el aviso `BORRAR-ESTO…`**. Si solo hay uno, hacer la otra versión
   (blanco o negro) solo si es un logo de un color; si no, pedirla
2. **Colores:** sacar los de la marca (logo, web, local). Proponer **cuatro paletas** de una sola
   familia cada una, con los ocho colores de `marca.json` (base, tinta, acento, clara, tinta clara,
   acento claro, golpe, tinta golpe), **chequeando el contraste** (texto sobre fondo, 4,5:1 como mínimo)
3. **Letras:** por defecto queda el kit que trae el sistema. Si la marca tiene las suyas, seguir el
   paso *Cambiar una letra* de `design-system`
4. Correr `python Áreas/Contenido/herramientas/aplicar-marca.py`, exportar el muestrario
   (`python .claude/skills/carrusel/render.py "Áreas/Contenido/Templates/Muestrario carrusel/01-demo-elementos"`)
   y **mostrar las láminas** antes de dar el bloque por cerrado. Se ajusta hasta que guste
5. Escribir la sección 5 del `Manual de marca.md` (logo, tabla de paletas, letras, qué fotos sí y no)

## 5. El conocimiento

1. ¿Qué cosas técnicas de tu rubro se explican siempre? ¿Qué te preguntan que la gente tiene mal?
2. ¿Hay documentos oficiales, manuales, reglamentos, fichas técnicas? Pedirlos
3. ¿Quién del equipo confirma un dato técnico antes de publicarlo?

Armar `Empresa/Conocimiento/` con un archivo por tema desde `_plantilla-tema.md`, **cada afirmación
con su fuente**. Lo que se dijo en la conversación sin documento va con "Fuente: {{nombre}}, dd/mm/aaaa".
La sección *Para contenido* de cada tema alimenta el banco de ideas.

## 6. Módulos y canales

Preguntar con opciones, en un solo mensaje:

1. **¿Querés historias?** Un recorrido por semana, la mayoría juegos (encuestas, quiz, mito o
   realidad). Suma unos 20 minutos por semana entre armar y subir. Si es que no, se desactiva y
   ninguna skill las propone
2. **¿Querés videos?** Necesita instalar FFmpeg, Node.js y faster-whisper (una vez). Sin video, el
   mes se arma con carruseles
3. **¿Hay alguien que pueda poner la cara a cámara?** Si no, solo short simple
4. **¿Qué canales?** Instagram siempre; Facebook, TikTok, LinkedIn (solo si vendés a empresas)

Escribir `modulos` en `marca.json` y la tabla de canales en `Contenido.md`.

**Si historias queda en `false`:** mover `.claude/skills/historias/` a `.claude/_desactivadas/historias/`
y `Templates/Muestrario historias/` a `.claude/_desactivadas/` (con `mv -n`). Así no aparece en la
lista de skills. **Para activarla después:** volver a moverla a `.claude/skills/historias/` y poner
`"historias": true`. Las demás skills leen `modulos` y se adaptan solas.

## 7. Cierre

1. Correr `aplicar-marca.py` y mostrar su salida: tiene que decir *La ficha está completa*, o listar
   lo que falta
2. **Un carrusel de prueba:** con `/carrusel`, un carrusel corto (4 láminas) sobre un tema real del
   banco de ideas. Es la prueba de que tono + diseño + conocimiento funcionan juntos
3. Lo que quedó sin resolver → `Plan.md`, por persona
4. En `Contenido.md`, *Estado*: el sistema configurado con la fecha
5. Decir el siguiente paso: cargar material en `Áreas/Contenido/Material/`, exportar los números de
   Instagram, y `/investigar-contenido` → `/plan-mensual-contenido`

## Reglas

- **Nada inventado:** ni precios, ni cifras, ni clientes, ni datos técnicos. `{{...}}` o `Falta el dato`
- **Un bloque por mensaje**, con lo escrito a la vista antes de seguir
- **El tono sale de ejemplos reales**, no de adjetivos
- **Los colores se cambian en `marca.json`**, nunca en `base.css` ni en un `index.html`
- **No se borra nada** de un documento ya cargado sin decirlo: se muestra qué cambia
