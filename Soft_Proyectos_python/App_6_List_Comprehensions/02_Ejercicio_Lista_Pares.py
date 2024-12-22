#Filtrar números pares
#  Dada una lista de números separados por comas, genera una lista que contenga solo los números pares.
#Input:
#Ingrese una lista de números separados por comas: 1,2,3,4,5,6,7,8
#Output
#[2, 4, 6, 8]



def lista_numeros_pares(mi_lista):

#usando la list comprehensions recorremos y validamos que sea entero

    return [ int(numero)  for numero in mi_lista if int(numero) % 2 == 0]
#nota:
#(numero % 2) esta expresion nos permite obtener el residuo de una división y si es 0 viene a ser un numero par



mi_lista = (input("Ingrese una lista de números separados por coma: "))
#convertimos la data ingresada a una lista
mi_lista = mi_lista.split(",")
resultado_lista = lista_numeros_pares(mi_lista)
print(f"La lista de numeros pares es: {resultado_lista}")

    