---
tipo: sistema
fecha_revision: 2026-10-03
---

# Reglas por tipo

Qué tiene que tener cada tipo de nota. Las plantillas de `90 Plantillas/` ya traen esta estructura.

- **Concepto / Mecanismo / Intervención**: definición, mecanismo, evidencia con nivel y fuente, qué NO sabemos, relaciones reales, debate. Intervención: *intervención → mecanismo propuesto → evidencia → riesgo → aplicación*.
- **Fuente**: tipo de fuente, nivel, afirmaciones principales (cada una enlazada a la nota donde se integró), metodología, población, limitaciones.
- **Protocolo**: objetivo, fundamento, intervención, dosis/frecuencia/duración (solo si hay evidencia), variables, métricas, riesgos, contraindicaciones, nivel de evidencia, fuentes. No hay protocolo sin fundamento.
- **Producto**: el conocimiento define la necesidad, nunca al revés. Cadena: necesidad → concepto → mecanismo → intervención/protocolo → producto → valor (texto → video). Separar evidencia del ingrediente / de la formulación / del producto específico / afirmaciones del fabricante (F). Pasa el filtro de [[Criterios de la tienda]] y recibe `estado_tienda`. `nivel_promesa` nunca supera la evidencia del producto específico. Ficha de valor: para qué sirve / cómo encaja en la biología / cómo usarlo / qué esperar y qué no / para quién no es. Claude recomienda un estado; decide el usuario.
- **Alimento**: se evalúa con [[Matriz de Cobertura Nutricional]] (densidad, digestibilidad, biodisponibilidad, utilización, de 1 a 5 según la rúbrica). La biodisponibilidad se registra por nutriente; el puntaje del alimento es un resumen. Cantidades de [[USDA - FoodData Central]] o de la tabla nacional, con FDC ID. El alimento (conocimiento) es distinto del producto (artículo de la tienda).
- **Órgano**: es el eje del mapa del cuerpo. Función · legos que necesita, en cuatro tipos (materiales, señales, condiciones, regulación), cada uno enlazado a su nota y con nivel · mecanismos · señales de que le falta algo (orientativo, nunca diagnóstico) · tips · alimentos · productos alineados · qué NO sabemos · valor para el mapa y preguntas del test. Ver [[Modelo Nutrición Evolutiva]] y [[Método de trabajo]].
- **Tesis** (`17 Información madre/`): síntesis de un gran tema. La verdad (lo que enseñan los maestros) · cómo lo enseña cada maestro · lo que hace el sistema · tips · productos · para explicarlo. Sin contrastes con la evidencia. Ver [[Información madre]].
- **Hábito** (`18 Sistema de salud/`): una semana del [[Sistema de salud Nutrición Evolutiva]]. Qué hacer · por qué (en simple y lo que enseñan los maestros) · órganos que lo reciben · cómo hacerlo · cómo explicarlo (contenido) · pregunta del test · texto para la web · productos alineados · cuidados. Se escribe desde la verdad de Agus y sus referentes, sin contrastes con la evidencia. **Es la fuente única**: la web, el test, el plan por WhatsApp, el contenido y la tienda salen de acá.
- **Nutriente**: ingesta de referencia (organismo y población), formas, biodisponibilidad, `estado_cobertura` calculado sobre los alimentos con `en_nucleo: true`.
- **Experimento**: un n=1 nunca es evidencia generalizable. Hipótesis, intervención, duración, variables, mediciones, resultado, limitaciones, conclusión provisional.
- **Contenido**: concepto → hook → explicación → mecanismo → ejemplo → aplicación → CTA. Nunca exagerar la evidencia de las notas enlazadas.
- **Hipótesis**: qué propone, origen, qué la haría verificable, qué dice la evidencia actual. Nivel D o E.
- **Pregunta abierta**: pregunta, por qué importa, qué falta, qué fuentes buscar, prioridad.

Fuentes preferidas para salud y suplementos: OMS, NIH/ODS, PubMed, NCCIH, Cochrane.

Volver a [[Inicio]].
