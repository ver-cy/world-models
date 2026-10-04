[CmdletBinding()]
param(
    [string]$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..')).Path,
    [switch]$IncludePrompt
)

$ErrorActionPreference = 'Stop'
$repo = [IO.Path]::GetFullPath($RepoRoot)
$queuePath = Join-Path $repo 'research\enterprise\queue.json'
$queue = Get-Content -LiteralPath $queuePath -Raw | ConvertFrom-Json
$publicationNames = @(Get-ChildItem -LiteralPath (Join-Path $repo 'publications') -Directory).Name

$pending = foreach ($unit in @($queue.units | Sort-Object sequence)) {
    if ($unit.status -in @('published', 'published-partial', 'research-reconciled')) { continue }

    $run = Join-Path $repo ('research\enterprise\runs\' + ([string]$unit.id).ToLowerInvariant())
    $manifestPath = Join-Path $run 'checkpoint-manifest.json'
    $promptPath = Join-Path $run 'grok-prompt.md'
    if (-not (Test-Path -LiteralPath $manifestPath -PathType Leaf)) { continue }
    if (-not (Test-Path -LiteralPath $promptPath -PathType Leaf)) { continue }
    if (@('grok-study.raw.md', 'grok-response.raw.md', 'grok-review.raw.md') | ForEach-Object {
            Test-Path -LiteralPath (Join-Path $run $_) -PathType Leaf
        } | Where-Object { $_ } | Select-Object -First 1) { continue }

    $manifest = Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json
    $errors = @()
    foreach ($file in @($manifest.files)) {
        $path = Join-Path $run ([string]$file.path)
        if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
            $errors += "missing:$($file.path)"
            continue
        }
        $actual = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant()
        if ($actual -ne [string]$file.sha256) { $errors += "hash:$($file.path)" }
    }
    if ($errors.Count) { throw "Invalid checkpoint $($unit.id): $($errors -join ', ')" }

    $missingBases = @($manifest.baseModelIds | Where-Object {
            $_ -and -not ($publicationNames -like (([string]$_).ToLowerInvariant() + '-*'))
        })
    $priorityRank = if (@($manifest.unassignedCandidates).Count) { 2 } elseif ($missingBases.Count) { 1 } else { 0 }
    $prompt = Get-Item -LiteralPath $promptPath
    [pscustomobject][ordered]@{
        priorityRank = $priorityRank
        sequence = [int]$unit.sequence
        id = [string]$unit.id
        promptPath = $prompt.FullName
        promptBytes = $prompt.Length
        promptSha256 = (Get-FileHash -LiteralPath $promptPath -Algorithm SHA256).Hash.ToLowerInvariant()
        missingBasePublicationIds = $missingBases
        unassignedCandidateCount = @($manifest.unassignedCandidates).Count
    }
}

$ordered = @($pending | Sort-Object priorityRank, unassignedCandidateCount, sequence)
if (-not $ordered.Count) {
    [ordered]@{ format = 'vercy-enterprise-next-grok/v1'; remaining = 0; next = $null } | ConvertTo-Json -Depth 5
    exit 0
}

$next = $ordered[0]
$result = [ordered]@{
    format = 'vercy-enterprise-next-grok/v1'
    remaining = $ordered.Count
    next = [ordered]@{
        id = $next.id
        sequence = $next.sequence
        promptPath = $next.promptPath
        promptBytes = $next.promptBytes
        promptSha256 = $next.promptSha256
        missingBasePublicationIds = @($next.missingBasePublicationIds)
        unassignedCandidateCount = $next.unassignedCandidateCount
        action = 'requires-fresh-user-confirmation-immediately-before-browser-send'
    }
}
if ($IncludePrompt) { $result.next.prompt = Get-Content -LiteralPath $next.promptPath -Raw }
$result | ConvertTo-Json -Depth 6
