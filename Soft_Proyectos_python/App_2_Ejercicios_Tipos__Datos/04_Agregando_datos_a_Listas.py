#Agrega el siguiente elemento "Salazar"
#a la lista apellidos

apellidos = ["Martinez", "Perez", "Carranza"]
apellidos.append("Salazar")
print(apellidos)



#Agrega el siguiente apellido "Saldarriaga"
#en la posicion 1 de la lista ya creada

apellidos.insert(1,"Saldarriaga")
print(apellidos)


#eliminar el numero 287
numeros = [4,6,9,3,23,56,287,123]

#Primera forma
del numeros[6]

#eliminar el numero 4
#Segunda forma

numeros.pop(0)

print(numeros)


#Agregar la list1 a la list2

list1 = [486512, 455567, 24894]
list2 = [993]

lista_final = list2 + list1
print(lista_final)


#Agregar el ultimo item de la list1 a la list2

list2.append(list1[-1])
print(list2)



#concatenar el primer elemento y el 10 elemento de la lista y almacenarlo en una nueva variable
mylist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

result = mylist[0] + mylist[9]
print(result)