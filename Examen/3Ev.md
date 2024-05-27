# MEDIOS

## Perturbaciones

### Atenuación

Consiste en la pérdida de energía inherente al transporte de dicho señal por el medio. A mayor distancia recorrida, mayor será dicha pérdida. Para solucionar esta perturbación se establecen mecanismos como:

- Limitar las longitudes máximas de los medios/canales.
- Uso de repetidores/amplificadores.

### Distorsión

Consiste en la alteración de las velocidades de transmisión de las señales y las frecuencias. Un modo de solucionarlo sería utilizando ecualizaciones.

### Ruido

Consiste en la introducción en el medio de señales no deseadas. El tratamiento del ruido se basa en la introducción de aislantes para estas señales no deseadas. Una de las perturbaciones más habituales.

## Tipos de Medios de Transmisión Guiados

### Coaxial

Consiste en un hilo de cobre recubierto por un aislante y una malla metalica. Se usaba como fibra cuando era muy cara. Ahora esta en desuso

### Par Trenzado

Es el medio guiado más utilizado en las LAN, permitiendo hasta 100m sin repetidores. Consiste en 8 hilos de cobre recubiertos por una funda plástica, trenzados de 2 en 2 para reducir el crosstalk. El estándar de terminación en RJ45 es el T568B en ambos lados.

**Codificación par trenzado X/YTP:**

- X indica el apantallamiento global:
  - U: no apantallado.
  - F: apantallado con lámina de aluminio.
  - S: apantallado con malla metálica.
  - SF: apantallado con malla y lámina metálica.
- Y indica el apantallamiento de los pares:
  - U: no apantallado.
  - F: apantallado con lámina de aluminio.

**Categorías según prestaciones/velocidades:**

- **Cat5**: 100 Mb/s
- **Cat5E**: 1 Gb/s
- **Cat6**: 1 Gb/s
- **Cat6A**: 10 Gb/s
- **Cat7**: 10 Gb/s
- **Cat7A**: 10 Gb/s

### Fibra Óptica

La fibra óptica utiliza luz para transportar información a través de filamentos de vidrio o plástico muy delgados. Permite velocidades de transmisión extremadamente altas y es menos susceptible a interferencias en comparación con los cables de cobre. Substituyo al cable coaxial con la reducción de su coste.

### PLC (Power Line Communication)

PLC utiliza la red eléctrica existente para la transmisión de información. Muy comodo y facil de usar pero muy supseptible a iteferencias, requiere una red eléctrica "moderna".

## No Guiados

Los señales se transmiten sin confinar, por ejemplo, a través del aire.

### Infrarrojos

Utilizados sobre todo en comunicaciones de corto alcance. Uso poco frecuente

### Microondas

Aquí se podrían incluir tecnologías bien conocidas como WiFi y Bluetooth.

### Satélites

Utilizados principalmente para la realización de enlaces punto a punto, aunque también pueden ser alquilados para el establecimiento de redes privadas.

# DHCP

El DHCP, o Protocolo de Configuración Dinámica de Host, es un protocolo que permite la asignación automática de direcciones IP a dispositivos en una red. Cuando un dispositivo se une a una red y está configurado para obtener su dirección IP de manera automática a través de DHCP, sigue un proceso de cuatro pasos:

1. DHCP Discovery: El dispositivo envía una solicitud DHCP Discovery a la red. Esta solicitud se envía con una dirección IP de origen 0.0.0.0 y una dirección IP de destino 255.255.255.255, indicando que está buscando un servidor DHCP en la red.

2. DHCP Offer: Si hay un servidor DHCP en la red, este responde con una oferta DHCP (DHCP Offer), que contiene una propuesta de configuración IP para el dispositivo. La dirección IP de origen de esta oferta es la del servidor DHCP, y la dirección IP de destino puede variar dependiendo del servidor DHCP utilizado. En algunos casos, como en servidores Linux ISC, la dirección de destino puede ser la IP ofrecida al cliente en lugar de 255.255.255.255, ya que se usa para convertir la conversación en unicast en lugar de multicast.

3. DHCP Request: El dispositivo DHCP selecciona una de las ofertas recibidas y envía una solicitud DHCP (DHCP Request) al servidor DHCP correspondiente, indicando que acepta la oferta específica. Esta solicitud también se envía con una dirección IP de origen 0.0.0.0 y una dirección IP de destino 255.255.255.255.

4. DHCP ACK: Finalmente, el servidor DHCP confirma la operación enviando un mensaje DHCP ACK al dispositivo, indicando que la configuración IP ha sido aceptada. Al igual que en los pasos anteriores, la dirección IP de origen es la del servidor DHCP y la dirección IP de destino puede ser la IP ofrecida al cliente o 255.255.255.255, dependiendo del servidor DHCP utilizado.

<p align="center">
  <img src="https://manuais.pages.iessanclemente.net/plantillas/daw/si/sistemas_informaticos/06_redes/03_dhcp/images/DHCP.jpg" />
  <img src="https://manuais.pages.iessanclemente.net/plantillas/daw/si/sistemas_informaticos/06_redes/03_dhcp/images/wireshark.png">
</p>

Este proceso permite que los dispositivos obtengan automáticamente una configuración IP válida al unirse a una red, lo que facilita la administración y configuración de redes, especialmente en entornos grandes o dinámicos.

# Práctica DHCP



# DOMINIOS

# DNS

# ACTIVE DIRECTORY
