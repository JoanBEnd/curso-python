#Filtrar palabras largas
#Dada una lista de palabras separadas por comas y un número n, genera una lista que contenga solo las palabras cuya longitud sea mayor a n.
#Input:
#   Ingrese una lista de palabras separadas por comas: hola,python,list,comprehension,programacion
#   Ingrese el valor de n: 5
#Output:
#   ['python', 'comprehension', 'programacion']



def lista_palabras_largas(mi_lista, longitud):

#usando la list comprehensions recorremos y elevamos al cuadrado
    return [ palabra for palabra in mi_lista if len(palabra) > longitud ]



mi_lista = input("Ingrese una lista de palabras separadas por comas: ")
longitud = int(input("Ingrese la longitud: "))
mi_lista = mi_lista.split(",")

resultado_palabras_largas = lista_palabras_largas(mi_lista, longitud)
if len(resultado_palabras_largas) == 0:
    print(f"No se encontraron palabras que superen la longitud brindada.")
else:
    print(f"La lista de palabas largas: {resultado_palabras_largas}")