Este script en Python analiza logs SSH y distingue entre intentos fallidos y accesos correctos.
Permite entender de forma básica cómo detectar actividad sospechosa.

logs = [
    "Failed password for root from 192.168.1.10",
    "Failed password for root from 192.168.1.10",
    "Accepted password for user from 192.168.1.20",
    "Failed password for root from 192.168.1.10"
]

contador = {}

for linea in logs:
    if "Failed" in linea:
        ip = linea.split()[-1]
        contador[ip] = contador.get(ip, 0) + 1

for ip in contador:
    print("IP:", ip, "- Intentos fallidos:", contador[ip])
