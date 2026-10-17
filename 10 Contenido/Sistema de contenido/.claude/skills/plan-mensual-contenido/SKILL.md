---
name: plan-mensual-contenido
description: Arma el plan de contenido de todo un mes para la marca (Instagram, Facebook, TikTok y LinkedIn según los módulos activos) en una conversación de cuatro fases — de dónde arranca el mes, lista de ideas, pieza por pieza, documento final — con ganchos de las 26 fórmulas, pies listos para pegar, fichas de video, tipos de carrusel e historias. Usar a fin de mes para planificar el siguiente, o cuando se pida el calendario mensual, la grilla de contenido o el plan de redes.
---

# Plan mensual de contenido

**La marca manda:** leer `Empresa/Marca/Manual de marca.md` antes de proponer nada.

Produce **un** archivo: `Áreas/Contenido/Plan mensual/aaaa-mm.md`. Ese archivo es el que se ejecuta
durante el mes: de ahí sale lo que se filma, lo que se edita y lo que se programa.

**Es conversacional. No se arma el mes de una sola vez.** Cuatro fases, y cada una espera respuesta:

| Fase | Qué pasa | Quién decide |
|---|---|---|
| **1 · De dónde arranca el mes** | Se pregunta qué inspira este mes y qué ideas ya hay | El equipo |
| **2 · La lista de ideas** | Se propone una lista larga; se elige de ahí | El equipo, por número |
| **3 · Pieza por pieza** | Se escribe una pieza, se corrige, se pasa a la siguiente | Se aprueba cada una |
| **4 · El documento** | Se completa el archivo del mes | — |

**No se salta a la fase 2 sin haber preguntado la 1, ni se escriben las piezas todas juntas** (salvo
que se pida "generá todo": ver sección 9).

---

## 0. Leer antes de abrir la boca

1. `Empresa/Marca/marca.json`: **`modulos`** (historias, video, linkedin, tiktok, facebook), las
   paletas, los hashtags de marca, el CTA. **Lo que está en `false` no se propone**
2. `Empresa/Marca/Tono de voz.md`: cómo se escribe
3. `Áreas/Contenido/Contenido.md`: **la matriz**, la mezcla, las formas de producir, canales, fechas
4. `Áreas/Contenido/Banco de ideas.md`: **la materia prima.** La lista se llena de acá antes de inventar
5. `Áreas/Contenido/Inspiración/`: las adaptaciones que quedaron sin usar
6. `Empresa/Personas.md`: los dolores reales. **De acá salen los ganchos**
7. `Empresa/Recorrido del cliente.md`: cada fila con dolor es una idea
8. `Áreas/Contenido/Plan mensual/`: los dos meses anteriores (para no repetir y ver qué quedó sin hacer)
9. `Áreas/Contenido/Reportes/`: el reporte del mes que cierra
10. `Empresa/Objetivos.md`: qué se quiere mover y **cuánto se puede producir de verdad**
11. **`Áreas/Contenido/Investigación/`: el informe más nuevo.** Si no hay de este mes, antes de la fase
    1 preguntar si se corre `/investigar-contenido` primero. Se puede seguir sin él, pero se dice en la
    sección 1 del plan
12. `Empresa/Conocimiento/`: **todo dato técnico de una pieza sale de ahí, con su fuente**. La sección
    *Para contenido* de cada tema es fuente de ideas

La estructura del archivo final → `Áreas/Contenido/Templates/Plan mensual.md`. Precios, de
`Empresa/Catálogo.md`. **No se estiman.**

## 1. De dónde arranca el mes

**Primer mensaje: preguntar, no proponer.** Cinco preguntas cortas:

1. **¿Qué te inspira este mes?** Un tema, algo que viste, algo que está pasando en el negocio
2. **¿Qué ideas tenés ya?** Aunque estén a medias. Van primero, marcadas 💡
3. **¿Hay algo puntual?** Promoción, lanzamiento, fecha especial, un cliente con testimonio
4. **¿Cuánto se puede producir?** Concreto: si hay jornada de grabación y cuándo
5. **¿Qué formatos este mes?** Dar las opciones que permiten los módulos:
   - **a) Solo short simple**: video con texto en pantalla y la info en el pie (si `video` está activo)
   - **b) Sumar carruseles**
   - **c) Sumar piezas a cámara**: solo si hay jornada de grabación

**No adelantar ideas propias en este mensaje.** Sin respuesta, se asume el default de `Contenido.md` y
**se dice explícito en el plan**.

**La audiencia no es opcional en ningún paso.** Cada idea y cada pieza lleva su audiencia desde el
primer momento. Es lo que evita que el mes se arme solo con lo más fácil de escribir.

## 2. La lista de ideas del mes

**Una lista larga, no el plan cerrado:** un 50 % más de ideas que piezas (15-18 para elegir 8-11).

**Cómo se arma, en este orden:**

