# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese tres palabras y arme un acrónimo con ellas
# Si desea puede modificar el código para ingresar más palabras
print('Ingrese palabra 1: teclado')
palabra_1 = str(input())

print('Ingrese palabra 2: monitor')
palabra_2 = str(input())

print('Ingrese palabra 3: compu')
palabra_3 = str(input())

# De cada palabra debe tomar la primera letra y armar el acrónimo
# Ejemplo: Alumbrado, barrido y limpieza --> ABL
# Imprimir el resultado en pantalla
print ( palabra_1 [ 1 ] + palabra_2 [ 1 ] + palabra_3 [ 1 ])