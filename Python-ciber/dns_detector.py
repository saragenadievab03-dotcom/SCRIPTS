# dns_detector.py

Este script en Python detecta dominios potencialmente sospechosos. 

Funciona recorriendo una lista de dominios y buscando si contienen palabras clave asociadas a intentos de phishing (como "login", "secure" o "verify"). 

Si encuentra alguna coincidencia, muestra una alerta indicando que el dominio podría ser malicioso.

#Ejemplo:

dominios = [
    "google.com",
    "gooogle-login.com",
    "facebook.com",
    "faceb00k-secure.net"
]

# palabras sospechosas
sospechosos = ["login", "secure", "verify"]

for dominio in dominios:
    for palabra in sospechosos:
        if palabra in dominio:
            print(f"ALERTA: dominio sospechoso -> {dominio}")
