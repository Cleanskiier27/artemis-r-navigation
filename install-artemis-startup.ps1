# Artemis R: Startup Configuration Script
# Configures the Mission Control Dashboard to run on Windows Startup with Admin privileges.

$ScriptPath = "C:\Users\ceans\OneDrive\Documents\GitHub\networkbuster.net\artemis-r-navigation\start-artemis-dashboard.ps1"
$TaskName = "ArtemisR-MissionControl-Startup"

Write-Host "Configuring Artemis R for System Startup..." -ForegroundColor Cyan

# Check for Admin Privileges (required for Scheduled Tasks)
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if (-not $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Warning "ADMIN PRIVILEGES REQUIRED. Re-launching as Administrator..."
    Start-Process powershell.exe -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs
    exit
}

# Create a Scheduled Task to run on Logon with Highest Privileges
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-WindowStyle Hidden -ExecutionPolicy Bypass -File `"$ScriptPath`""
$trigger = New-ScheduledTaskTrigger -AtLogOn
$principal = New-ScheduledTaskPrincipal -UserId "$env:USERNAME" -LogonType Interactive -RunLevel Highest

Write-Host "Registering Scheduled Task: $TaskName" -ForegroundColor Green
Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Principal $principal

Write-Host "Success: Artemis R Mission Control will now launch on system startup." -ForegroundColor Green
Write-Host "You can manually test it now by running: ./start-artemis-dashboard.ps1" -ForegroundColor Yellow
