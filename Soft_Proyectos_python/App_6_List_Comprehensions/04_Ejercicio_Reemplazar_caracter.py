#Reemplazar caracteres en palabras
#Problema: Dada una lista de palabras separadas por comas, genera una nueva lista reemplazando todas las vocales con un asterisco (*).
#Input:
#   Ingrese una lista de palabras separadas por comas: hola,python,ejemplo
#Output:
#   ['h*l*', 'pyth*n', '*j*mpl*']

def lista_reemplazada(mi_lista):
#Para este ejercicio usaremos listas de comprehension anidadas
#esto quiere decir una list comprehension dentro de otra list comprehensions
#El primer list comprehension recorre la lista de cada palabra
#el segundo list comprehension recorre cada palabra obteniendo la letra y luego comparando para ver cual es una vocal y reemplazar por el *
#el segundo list comprehension va dentro de la función join para poder unir esa palabra con los * reemplazados.

    return [ "".join("*" if letra in "aeiou" else letra for letra in palabra) for palabra in mi_lista]

mi_lista = input("Ingrese una lista de palabras separadas por comas: ")
mi_lista = mi_lista.split(",")

resultado = lista_reemplazada(mi_lista)
print(f"El resultado de reemplazadar caracteres es: {resultado}")