# Este proyecto es un pequeño programa en Python que permite al usuario escribir una frase 
y contar cuántas palabras tiene.


print("CONTADOR DE PALABRAS")

texto = input("Escribe una frase: ")

palabras = texto.split()

print("Número de palabras:", len(palabras))


# Ejemplo:

Entrada:
Me gusta programar en Python

Salida:
Número de palabras: 5
