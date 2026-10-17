---
tipo: nutriente
clase: otro esencial
pilar:
  - nutricion
  - biologia
ingesta_referencia: 550 (hombres) / 425 (mujeres)
unidad: mg/día (AI)
poblacion_referencia: adultos
estado_cobertura:
estado: borrador
nivel_evidencia: A
fecha_creacion: 2026-10-03
fecha_revision: 2026-10-03
fuentes:
  - "[[NIH ODS - Fichas de suplementos]]"
relacionados: []
---

# Colina

Matriz: [[Matriz de Cobertura Nutricional]] · Pilar: [[P02 Nutrición]]

## Qué es y para qué lo usa el cuerpo
Nutriente esencial. Se usa para formar membranas celulares (fosfatidilcolina) y el neurotransmisor acetilcolina, y participa en el metabolismo de grasas en el hígado y en el metabolismo de grupos metilo.

## Ingesta de referencia
Ingesta adecuada (AI) para adultos: 550 mg/día en hombres y 425 mg/día en mujeres. Es mayor en el embarazo y la lactancia. → [[NIH ODS - Fichas de suplementos]] (ficha de colina)

## Formas y biodisponibilidad
*(Pendiente.)*

## Utilización
El cuerpo produce algo de colina, pero no la suficiente: hace falta incorporarla con la dieta.

## Quiénes tienen más riesgo de déficit
Embarazo, y personas que comen pocos alimentos de origen animal. *(Ampliar con la ficha del ODS.)*

## Exceso / límite superior
Existe un límite superior para adultos. *(Cargar el valor desde la ficha del ODS.)*

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
*(Pendiente: depende del surtido.)*
