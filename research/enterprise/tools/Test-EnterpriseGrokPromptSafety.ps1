[CmdletBinding()]
param(
    [string]$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..')).Path,
    [string]$OutputPath = (Join-Path $PSScriptRoot '..\grok-prompt-safety-report.json')
)

$ErrorActionPreference = 'Stop'
$repo = [IO.Path]::GetFullPath($RepoRoot)
$queue = Get-Content -LiteralPath (Join-Path $repo 'research\enterprise\queue.json') -Raw | ConvertFrom-Json
$patterns = [ordered]@{
    windowsPath = '(?im)(?:^|[\s`"''])(?:[A-Z]:\\|\\\\[^\s\\]+\\)'
    userHome = '(?i)(?:/Users/|/home/|C:\\Users\\)'
    email = '(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b'
    ipv4 = '(?<![\d.])(?:25[0-5]|2[0-4]\d|1?\d?\d)(?:\.(?:25[0-5]|2[0-4]\d|1?\d?\d)){3}(?![\d.])'
    secretAssignment = '(?im)\b(?:api[_-]?key|password|passwd|secret|bearer|access[_-]?token|private[_-]?key)\b\s*[:=]\s*\S+'
    passwordManager = '(?i)\b1password\b|\baeilius\.tech\b'
}

$items = foreach ($unit in @($queue.units | Sort-Object sequence)) {
    if ($unit.status -ne 'research-checkpoint-awaiting-grok') { continue }
    $relative = 'research/enterprise/runs/' + ([string]$unit.id).ToLowerInvariant() + '/grok-prompt.md'
    $path = Join-Path $repo ($relative -replace '/', [IO.Path]::DirectorySeparatorChar)
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) { throw "Missing prompt: $relative" }
    $text = Get-Content -LiteralPath $path -Raw
    $findings = foreach ($entry in $patterns.GetEnumerator()) {
        $matches = [regex]::Matches($text, $entry.Value)
        if ($matches.Count) {
            [ordered]@{ kind = $entry.Key; count = $matches.Count }
        }
    }
    $file = Get-Item -LiteralPath $path
    [ordered]@{
        sequence = [int]$unit.sequence
        id = [string]$unit.id
        path = $relative
        bytes = $file.Length
        sha256 = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant()
        safe = @($findings).Count -eq 0
        findings = @($findings)
    }
}

$result = [ordered]@{
    format = 'vercy-enterprise-grok-prompt-safety/v1'
    generatedAt = (Get-Date).ToUniversalTime().ToString('o')
    patterns = @($patterns.Keys)
    total = @($items).Count
    passed = @($items | Where-Object safe).Count
    failed = @($items | Where-Object { -not $_.safe }).Count
    items = @($items)
}
$result | ConvertTo-Json -Depth 7 | Set-Content -LiteralPath $OutputPath -Encoding utf8
[pscustomobject][ordered]@{
    format = $result.format
    generatedAt = $result.generatedAt
    total = $result.total
    passed = $result.passed
    failed = $result.failed
} | ConvertTo-Json
if ($result.failed) { exit 2 }
