Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Get-RepoRoot {
  $r = git rev-parse --show-toplevel 2>$null
  if (-not $r) { throw "Not in a git repo." }
  (Resolve-Path $r).Path
}
function Enter-RepoRoot { Set-Location -LiteralPath (Get-RepoRoot) }
function Join-UnderRoot { param([Parameter(ValueFromRemainingArguments=$true)][string[]]$Segments)
  $p = Get-RepoRoot; foreach($s in $Segments){ $p = Join-Path -Path $p -ChildPath $s }; $p }
function Assert-NotInside { param([string]$Target)
  $wd = (Resolve-Path .).Path; $tp = [IO.Path]::GetFullPath($Target)
  if ($wd -like "$tp*") { throw "Do not run from inside: $Target" } }
function Assert-PathSanity { param([string]$Path)
  $norm = [IO.Path]::GetFullPath($Path)
  if ($norm -match '(\\[^\\]+)\\.*?\1(\\|$)') { throw "Repeated segment in path: $norm" } }
