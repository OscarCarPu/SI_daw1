Copy-Item -Path "C:\PRACTICA2\*.txt" -Destination "C:\DOS\" -Force -PassThru | Rename-Item -NewName { $_.Name -replace '\.txt$', '.sol' }
