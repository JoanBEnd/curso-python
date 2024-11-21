"""
En esta sección hemos aprendido a:
    Que la list comprehensions es una expresión
    que nos permite crear una lista iterando
    a partir de contenedor
"""
 
#lista:
mi_lista = [15, 56, -15, 12, 35, -12]

print([elemento / 10 for elemento in mi_lista])

"""
Tambien hemos aprendido a usar la list comprehension con if y
"""


print([elemento * -1 for elemento in mi_lista if elemento < 0])


"""
y hemos aprendido a usar la list comprehension con if and else
"""

print([elemento if elemento > 0 else elemento * -1  for elemento in mi_lista])