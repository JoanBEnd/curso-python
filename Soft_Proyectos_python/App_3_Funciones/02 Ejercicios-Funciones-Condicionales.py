#Crea una funcion donde pasemos como parametro una lista y esta me filtre solo los
#numeros pares en una nueva lista

#Una primera forma y para ir practicando lo aprendido con los bucles y condicionales 

def filtrar_numeros_pares(list_numeros):
    new_list = []
    for i in list_numeros:
        if i % 2 == 0:
            new_list.append(i)
    
    return new_list




list_numbers = [1,2,54,6,43,13,87,52]

resultado = filtrar_numeros_pares(list_numbers)
print(f"Este es el resultado: {resultado}")



#segunda forma: Podemos aplicar el list comprehension

def filtro_de_pares(list_numeros):

        return [i  for i in list_numeros if i %2 == 0]


 #usando la misma lista deberiamos obtener el mismo resultado

resultado_pares = filtro_de_pares(list_numbers)
print(f"Este es el resultado con list comprehesion: {resultado_pares}")