1. **Las ideas del equipo**, refinadas: con el gancho, la audiencia y el pilar. Marcadas 💡
2. **Lo que piden las fechas del mes** → `Contenido.md`
3. **Las adaptaciones de inspiración sin usar**, marcadas ✨
4. **El banco de ideas**, revisando que **no falte la audiencia que menos contenido tiene**. **Una idea
   `(✅ usada aaaa-mm)` reciente no se propone sin avisar**
5. **Lo que el reporte del mes anterior dijo que funcionó**, con otro tema
6. **Las recomendaciones del informe de investigación:** *Repetir* sube, *Probar* entra con 1-2 ideas,
   *Dejar de hacer* no se propone sin avisar. Marcadas 🔍

**Numerada y agrupada por celda, una línea por idea:**

```
### Audiencia 1 · Autoridad 🧭
1. 💡 "La pregunta que nos hacen todas las semanas" · Short simple · Info
2. ✨ "3 errores, el peor al final" (de la adaptación del 03/10) · Carrusel · Lista

### Audiencia 2 · Espejo 🪞
3. ...
```

Cada línea: **gancho en lenguaje de calle · forma de producir**. Si necesita un párrafo, no está lista.

**Cerrar el mensaje con:** qué mezcla queda si se eligen las recomendadas (contra la de referencia),
cuáles no se pueden hacer con la producción declarada y por qué, y la pregunta: cuáles van.

## 3. Pieza por pieza

**Una pieza por mensaje. Se escribe, se corrige, se aprueba, y ahí la siguiente.** Orden: las de a
cámara primero (definen la jornada de grabación), después el resto.

**Al arrancar la fase 3 se copia `Templates/Plan mensual.md` a `Plan mensual/aaaa-mm.md`** con
`**Estado del plan:** A confirmar`. Es el mismo archivo desde el principio: si la conversación se
corta, nada queda solo en el chat.

**Cada pieza completa, así** (los campos de la plantilla):

```
### Pieza 3 · 14/05 · Audiencia 1 · Autoridad · Short simple · Video 9:16

**Pilar de contenido:** Autoridad 🧭
**Título:** ...
**Gancho (fórmula 16), texto en pantalla:** "La pregunta tal cual" / remate corto
**Qué se ve:** ...
**Pie (IG · FB · TikTok):** el copy entero, listo para pegar
**Hashtags:** los de marca + 1-2 del tema
**Canales:** IG · FB · TikTok
**Video:** Frases · paleta alterna · 15 s
  Título: "..."
  Frases: 1) "... **palabra** ..." 2) "..." 3) "..."
  Canción: piano, elegida en IG
**Tomas necesarias:** la lista concreta
**Qué se necesita para producirla:** /editar-video
```

**Toda pieza dice su pilar**, y **el texto se escribe distinto según el pilar:**

| Pilar | Qué tiene que lograr el texto en pantalla y el pie |
|---|---|
| **Espejo** 🪞 | Que se sienta entendido. Deja ganas de seguir viendo contenido que "te entiende" |
| **Autoridad** 🧭 | Un dato de valor real, ya, más la promesa de que hay más |
| **Conexión** 🤝 | Que confíe en quién está del otro lado. Deja ganas de seguir a la cuenta |
| **Inspiración** 🌟 | Una frase que alguien quiera guardar o mandar. Concreta, de acá, sin citas de famosos. El pie cuenta por qué es cierta |
| **Oferta** 💸 | Un CTA concreto y nada más |

**Reglas de cada pieza, que se chequean antes de presentarla** (sin esperar a que se corrija lo mismo
dos veces):

- **El gancho sale de una fórmula** de `Templates/Fórmulas de gancho.md`, con su número, elegida por el
  pilar, **sin repetir fórmula en el mes**, priorizando las que el informe dijo que rindieron
- **El texto en pantalla es directo y corto**, como se habla. Dos líneas alcanzan. Seis palabras o
  menos en el gancho
- **El pie nunca queda como `____`.** Completo, listo para pegar, y **sonando humano** → `Tono de
  voz.md`, *Que no suene a IA*, y su *Chequeo rápido*
- **Todo pie trae valor real, también los de Espejo.** ¿Qué se lleva quien lo lee, aunque no escriba nunca?
- **El cierre del pie es una razón, no una orden** ("guardá este post" no)
- **Nada de guion largo (—)**, en ningún uso. Buscar el carácter antes de cerrar
- **Antes de presentarla, el pie pasa por** `python Áreas/Contenido/herramientas/revisar-texto.py --texto "..."`.
  Se corrigen las FALLAS y cada AVISO se decide. Los primeros 125 caracteres tienen que hacer tocar
- **Un solo pie para IG, FB y TikTok.** Solo LinkedIn se reescribe
- **Los hashtags de marca, todos** (los de `marca.json`), más 1-2 del tema
- **Toda pieza de carrusel dice su tipo** (de `Tipos de carrusel.md`) **y trae las láminas escritas**
  con el esqueleto de ese tipo, así `/carrusel` las diseña sin reordenar
