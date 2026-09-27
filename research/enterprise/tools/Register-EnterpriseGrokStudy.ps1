[CmdletBinding()]
param(
    [Parameter(Mandatory)][ValidatePattern('^EM-[A-Z]+-[0-9]{2}$')][string]$Contour,
    [Parameter(Mandatory)][string]$ResponseFile,
    [Parameter(Mandatory)][ValidatePattern('^https://grok\.com/c/')][string]$ConversationUrl,
    [Parameter(Mandatory)][ValidateSet('ACCEPT', 'ACCEPT WITH LIMITS', 'REVISE', 'REJECT')][string]$Verdict,
    [Parameter(Mandatory)][bool]$NewModel,
    [string]$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..')).Path,
    [datetime]$CompletedAt = (Get-Date).ToUniversalTime(),
    [switch]$Force
)

$ErrorActionPreference = 'Stop'
$repo = [IO.Path]::GetFullPath($RepoRoot)
$run = Join-Path $repo ('research\enterprise\runs\' + $Contour.ToLowerInvariant())
$promptPath = Join-Path $run 'grok-prompt.md'
$responsePath = Join-Path $run 'grok-study.raw.md'
$manifestPath = Join-Path $run 'grok-study.manifest.json'
$sourceResponse = [IO.Path]::GetFullPath($ResponseFile)

if (-not (Test-Path -LiteralPath $run -PathType Container)) { throw "Missing contour run: $Contour" }
if (-not (Test-Path -LiteralPath $promptPath -PathType Leaf)) { throw "Missing prompt: $promptPath" }
if (-not (Test-Path -LiteralPath $sourceResponse -PathType Leaf)) { throw "Missing response file: $sourceResponse" }
if ((Get-Item -LiteralPath $sourceResponse).Length -eq 0) { throw 'Grok response is empty.' }
if (-not $Force -and ((Test-Path -LiteralPath $responsePath) -or (Test-Path -LiteralPath $manifestPath))) {
    throw "Grok evidence already exists for $Contour; use -Force only for an intentional exact replacement."
}

if ($sourceResponse -ne [IO.Path]::GetFullPath($responsePath)) {
    Copy-Item -LiteralPath $sourceResponse -Destination $responsePath -Force
}

$manifest = [ordered]@{
    format = 'vercy-provider-study-manifest/v1'
    contour = $Contour
    provider = 'Grok'
    mode = 'Heavy'
    toolsUsedByProvider = $true
    promptFile = 'grok-prompt.md'
    promptSha256 = (Get-FileHash -LiteralPath $promptPath -Algorithm SHA256).Hash.ToLowerInvariant()
    responseFile = 'grok-study.raw.md'
    responseSha256 = (Get-FileHash -LiteralPath $responsePath -Algorithm SHA256).Hash.ToLowerInvariant()
    conversationUrl = $ConversationUrl
    completedAt = $CompletedAt.ToUniversalTime().ToString('o')
    verdict = $Verdict
    newModel = $NewModel
}
$json = $manifest | ConvertTo-Json -Depth 5
[IO.File]::WriteAllText($manifestPath, $json + "`n", [Text.UTF8Encoding]::new($false))

[pscustomobject][ordered]@{
    format = 'vercy-enterprise-grok-study-registration/v1'
    contour = $Contour
    responseBytes = (Get-Item -LiteralPath $responsePath).Length
    responseSha256 = $manifest.responseSha256
    manifestPath = $manifestPath
    valid = $true
} | ConvertTo-Json
