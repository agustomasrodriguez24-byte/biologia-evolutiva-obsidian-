---
tipo: sistema
fecha_revision: 2026-10-03
---

# Criterios de la tienda

> La tienda es el último eslabón del sistema, no el primero. Ningún producto entra porque "se vende" o "es rico": entra porque cubre una **necesidad** que el sistema ya documentó.

## La cadena de alineación

Todo producto tiene que poder recorrer esta cadena completa. Si se corta en algún punto, no entra.

```
NECESIDAD del cuerpo
  → CONCEPTO (02 Conceptos)
  → MECANISMO (03 Mecanismos)
  → INTERVENCIÓN / PROTOCOLO (05–06)
  → PRODUCTO (08 Productos)
  → VALOR para el cliente: texto → video de regalo (10 Contenido)
```

Ejemplo: [[Ritmo circadiano]] → [[Señalización lumínica circadiana]] → [[Reducción de luz nocturna]] → [[Lentes con filtro de luz azul]].

## Filtro 1: alimentos

Un alimento entra solo si cumple **todos** estos criterios:

1. **Nutre de forma efectiva**: tiene su nota en `14 Alimentos/` evaluada con la [[Matriz de Cobertura Nutricional]] (densidad, digestibilidad, biodisponibilidad, utilización). Umbral sugerido para entrar: densidad ≥4 y ningún otro puntaje <3; las excepciones se justifican, por ejemplo si cubre un hueco del núcleo.
2. **Mínimamente procesado**: lista de ingredientes corta y reconocible. Sin azúcares añadidos, sin aceites refinados, sin aditivos cosméticos (colorantes, saborizantes) que no cumplan una función.
3. **Alineado**: enlaza con al menos un concepto o protocolo del vault.
4. **Trazable**: origen, proveedor, habilitación sanitaria y, si existe, análisis de laboratorio.
5. **Seguro**: alérgenos, interacciones y contraindicaciones documentados.

> [!note] Sobre "superalimento"
> No es una categoría científica ni regulatoria: cualquiera puede ponérsela a cualquier cosa. Usala como **sello propio definido por estos criterios** (por ejemplo, "Aprobado Nutrición Evolutiva"), y en la comunicación hablá de lo concreto: "fuente de magnesio", "30 g de proteína por porción". Eso es lo que te diferencia de la tienda de al lado.

## Filtro 2: herramientas (lentes, lámparas, accesorios)

1. **Necesidad real** documentada en el vault.
2. **Mecanismo** con nivel A o B.
3. **Evidencia del producto específico** (no solo del mecanismo). Si es C o inferior, el producto puede entrar, pero la promesa se ajusta a esa evidencia.
4. **Lugar dentro de un protocolo**: la herramienta acompaña un hábito, no lo reemplaza.

## Regla de la promesa

Lo que se puede decir de un producto depende del nivel de la afirmación, no de lo que dice el fabricante.

| Nivel | Cómo se comunica |
|---|---|
| A | "Ayuda a…", con el matiz que corresponda |
| B | "Puede ayudar a…" |
| C | "Hay datos preliminares de que…" |
| D / E | "En la tradición X se usa para…". Nunca como promesa |
| F | No se repite. Las afirmaciones del fabricante no son argumento de venta |

## Bloque de valor (texto → video)

Cada producto aprobado lleva una ficha de valor con esta estructura. Primero va en texto en la tienda; después se graba como video de regalo (nota en `10 Contenido/`, enlazada en la propiedad `contenido` del producto).

1. **Para qué te sirve**: la necesidad, en palabras simples.
2. **Cómo encaja en tu biología**: el concepto y el mecanismo.
3. **Cómo usarlo**: el protocolo, paso a paso.
4. **Qué podés esperar y qué no**: la evidencia, contada honestamente.
5. **Para quién no es**: contraindicaciones.

El punto 4 es lo que construye confianza: el cliente percibe que no le estás vendiendo humo.

## Estados (`estado_tienda`)

- `evaluando`: en análisis.
- `aprobado`: cumple todos los criterios.
- `aprobado-con-condiciones`: entra con una promesa limitada o con requisitos (por ejemplo, venderse solo dentro de un protocolo).
- `rechazado`: no cumple. Se guarda la nota con el motivo, para no volver a evaluarlo.

## Aspecto legal

Las declaraciones de salud en alimentos y productos están reguladas (en Uruguay, por el Ministerio de Salud Pública y la normativa bromatológica). Antes de publicar una promesa de salud, revisala con un profesional del área regulatoria. Lista de trabajo: [[Claims permitidos]]. Riesgos: [[Riesgos y cumplimiento]].

Panel: [[Tienda.base|Tienda]]. Volver a [[Inicio]].