- **Toda pieza de video trae su ficha completa** (tipo, paleta alternando, largo, todo el texto en
  pantalla marcado). `/editar-video` no inventa texto
- **Toda pieza lleva su lista de tomas**, mirando primero el banco, sección 14
- **Una pieza que viene de una adaptación** lleva la línea *Inspiración* con el archivo
- **Preguntar cuando falta el dato, en el momento.** No se estima y no se deja para después

**La pieza de Autoridad le habla también a quien todavía no es cliente.** Ese público no se gana con un
CTA duro: se gana recordándole, con naturalidad y en una línea variada, que esto se aprende o se
resuelve con la marca.

## 4. El documento final

El archivo ya existe desde la fase 3: acá se completa.

1. **Qué queremos mover este mes** y de dónde salió el mes
2. **El calendario**, una fila por pieza
3. **Las piezas escritas**, tal como se aprobaron
4. **Historias** (solo si `modulos.historias` es `true`): un recorrido por semana, la mayoría juegos →
   `Templates/Recorridos de historias.md`. Cada fila con número, recorrido y paleta. Si está en
   `false`, la sección se borra
5. **La lista de producción**, agrupada por jornada, con las tomas por pieza
6. **Resultado del mes**: vacío, se completa al cierre

## 5. Reparto por canal (según `modulos`)

| Canal | Qué va |
|---|---|
| **Instagram** | Todo. Es el canal principal |
| **Facebook** | Lo mismo que Instagram, priorizando lo que le habla a la audiencia mayor |
| **TikTok** | Solo el video vertical, con el mismo pie |
| **LinkedIn** | Solo empresas, 2-3 por mes: carrusel educativo, caso de un cliente empresa (con permiso), post de texto → `Tipos de carrusel.md`, *LinkedIn* |

## 6. Mezcla mensual

La de `Contenido.md`. **Un mes temático puede romperla**, y está bien, pero se dice en la sección 1 del
plan. **Lo que no se rompe nunca es el mínimo de la audiencia que menos contenido tiene.**

**Antes de cerrar la lista, contar cuántas piezas hay de cada pilar** y compararlo. Si un pilar quedó
en cero sin explicación, decirlo antes de la fase 3.

**Si se pide que "quede bien distribuido":** nunca dos Espejo seguidas; se alterna el dolor con lo
que se sabe o se puede comprobar. Si hay una semana de promoción, la pieza anterior baja la traba.

## 7. Reglas que no se rompen

- El trato de la marca. Frases cortas. El dato adelante
- **Nada de lo prohibido** (`Brief.md`, `marca.json` → `prohibido`)
- **Un solo CTA por pieza**, el de `marca.json` o uno concreto
- **Ningún cliente ni empresa se nombra** sin permiso confirmado
- **Los descuentos van con el monto de `Catálogo.md`** o marcados `[CONFIRMAR con <quién>]`. **Esto vale
  aunque alguien proponga un monto al pasar**: no se inventa, se marca y va a `Plan.md`
- Un dato que no está en `Empresa/` se marca `[CONFIRMAR con <quién>]` y va a `Plan.md`
- **La fila "Qué quiere" de `Personas.md` es el deseo del cliente, no un hecho de la marca**

## 8. Si cambia algo a mitad de camino

- **Cambia el total o el formato:** recalcular, decir **cuáles se cortan y por qué**, y recién seguir
- **Los ganchos están aburridos:** `/investigar-contenido` (o una pasada corta con el método), y el
  hallazgo al banco antes de seguir escribiendo
- **Llega una inspiración nueva:** `/adaptar-inspiracion` y, si se aprueba, entra como pieza
- **Aparece un canal que no estaba en `modulos`:** actualizar `marca.json` y `Contenido.md` en el momento
- **Se pide más texto en pantalla** para una pieza: se hace y se nota en la pieza

## 9. Si se pide "generá todo"

Se escriben todas las piezas juntas, completas. El plan queda en `A confirmar` y se avisa que falta la
revisión. **Las reglas de la sección 3 se aplican igual, pieza por pieza.**

## 10. Al terminar

1. `Plan mensual/aaaa-mm.md` completo, con `**Estado del plan:** Aprobado (dd/mm/aaaa)` cuando se da el OK
2. **Las ideas que quedaron afuera vuelven a `Banco de ideas.md`**
3. **Cada idea usada se marca `(✅ usada aaaa-mm)`** en el banco
4. Lo sin resolver → `Plan.md`
5. Recordar los estados (Planificada → Producida → Publicada → Medida) y que al cierre va
   `/reporte-contenido`
6. **La producción sigue en:** `/carrusel`, `/editar-video` y `/historias` (si está activo)
