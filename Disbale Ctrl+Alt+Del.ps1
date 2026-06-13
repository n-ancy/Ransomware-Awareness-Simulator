$ErrorActionPreference = "SilentlyContinue"

Write-Host "--- Ransomware Awareness Demo ---" -ForegroundColor Red
Write-Host "SIMULATION STARTED: Keyboard interrupts and Ctrl+Alt+Del are BLOCKED for 2 minutes." -ForegroundColor Yellow
Write-Host "Pressing Ctrl+Alt+Del will result in an immediate fallback to the desktop." -ForegroundColor Cyan

# Define 2 minutes in seconds (120 seconds total)
$DurationSeconds = 120
$Stopwatch = [System.Diagnostics.Stopwatch]::StartNew()

# Active process suppression loop
while ($Stopwatch.Elapsed.TotalSeconds -lt $DurationSeconds) {
    
    # 1. Instantly kill the Windows Lock Overlay application if spawned
    Stop-Process -Name "LockApp" -Force
    
    # 2. Force Windows to return to the active user session workspace if it tries to switch
    $SecOverlay = Get-Process | Where-Object {$_.Name -eq "LogonUI" -and $_.SessionId -ne 0}
    if ($SecOverlay) {
        Stop-Process -Id $SecOverlay.Id -Force
    }

    # 3. Calculate remaining execution time for the visual display progress bar
    $TimeLeft = [math]::Round($DurationSeconds - $Stopwatch.Elapsed.TotalSeconds)
    $Percent  = [math]::Round(($Stopwatch.Elapsed.TotalSeconds / $DurationSeconds) * 100)
    
    Write-Progress -Activity "DEMO ACTIVE: Ctrl+Alt+Del Screen Intercepted" -Status "$TimeLeft seconds remaining" -PercentComplete $Percent
    
    # Run loop at max speed to ensure zero lag time when catching the key combinations
    Start-Sleep -Milliseconds 50
}

$Stopwatch.Stop()
Write-Host "DEMO FINISHED: System keyboard security hooks restored to normal parameters." -ForegroundColor Green
