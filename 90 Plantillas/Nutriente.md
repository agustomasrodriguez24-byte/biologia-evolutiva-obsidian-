---
tipo: nutriente
clase:
pilar:
  - nutricion
ingesta_referencia:
unidad:
poblacion_referencia: adultos
estado_cobertura:
estado: borrador
nivel_evidencia:
fecha_creacion: {{date:YYYY-MM-DD}}
fecha_revision: {{date:YYYY-MM-DD}}
fuentes: []
relacionados: []
---

# {{title}}

Matriz: [[Matriz de Cobertura Nutricional]] · Pilar: [[P02 Nutrición]]

## Qué es y para qué lo usa el cuerpo

## Ingesta de referencia
<!-- Valor, unidad, población y organismo que lo define -->

## Formas y biodisponibilidad
<!-- Qué formas existen, cuáles se absorben mejor, potenciadores e inhibidores -->

## Utilización
<!-- ¿Requiere conversión? ¿qué la limita? -->

## Quiénes tienen más riesgo de déficit

## Exceso / límite superior

## Alimentos que lo aportan

```base
filters:
  and:
    - 'tipo == "alimento"'
    - file.hasLink(this.file)
views:
  - type: table
    name: Fuentes alimentarias
    order:
      - file.name
      - en_nucleo
      - biodisponibilidad
      - porcion_g
```

## Cobertura en el núcleo
<!-- cubierto / parcial / hueco / contexto, y por qué -->
