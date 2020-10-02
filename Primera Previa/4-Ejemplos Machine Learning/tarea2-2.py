# COMPUTACIÓN BLANDA - Sistemas y Computación
# -------------------------------------------
# Introducción a numpy
# -------------------------------------------
# Lección 02
#
# ** Técnicas de apilamiento
# ** División de arrays
# ** Propiedades de arrays
#
# -------------------------------------------

# Se importa la librería numpy

import numpy as np
# APILAMIENTO
# -----------
# Apilado
# Las matrices se pueden apilar horizontalmente, en profundidad o
# verticalmente. Podemos utilizar, para ese propósito,
# las funciones vstack, dstack, hstack, column_stack, row_stack y concatenate.
# Para empezar, vamos a crear dos arrays
# Matriz a
a = np.arange(9).reshape(3,3)
print('a =\n', a, '\n')
# Matriz b, creada a partir de la matriz a
b = a*2
print('b =\n', b)
# Utilizaremos estas dos matrices para mostrar los mecanismos
# de apilamiento disponibles

# APILAMIENTO HORIZONTAL
# Matrices origen
print("\n ---APILAMIENTO HORIZONTAL--- \n")
print('a =\n', a, '\n')
print('b =\n', b, '\n')
# Apilamiento horizontal
print('Apilamiento horizontal =\n', np.hstack((a,b)) )

# APILAMIENTO HORIZONTAL - Variante
# Utilización de la función: concatenate()
# Matrices origen
print("\n APILAMIENTO HORIZONTAL - Variante \n")
print('\n a =\n', a, '\n')
print('b =\n', b, '\n')
# Apilamiento horizontal
print( 'Apilamiento horizontal con concatenate = \n',
np.concatenate((a,b), axis=1) )
# Si axis=1, el apilamiento es horizontal
#------------------------------------
print( 'Prueba, Apilamiento horizontal con concatenate = \n',
np.concatenate((a,b)) )
#Si no se le pone axist=1, el apilamiento se comporta como un apilamiento vertical


# APILAMIENTO VERTICAL
# Matrices origen
print("\n ---APILAMIENTO VERTICAL--- \n")
print('a =\n', a, '\n')
print('b =\n', b, '\n')
# Apilamiento vertical
print( 'Apilamiento vertical =\n', np.vstack((a,b)) )


# APILAMIENTO VERTICAL - Variante

# Utilización de la función: concatenate()
# Matrices origen
print("\n ---APILAMIENTO VERTICAL - Variante--- \n")
print('a =\n', a, '\n')
print('b =\n', b, '\n')
# Apilamiento vertical
print( 'Apilamiento vertical con concatenate =\n',
np.concatenate((a,b), axis=0) )
# Si axis=0, el apilamiento es vertical
print( 'Prueba, Apilamiento vertical con concatenate =\n',
np.concatenate((a,b)) )

# APILAMIENTO EN PROFUNDIDAD

# En el apilamiento en profundidad, se crean bloques utilizando
# parejas de datos tomados de las dos matrices
# Matrices origen
print("\n ---APILAMIENTO EN PROFUNDIDAD--- \n")
print('\n a =\n', a, '\n')
print('\n b =\n', b, '\n')
# Apilamiento en profundidad
print( 'Apilamiento en profundidad =\n', np.dstack((a,b)) )
#Apila el primer valor del bloque 0 fila 0 columna 0, con el primer valor del bloque 1 fila 0 columna 0,
#Luego, el valor del bloque 0 fila 0 columna 1, con el valor del bloque 1 fila 0 columna 1 y asi sucesivamente...

# APILAMIENTO POR COLUMNAS

# El apilamiento por columnas es similar a hstack()
# Se apilan las columnas, de izquierda a derecha, y tomándolas
# de los bloques definidos en la matriz
# Matrices origen
print("\n ---APILAMIENTO POR COLUMNAS--- \n")
print('a =\n', a, '\n')
print('b =\n', b, '\n')
# Apilamiento vertical
print( 'Apilamiento por columnas =\n',
np.column_stack((a,b)) )


# APILAMIENTO POR FILAS

# El apilamiento por fila es similar a vstack()
# Se apilan las filas, de arriba hacia abajo, y tomándolas
# de los bloques definidos en la matriz
# Matrices origen
print("\n ---APILAMIENTO POR FILAS--- \n")
print('a =\n', a, '\n')
print('b =\n', b, '\n')
# Apilamiento vertical
print( 'Apilamiento por filas =\n',
np.row_stack((a,b)) )

