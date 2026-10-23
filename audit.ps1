
$report = [ordered]@{
    ScanTime = (Get-Date).ToString("o")
    Hostname = $env:COMPUTERNAME
    OperatingSystem = $null
    TotalRAMGB = $null
    DiskFreeGB = $null
    Firewall = @()
    Defender = $null
}

$os = Get-CimInstance Win32_OperatingSystem

$report.OperatingSystem = $os.Caption

$report.TotalRAMGB = [math]::Round(
    $os.TotalVisibleMemorySize / 1MB, 2
)

$disk = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'"

if ($disk) {
    $report.DiskFreeGB = [math]::Round(
        $disk.FreeSpace / 1GB, 2
    )
}

try {
    $report.Firewall = @(
        Get-NetFirewallProfile -ErrorAction Stop |
        Select-Object Name, Enabled
    )
} catch {
    $report.Firewall = @()
}

try {
    $defender = Get-MpComputerStatus -ErrorAction Stop

    $report.Defender = @{
        AntivirusEnabled = $defender.AntivirusEnabled
        RealTimeProtectionEnabled = $defender.RealTimeProtectionEnabled
    }
} catch {
    $report.Defender = $null
}

$report | ConvertTo-Json -Depth 5 |
    Set-Content -Path ".\audit_results.json" -Encoding UTF8

Write-Host "IT audit completed!"
Write-Host "Results saved to audit_results.json"
