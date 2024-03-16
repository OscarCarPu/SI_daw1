# Particiones
- 1 MBR (master boot record)
- Particiones primarias + particiones extendidas = 4 max
- Particiones extendidas = 1 max
- Particion activa: arranca el equipo
- Partición lógias: divisores de partición extendida
FSTAB
# RAIDs
## RAID 0
Divide en 2 discos los datos:
- Mayor rendimiento
## RAID 1
Copia un disco en otro
- Copia de seguridad
- Capacidad 0.5
## RAID 3/4
Divide en mínimo 3 discos los datos y crea un disco con paridad
- Copia de seguridad
- Capacidad 0.66
## RAID 5
La paridad se reparte entre los discos, como RAID 3/4
## RAID 6
Doble paridad
- Caída de 2 discos
## Raid 10
Se hace una copia de datos (RAID 1) y se reparte entre los discos (RAID 0)
## Raid 01
Se reparte entre los discos (RAID 0) y se hace una copia de datos (RAID 1)
## Raid 50/60
Combinaciones de RAID 5/6 y RAID 0
## JBOD
Combinación de discos para forma un único disco lógico
# Bash

# Shell
# Python
# Redes