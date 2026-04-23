# Definimos la altura del triangulo
n = 5

# Iniciamos un bucle para recorrer cada fila
for i in range(1, n + 1):
    # Calculamos los espacios necesarios para centrar el triangulo
    espacios = " " * (n - i)
    
    # Definimos las estrellas con un espacio para mejorar la forma visual
    estrellas = "* " * i
    
    # Imprimimos la linea combinando espacios y estrellas
    print(espacios + estrellas)

# Explicacion del codigo:
# 1. El bucle for recorre del 1 al valor de n.
# 2. Los espacios disminuyen en cada fila para empujar las estrellas al centro.
# 3. Al usar "* ", el triangulo mantiene una forma equilibrada.

# Resultado en consola:
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * *
