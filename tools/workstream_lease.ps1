[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [ValidateSet("acquire", "release", "status")]
    [string]$Action,

    [Parameter(Mandatory = $true, Position = 1)]
    [ValidateSet("claude", "grok", "integration", "production-deploy")]
    [string]$Resource,

    [Parameter(Mandatory = $true, Position = 2)]
    [ValidatePattern("^stream-0[1-6]$")]
    [string]$Stream,

    [string]$CoordinationRoot = "R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\vercy-workstreams\_coordination"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

if ($Resource -in @("integration", "production-deploy") -and $Stream -ne "stream-01") {
    [Console]::Error.WriteLine("$Resource is reserved for stream-01")
    exit 4
}

$lockRoot = [System.IO.Path]::GetFullPath((Join-Path $CoordinationRoot "locks"))
[System.IO.Directory]::CreateDirectory($lockRoot) | Out-Null
$lockPath = [System.IO.Path]::GetFullPath((Join-Path $lockRoot "$Resource.lock"))
$expectedPrefix = $lockRoot.TrimEnd("\") + "\"
if (-not $lockPath.StartsWith($expectedPrefix, [System.StringComparison]::OrdinalIgnoreCase)) {
    [Console]::Error.WriteLine("Resolved lock path escaped the coordination root")
    exit 5
}
$ownerPath = Join-Path $lockPath "owner.json"

function Show-Owner {
    if (Test-Path -LiteralPath $ownerPath) {
        Get-Content -Raw -LiteralPath $ownerPath
    }
    elseif (Test-Path -LiteralPath $lockPath) {
        Write-Output '{"state":"locked","owner":"not-yet-recorded"}'
    }
    else {
        Write-Output "{`"state`":`"free`",`"resource`":`"$Resource`"}"
    }
}

switch ($Action) {
    "status" {
        Show-Owner
        exit 0
    }
    "acquire" {
        try {
            New-Item -ItemType Directory -Path $lockPath -ErrorAction Stop | Out-Null
        }
        catch {
            Show-Owner
            [Console]::Error.WriteLine("$Resource lease is busy; do not start the protected action")
            exit 2
        }
        $owner = [ordered]@{
            schema = "https://ver.cy/schemas/workstream-lease/v1"
            resource = $Resource
            stream = $Stream
            acquired_at = [DateTimeOffset]::UtcNow.ToString("yyyy-MM-dd'T'HH:mm:ss'Z'")
            host = [Environment]::MachineName
            process_id = $PID
        }
        [System.IO.File]::WriteAllText(
            $ownerPath,
            (($owner | ConvertTo-Json -Depth 3) + [Environment]::NewLine),
            [System.Text.UTF8Encoding]::new($false)
        )
        Show-Owner
        exit 0
    }
    "release" {
        if (-not (Test-Path -LiteralPath $lockPath)) {
            [Console]::Error.WriteLine("$Resource lease is already free")
            exit 3
        }
        if (-not (Test-Path -LiteralPath $ownerPath)) {
            [Console]::Error.WriteLine("$Resource lease has no readable owner; fail closed")
            exit 3
        }
        $owner = Get-Content -Raw -LiteralPath $ownerPath | ConvertFrom-Json
        if ($owner.stream -ne $Stream -or $owner.resource -ne $Resource) {
            Show-Owner
            [Console]::Error.WriteLine("$Stream does not own the $Resource lease")
            exit 3
        }
        $resolvedLock = (Resolve-Path -LiteralPath $lockPath).Path
        if (-not $resolvedLock.StartsWith($expectedPrefix, [System.StringComparison]::OrdinalIgnoreCase)) {
            [Console]::Error.WriteLine("Refusing to remove a path outside the coordination root")
            exit 5
        }
        Remove-Item -LiteralPath $resolvedLock -Recurse -Force
        Write-Output "{`"state`":`"released`",`"resource`":`"$Resource`",`"stream`":`"$Stream`"}"
        exit 0
    }
}
