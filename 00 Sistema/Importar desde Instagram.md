---
tipo: sistema
fecha_creacion: 2026-10-07
fecha_revision: 2026-10-07
relacionados:
  - "[[Flujo de ingreso]]"
  - "[[Dirección creativa]]"
---

# Importar desde Instagram

> Cómo pasar tu **archivo de oro** (los posts que te mandás al chat con @nutricionancestral.uy) al sistema. Claude lo hace con la skill `/importar-instagram`.

## El circuito
```
Ves un post que te sirve → lo mandás al chat con @nutricionancestral.uy
        ↓ (cada tanto: una vez por mes o cuando juntes muchos)
Exportás tus mensajes de Instagram → ZIP en Descargas → /importar-instagram
        ↓
Bandeja ordenada por tema → /procesar-bandeja (salud, con nivel A–F)
                          → Dirección creativa (marketing y formatos)
```

## Paso a paso: exportar los mensajes (lo hacés vos, 2 minutos)
1. Instagram → **Configuración** → **Centro de cuentas** → **Tu información y permisos** → **Descargar tu información**.
2. **Descargar o transferir información** → elegí **agustin.nutricion.evolutiva**.
3. **Algunos de tus datos** → marcá **solo "Mensajes"**.
4. **Descargar en el dispositivo** →
   - Intervalo: **Desde el principio** la primera vez; después, **Último mes**.
   - Formato: **JSON** (importante: no HTML).
   - Calidad de multimedia: **Baja**.
5. **Crear archivos.** Meta avisa por mail o notificación cuando está listo.
6. Bajá el ZIP a **Descargas** y decile a Claude: **"importá Instagram"**.

## Qué hace Claude
- Lee **solo** ese chat (las demás conversaciones no se tocan) y saca cada post compartido: autor, link, fecha y texto.
- Los ordena por tema y los deja en `13 Bandeja de entrada/`, uno por tema.
- Arma y mantiene la tabla de referentes (abajo).
- Te pide un resumen de una línea solo de los reels clave que no tienen texto.
- Después, con tu OK: `/procesar-bandeja` verifica lo de salud contra estudios y lo de marketing alimenta la [[Dirección creativa]].

## Tip para que rinda más
Cuando te mandes un post, **escribí una palabra al lado**: `nutri`, `venta`, `formato`, `hábito`, `idea`. El script la lee como "nota de Agus" y ordena mejor.

## Importaciones
| Fecha | Desde | Posts | Notas |
|---|---|---|---|
| 2026-10-07 | n/a | muestra parcial leída desde Chrome | Ver bandeja: *Archivo de oro Instagram (muestra)* |

## Referentes
*Se completa con cada importación. Confianza: alta (cita fuentes) · media (comunicador serio) · baja (marketing o prácticas sin respaldo).*

| Cuenta | Tema | Qué tomamos | Confianza |
|---|---|---|---|
| @mundofitness.x | Nutrición: pérdidas de nutrientes | Idea de "drenaje vs. suministro"; datos a verificar en NIH | Media, verificar |
| @hombresdelatierra | Nutrición ancestral, comunidad | Alimentos densos; CTA por comentario y comunidad con prueba gratis | Media (marketing fuerte) |
| @freehuman.global | Ritmos y hábitos | Luz matutina, horarios de comida, cambios pequeños | Media |
| @michellepiters | Ventas | Vender sin sonar vendedor; prueba social; historias | Media |
| @the_whole_istic_gangsta | Prácticas alternativas | Nada (recomienda tomar orina) | Baja: descartado |

Volver a [[Inicio]].
