# dns_detector.py

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
