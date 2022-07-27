# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese primero su nombre y luego su apellido
# Capture ambos datos e imprima su nombre completo
print('Ingrese por consola su nombre/s:')
nombre = str(entrada())

print('Ingrese por consola su apellido/s:')
apellido = str(entrada())

# Imprima su nombre completo
print( ¨su nombre completo es:¨ , nombre , apellido )
# Almacenar su nombre completo en una variable
# nombre_completo = .....
nombre_completo = nombre + apellido
# Imprimir la cantidad de letras que posee su nombre completo
# cantidad_letras = len(....)
nombre_completo_len = len ( nombre_completo )
print( ¨su nombre completo posee¨ , nombre_completo_len , ¨letras¨)