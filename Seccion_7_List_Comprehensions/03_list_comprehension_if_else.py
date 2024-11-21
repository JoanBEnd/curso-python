

"""
If - else en list comprehensions:
Ahora cuando se trabaje con el if-else la estructura cambia:

        [elemento  if elemento > 0 else  0 for elemento in mi_lista]

    Por lo que:
        La condicion if else se mueve a la parte izquierda del for
        y el elemento que se va a deovlver cuando se cumple el if en la nueva lista
        se mantiene en la parte izquierda.


    Se leeria de la siguiente forma: 

    Por cada elemento en mi_lista, si el elemento es mayor que 0, devuelve el elemento; de lo contrario, devuelve 0

"""


def devolver_con_zero(lista_completa):
    
    new_lista = [elemento if type(elemento) == int else 0 for elemento in lista_completa]
    return new_lista
    

print(devolver_con_zero([69, 'Sin datos', 36, 65, 'Sin datos']))    

