Set-ItemProperty -Path C:\DOS\folla.dat -Name Attributes -Value ([System.IO.FileAttributes]::Hidden)

New-Item L:\FOL\folla.dat
$FILE=Get-Item L:\FOL\folla.dat
$FILE.Attributes = 'Hidden'
Set-Location  L:\FOL
Get-ChildItem -force