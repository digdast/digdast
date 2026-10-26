<#
.SYNOPSIS
    Registers a Windows Scheduled Task for Daily LinkedIn Posting
.DESCRIPTION
    Creates 'LinkedInDailyAutopilot' task that executes every weekday at 8:30 AM,
    loading the day's post and graphic, and opening LinkedIn.
#>

$taskName = "LinkedInDailyAutopilot"
$pythonPath = (Get-Command python).Source
$scriptPath = "C:\scripts\linkedin_autopilot\daily_post_engine.py"

# Define the action
$action = New-ScheduledTaskAction -Execute $pythonPath -Argument "`"$scriptPath`"" -WorkingDirectory "C:\scripts\linkedin_autopilot"

# Define the trigger: Monday through Friday at 8:30 AM
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday, Tuesday, Wednesday, Thursday, Friday -At 8:30AM

# Settings
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

# Register or update task
try {
    Unregister-ScheduledTask -TaskName $taskName -Confirm:$false -ErrorAction SilentlyContinue
    Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Settings $settings -Description "Daily LinkedIn Post Autopilot for Efrain Rivas" | Out-Null
    Write-Host "[SUCCESS] Scheduled Task '$taskName' registered!" -ForegroundColor Green
    Write-Host "It will trigger automatically Monday - Friday at 8:30 AM EST." -ForegroundColor Cyan
} catch {
    Write-Warning "Could not register scheduled task: $_"
}
