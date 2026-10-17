# Compara las notas del vault con sus copias en docs/ del repo.
# Uso: comparar.ps1            -> solo informa
#      comparar.ps1 -Aplicar   -> copia al repo las notas que cambiaron
# Empareja por nombre de archivo (sin escribir nombres con tildes en el script).
param([switch]$Aplicar)

$vault = Split-Path (Split-Path (Split-Path $PSScriptRoot -Parent) -Parent) -Parent
$docs = Join-Path (Split-Path $vault -Parent) "Nutricion-Evolutiva-Web\docs"
if (-not (Test-Path -LiteralPath $docs)) { "ERROR: no encuentro el repo en $docs"; exit 1 }

$notas = Get-ChildItem -LiteralPath $vault -Recurse -File -Filter *.md |
  Where-Object { $_.FullName -notmatch '\\(\.claude|\.obsidian|90 Plantillas|99 Archivo)\\' }

$cambios = 0
foreach ($copia in Get-ChildItem -LiteralPath $docs -File -Filter *.md | Where-Object { $_.Name -ne 'README.md' }) {
  $orig = $notas | Where-Object { $_.Name -eq $copia.Name } | Select-Object -First 1
  if (-not $orig) { "SIN ORIGINAL EN EL VAULT: $($copia.Name)"; continue }
  if ((Get-FileHash -LiteralPath $orig.FullName).Hash -ne (Get-FileHash -LiteralPath $copia.FullName).Hash) {
    $cambios++
    if ($Aplicar) { Copy-Item -LiteralPath $orig.FullName -Destination $copia.FullName -Force; "ACTUALIZADO: $($copia.Name)" }
    else { "CAMBIO: $($copia.Name)  <-  $($orig.FullName.Substring($vault.Length + 1))" }
  }
}
"notas con cambios: $cambios"
