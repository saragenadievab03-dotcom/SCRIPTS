# Calculadora simple en Python con operaciones de suma y resta

print("CALCULADORA SIMPLE")
print("1. Sumar")
print("2. Restar")

opcion = input("Elige opción (1 o 2): ")

num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))

if opcion == "1":
    print("Resultado:", num1 + num2)

elif opcion == "2":
    print("Resultado:", num1 - num2)

else:
    print("Opción no válida")
