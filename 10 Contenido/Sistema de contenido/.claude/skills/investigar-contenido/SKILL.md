---
name: investigar-contenido
description: Investiga qué funcionó en el Instagram de la marca y qué está funcionando en la competencia y en las cuentas de referencia, y lo deja como insumo del plan del mes con tres listas (repetir, probar, dejar de hacer) e ideas nuevas. Usar antes de /plan-mensual-contenido, cuando se pida investigar la cuenta, ver qué rindió, mirar a la competencia, buscar tendencias o refrescar los ganchos.
---

# Investigar contenido

**La marca manda:** leer `Empresa/Marca/Manual de marca.md` antes de recomendar nada.

Produce **un** archivo: `Áreas/Contenido/Investigación/aaaa-mm.md`, con la estructura de
`Templates/Informe de investigación.md`. Y **alimenta dos documentos base**: `Banco de ideas.md` (ideas
nuevas, marcadas 🔍) y *Lo que ya sabemos* de `Contenido.md` (solo lo que tiene evidencia).

**Para qué existe:** que el plan del mes salga de lo que de verdad funcionó, no de la intuición. **Se
corre una vez por mes, la semana antes de armar el plan.** **Investiga, no planifica:** no escribe
piezas, deja la evidencia y tres listas.

---

## 0. Leer antes de arrancar

1. `Áreas/Contenido/Contenido.md`: la matriz. Todo hallazgo se traduce a una celda
2. `Áreas/Contenido/Templates/Investigación de contenido.md`: **el método**
3. `Áreas/Contenido/Investigación/`: el informe del mes anterior, para comprobar si lo recomendado se
   hizo y rindió
4. `Áreas/Contenido/Inspiración/Inspiración.md`: lo que se adaptó este mes (y si rindió)
5. `Banco de ideas.md`, sección 13 (ganchos), y `Empresa/Competencia.md`
6. `Empresa/Personas.md`: todo hallazgo se filtra contra los dolores reales
7. `Áreas/Contenido/Reportes/`: el reporte del mes que cierra, si está

## 1. Preguntar el foco, en un solo mensaje

1. **¿Hay algo puntual que quieras entender?** Un formato que no rinde, una celda floja, una cuenta
2. **¿Sumamos alguna cuenta para mirar?** Las de `Competencia.md` se miran siempre
3. **¿Profundidad?** *Rápida* (tu cuenta + 3 cuentas, ~20 min) o *completa*

Sin respuesta: completa, con foco en la audiencia que menos contenido tiene, y se dice en el informe.

## 2. Tu cuenta: qué funcionó

**Va primero y pesa más que todo lo demás:** es evidencia de tu propio público.

1. **Los números:** buscar en `Empresa/Datos y feedback/Crudos/` un `aaaa-mm-instagram.csv` (o `.json`)
   **de los últimos 7 días**. Si no hay, pedir **una sola cosa**: el export de Meta Business Suite
   (Estadísticas → Contenido → últimos 90 días → Exportar) guardado ahí. Mientras tanto, se sigue
   con lo de afuera
2. `python Áreas/Contenido/herramientas/analizar-instagram.py`: ordena, no opina. Top por compartidos y
   por tasa de guardado, el **múltiplo** de cada pieza, por formato, por día, por largo del pie
3. **Leer las 10 mejores y las 10 peores una por una** (el enlace está en la tabla) y anotar: celda,
   **qué fórmula de gancho** usó, formato, qué se ve en los primeros 2 segundos, si vino de una
   adaptación. **De acá salen los patrones**, no de las medianas solas
4. **3 a 5 patrones con la evidencia al lado** ("los carruseles de checklist se guardan el triple que
   los reels: 6,0% contra 2,0%, sobre 14 piezas"). **Con menos de 5 piezas, no es patrón: es anécdota**

**Qué se mide, en este orden de peso:** compartidos por alcance > tasa de guardado > comentarios >
múltiplo > likes.

**Mucho alcance y casi ningún seguidor nuevo no es un mal video: es el perfil que no convence.** Ahí
se pasa `Templates/Rúbrica de perfil.md`.

## 3. Competencia y referentes

**6 a 12 cuentas** de `Competencia.md`: directas, creadores del rubro, vecinas (otro rubro, el mismo
público) y del mismo rubro en otros países (solo formato). Mejor cuentas de hasta 10 veces tu tamaño.
**Y pedir que abran sus Guardados de Instagram**: es el material más filtrado que hay (cada uno se
puede pasar después por `/adaptar-inspiracion`).

**Cómo se mira, con el navegador** (el integrado; si no, Claude in Chrome):

1. Abrir `instagram.com/<cuenta>/reels/`: las vistas se ven en la grilla
2. Las **últimas 15-20 piezas** y la mediana de vistas a ojo
3. **Quedarse con las que superan 2x esa mediana**
4. Para cada una, la ficha del método: ángulo, gancho exacto, **número de fórmula**, formato, función
5. Si pide iniciar sesión, pedir que se inicie en el navegador. **Nunca se piden credenciales**

**Es leer, no raspar:** pocas cuentas, a ritmo de persona. **Al resumir, decir con cuántas piezas.**
**No se copia nada tal cual.**

## 4. Afuera: tendencias y el rubro

Con búsqueda web, en una pasada corta:

- **Ganchos y formatos vigentes** en el rubro (en el idioma de la marca y en inglés)
- **Audios en tendencia** del mes (solo el nombre)
- **Novedades del rubro**: reglas, datos, campañas. **Toda cifra con fuente y fecha**; lo confirmado
  va a `Empresa/Conocimiento/`
- **Fechas del mes que viene**

**Una vez por trimestre** (o cuando el punto 2 lo pida): puntuar el perfil con `Templates/Rúbrica de perfil.md`.

## 5. Las recomendaciones

El cierre del informe. Tres listas, cada ítem con la evidencia entre paréntesis:

- **Repetir:** formatos, celdas o ganchos que rindieron en tu cuenta
- **Probar:** lo que funciona afuera y no se probó acá, ya traducido a la matriz, a una forma de
  producir que exista, y **a un gancho nuestro, listo para usar**. Nunca "hacé un video como este"
- **Dejar de hacer:** lo que rindió peor de forma consistente

Y **5 a 10 ideas concretas** con gancho, audiencia, pilar y forma de producir.

**Se presenta el resumen antes de escribir en los documentos base.** Lo que se descarta no entra al banco.

## 6. Reglas que no se rompen

- **Ningún número sin fuente**
- **Lo que falló se escribe igual** que lo que funcionó
- **La competencia no se nombra en una pieza pública** ni se la critica
- Nada de lo prohibido de `Brief.md`, aunque una referencia lo haga
- Un dato que no se pudo confirmar → `Plan.md`

## 7. Al terminar

1. `Investigación/aaaa-mm.md` completo
2. Ideas aprobadas → `Banco de ideas.md` con `(🔍 investigación aaaa-mm)`. Ganchos → sección 13;
   fórmulas que no entran en ninguna → *Fórmulas nuevas*. Cuentas nuevas → `Competencia.md`
3. Patrones con evidencia de **tu** cuenta → `Contenido.md`, *Lo que ya sabemos*
4. Números nuevos (seguidores, medianas) → `Empresa/Números.md`, con fecha y fuente
5. Decir que el plan ya puede arrancar: `/plan-mensual-contenido`
