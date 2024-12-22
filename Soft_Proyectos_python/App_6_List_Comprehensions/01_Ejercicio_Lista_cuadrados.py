
#Lista de Cuadrados:
# Dado un número entero n, genera una lista que contenga los cuadrados de los números del 1 al n.
#Input: Ingrese un número: 5
#Output: [1, 4, 9, 16, 25]


def lista_cuadrado(numero):
#usando la list comprehensions recorremos y elevamos al cuadrado
    return [item**2 for item in range(1, numero+1)]



mi_numero = int(input("Ingrese un número: "))

resultado_lista = lista_cuadrado(mi_numero)
print(f"La lista de cuadrados resultante es: {resultado_lista}")

    