# DIVISIÓN DE ARRAYS

# Las matrices se pueden dividir vertical, horizontalmente o en profundidad.
# Las funciones involucradas son hsplit, vsplit, dsplit y split.
# Podemos hacer divisiones de las matrices utilizando su estructura inicial
# o hacerlo indicando la posición después de la cual debe ocurrir la división


# DIVISIÓN HORIZONTAL
print("\n ---DIVISIÓN HORIZONTAL--- \n")
print('Matriz a= \n', a, '\n')
# El código resultante divide una matriz a lo largo de su eje horizontal
# en tres piezas del mismo tamaño y forma:
print('Array con división horizontal =\n', np.hsplit(a, 3), '\n')
# El mismo efecto se consigue con split() y utilizando una bandera a 1
print('Array con división horizontal, uso de split() =\n',
np.split(a, 3, axis=1))
#Cuando axist=1 se hace de forma horizontal


# DIVISIÓN VERTICAL
print("\n ---DIVISIÓN VERTICAL--- \n")
print('Matriz a= \n', a, '\n')
# La función vsplit divide el array a lo largo del eje vertical:
print('División Vertical = \n', np.vsplit(a, 3), '\n')
# El mismo efecto se consigue con split() y utilizando una bandera a 0
print('Array con división vertical, uso de split() =\n',
np.split(a, 3, axis=0))
#Cuando axist=0 se hace de forma vertical

# DIVISIÓN EN PROFUNDIDAD
print("\n ---DIVISIÓN EN PROFUNDIDAD--- \n")
# La función dsplit, como era de esperarse, realiza división
# en profundidad dentro del array
# Para ilustrar con un ejemplo, utilizaremos una matriz de rango tres
c = np.arange(27).reshape(3, 3, 3)
print("Matriz c= \n", c, '\n')
# Se realiza la división
print('División en profundidad =\n', np.dsplit(c,3), '\n')

# PROPIEDADES DE LOS ARRAYS
print("\n ---PROPIEDADES DE LOS ARRAYS--- \n")
# El atributo ndim calcula el número de dimensiones
print("Matriz b = \n", b, '\n')
print('Numero de dimensiones (ndim): ', b.ndim)
print('Numero de dimensiones (ndim): ', a.ndim)
print('Numero de dimensiones (ndim): ', c.ndim)


# El atributo size calcula el número de elementos

print("Matriz b = \n", b, '\n')
print('Numero de elementos (size): ', b.size)


# El atributo itemsize obtiene el número de bytes por cada
# elemento en el array
print('Numero de bytes por cada elemento en el array (itemsize): ', b.itemsize)


# El atributo nbytes calcula el número total de bytes del array

print(b, '\n')
print('Total de bytes del array (nbytes): ', b.nbytes, '\n')
# Es equivalente a la siguiente operación
print('nbytes equivalente: ', b.size * b.itemsize)

# El atributo T tiene el mismo efecto que la transpuesta de la matriz

b.resize(6,4)
print("Nueva Matriz b = \n", '\n')
print('Transpuesta: \n', b.T)

# Los números complejos en numpy se representan con j

b = np.array([1.j + 1, 2.j + 3])
print('Complejo: ', b)


# El atributo real nos da la parte real del array,
# o el array en sí mismo si solo contiene números reales
print('real: ', b.real, '\n')
# El atributo imag contiene la parte imaginaria del array
print('imaginario: ', b.imag, '\n')


# Si el array contiene números complejos, entonces el tipo de datos
# se convierte automáticamente a complejo
print(b.dtype)


# El atributo flat devuelve un objeto numpy.flatiter.
# Esta es la única forma de adquirir un flatiter:
# no tenemos acceso a un constructor de flatiter.
# El iterador nos permite recorrer una matriz
# como si fuera una matriz plana, como se muestra a continuación:
# En el siguiente ejemplo se clarifica este concepto
b = np.arange(4).reshape(2,2)
print("Nueva matriz b = \n", b, '\n')
f = b.flat
print(f, '\n')
# Ciclo que itera a lo largo de f
for item in f: print (item)
# Selección de un elemento
print('\n')
print('Elemento 2: ', b.flat[2])
# Operaciones directas con flat
b.flat = 7
print(b, '\n')
b.flat[[1,3]] = 1
print(b, '\n')


