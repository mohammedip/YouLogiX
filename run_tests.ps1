# Script PowerShell pour exécuter les tests YouLogiX
Write-Host "=== Exécution des tests YouLogiX ===" -ForegroundColor Cyan

# Activer l'environnement virtuel
$venvPath = ".venv\Scripts\Activate.ps1"
if (Test-Path $venvPath) {
    & $venvPath
    Write-Host "Environnement virtuel activé" -ForegroundColor Green
}

# Définir la variable d'environnement pour les tests
$env:TESTING = "1"
Write-Host "Variable TESTING=1 définie" -ForegroundColor Green

# Exécuter pytest
Write-Host "`nExécution de pytest..." -ForegroundColor Yellow
python -m pytest app/tests/ -v --tb=short

Write-Host "`n=== Tests terminés ===" -ForegroundColor Cyan
