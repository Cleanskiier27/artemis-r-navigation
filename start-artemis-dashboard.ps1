# Artemis R: Mission Control Startup Script
# Starts the telemetry relay and launches the dashboard.

$ProjectDir = "C:\Users\ceans\OneDrive\Documents\GitHub\networkbuster.net\artemis-r-navigation"
Set-Location $ProjectDir

Write-Host "Checking Mission Readiness..." -ForegroundColor Cyan

# 1. Install dependencies if node_modules is missing
if (-not (Test-Path "node_modules")) {
    Write-Host "Installing mission-critical Node.js dependencies..." -ForegroundColor Yellow
    npm install
}

# 2. Start the Telemetry Relay Server in the background
Write-Host "Starting Artemis R Telemetry Relay..." -ForegroundColor Green
Start-Process -FilePath "node" -ArgumentList "src/server/mission_relay_server.js" -WindowStyle Hidden

# 3. Launch the Mission Control Dashboard
Write-Host "Launching Mission Control Dashboard..." -ForegroundColor Green
Start-Sleep -Seconds 2
Start-Process "http://localhost:3000"

Write-Host "Mission Control is LIVE. Pilot Controls: LOCKED." -ForegroundColor White -BackgroundColor DarkBlue
