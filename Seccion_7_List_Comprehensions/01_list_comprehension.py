
"""
Las list comprehensions, nos permite más que todo crear nuevas
listas usando el ciclo for, pero con la diferencia de un ciclo for
normal, es que la list comprehension se crea en una sola linea.

"""

def devolver_suma(lista_completa):

    resultado = sum([float(elemento) for elemento in lista_completa])
    return resultado 
    

print(devolver_suma(['1.2', '2.6', '3.3']))    






