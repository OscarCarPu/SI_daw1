# DHCP
### Instala un servidor DHCP nun Debian Server

Configuracion ip server:

![Configuracion ip server](./img/conf%20server%20ip.png)

Status de dhcp al instalar:

![Status dhcp](./img/dhcp%20status%20installed.png)

### Monta unha infraestuctura na rede 172.16.X.0/24
- Rango entre 10 e 20
- ip server X.X.X.1
- gateway X.X.X.100
- dns X.X.X.254
- dominio si.local

Configuracion interfaz dhcp:

![interfaz](./img/interfaz%20dhcp.png)

Configuracion dhcp:

![conf dhcp](./img/configuracion%20dhcp.png)

Nuevo status de dhcp:

![status dhcp](./img/nuevo%20status%20dhcp.png)

### Utiliza Wireshark para capturar a asignar DHCP

Desde windows, al hacer un renew:

![renew](./img/ipconfig%20renew.png)

Se capturan los paquetes desde wireshark:

![wireshark](./img/wireshark.png)

## Crea reservas MAC para:
- Windows: X.X.X.15
- Ubuntu: X.X.X.17

Ip reservadas:

![reserva](./img/ip%20reservadas.png)

Windows ipconfig:

![ipconfig](./img/config%20windows.png)

Ubuntu ip a

![ipa](./img/ubuntu%20configuracion.png)