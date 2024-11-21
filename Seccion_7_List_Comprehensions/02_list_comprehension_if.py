
"""
If en list comprehensions:
Tambien se puede considerar una condicion dentro de una list comprehensions
y la estructura es la siguiente:

        [elemento for elemento in mi_lista if elemento > 0]

    Por lo que:
        La condicion se estructura en la parte derecha del for
        y el elemento que se va a deovlver en la nueva lista
        se mantiene en la parte izquierda.

"""


def retornar_enteros(lista_completa):
        
    new_list = [elemento for elemento in lista_completa if type(elemento) == int]    
    return new_list


print(retornar_enteros([56, 'Sin datos', 23, 15, 'sin datos']))








def numeros_enteros(lista_completa):
    
    new_list = [elemento for elemento in lista_completa if elemento > 0]
    return new_list
    

print(numeros_enteros([-15, 34, -21, 21]))
