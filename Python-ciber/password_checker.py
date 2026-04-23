# Password Checker 

Este es un script básico en Python que verifica si una contraseña es lo suficientemente larga.

# Cómo funciona

- Si la contraseña tiene 6 o más caracteres → aceptable
- Si tiene menos → es muy corta

 # Ejemplo
  
  password = input("Escribe tu contraseña: ")

if len(password) >= 6:
    print("Contraseña aceptable")
else:
    print("Contraseña muy corta")
