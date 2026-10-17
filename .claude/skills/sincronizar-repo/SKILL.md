---
name: sincronizar-repo
description: Sube al repositorio de GitHub de la web (aaavril/Nutricion-Evolutiva-Web) los cambios de las notas del vault que tienen copia en docs/, respetando las reglas de git del repo. Usar cuando el usuario dice "sincronizá el repo", "actualizá el repo", "subí los cambios a GitHub" o cuando cambió una nota que la programadora usa (brief, especificación, diseño, claims, etc.).
---

# Sincronizar repo

El vault es la fuente de verdad. El repo tiene copias en `docs/` para Avril. Esta skill las mantiene iguales.

- **Repo local:** `C:\Users\Usuario\Downloads\nutricion evolutiva\Nutricion-Evolutiva-Web`
- **Git:** `C:\Program Files\Git\cmd\git.exe` (puede no estar en el PATH de la sesión)
- **Reglas de git:** las del `CLAUDE.md` del repo. Leelo si no lo leíste en esta sesión. Su mención a "datos de pacientes" no aplica.

## Pasos
1. **Avisá y traé lo último.** Decí qué hace `git pull --ff-only` y corrélo. Si falla por cambios locales o por divergencia, frená y explicá; no fuerces nada.
2. **Compará.** Corré `.claude/skills/sincronizar-repo/comparar.ps1` (sin parámetros). Lista las notas que cambiaron. Si no hay cambios, decilo y terminá.
3. **¿Hay notas nuevas para sumar?** Si en la sesión se creó o cambió una nota que Avril necesita y no tiene copia en `docs/`, proponela con AskUserQuestion antes de agregarla (y sumala a la tabla de `docs/README.md`).
4. **Copiá.** Corré `comparar.ps1 -Aplicar` (y copiá a mano las notas nuevas aprobadas).
5. **Caso especial: el brief.** Si cambió `Brief para desarrollo.md`, actualizá también `docs/brief-desarrollo.html` con los mismos cambios y republicá la página con `Artifact` usando `url: https://claude.ai/artifact/CX77uVkWgV6YntbtuqV9zW` (leela primero con `action: "read"`, editá el archivo que te devuelve y publicá ese archivo).
6. **Control antes de commitear.** `git status` + `git diff --stat`. Verificá que no entre ninguna clave, `.env` ni dato personal real. Si aparece algo así, frená y avisá.
7. **Commit.** Decí qué vas a commitear. Un commit por cambio que se entienda solo: mensaje en español, el cuerpo explica el porqué. Sin `Co-Authored-By` ni menciones de Claude.
8. **Push.** Decí qué hace y corré `git push origin main`. Si pide login, se abre la ventana de GitHub para Agus.
9. **Verificá.** `git rev-parse HEAD` igual a `origin/main` y corré de nuevo `comparar.ps1`: tiene que dar 0 cambios.
10. **Registrá.** Una línea en la sección de repositorio de `30 Web/Estado - Web.md` con la fecha y qué se subió.

## No hacer
- No tocar `_bmad/`, `.claude/`, `CLAUDE.md` ni `GUIA-BMAD.md` del repo: son de Avril.
- No modificar `docs/referencia-web-v0/`: es una foto fija del prototipo. El código vivo lo decide el paso de arquitectura de BMAD.
- Nada destructivo (`reset --hard`, `push --force`, `checkout --`, `clean`) sin permiso explícito.
