puertos = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    631: "IPP" 
}

for puerto in puertos:
    print("Puerto", puerto, "→", puertos[puerto])


# Este script define un diccionario donde cada puerto está asociado a un servicio (por ejemplo, 22 → SSH). Luego recorre ese diccionario con un bucle y muestra por pantalla cada puerto junto con su servicio correspondiente.
