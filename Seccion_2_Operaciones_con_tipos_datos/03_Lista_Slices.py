"""
Ya hemos visto como acceder a un valor en especifico de una lista
usando el indice.
Ahora veremos como acceder a una porcion de la lista, para ello
Para acceder a una porción de una lista en Python, se usa la notación de "slicing" con la estructura [inicio:fin]. Esta notación nos permite seleccionar elementos desde una posición inicial hasta una posición final, excluyendo el último índice especificado:
[inicio:fin]: selecciona los elementos desde el índice inicio hasta el índice fin - 1.
Si inicio no se especifica, la selección empieza desde el primer elemento (0).
Si fin no se indica, incluye todos los elementos hasta el final de la lista.
"""

mi_serie = [14, 546, 78, 34, 85, 56]

#digamos que quiero los 3 primeros numeros, seria:
print(mi_serie[0:3])
#resultado: [14, 546, 78]
#Entonces esto nos indica que partimos de la posición 0 y hasta antes de la posicion 3,

#otros ejemplos
#que sucede si solo uso esta forma [:]
print(mi_serie[:])
#resultado: [14, 546, 78, 34, 85, 56] 
#nos vuelve a traer la lista origninal, ya que al no definir un inicio y fin python por defecto asume el inicio = 0 y el fin = la ultima posicion de la lista

print(mi_serie[3:])
#resultado: [34, 85, 56]
#en este caso definimos el inicio que es la posicion 3 y fin como no se definió toma automaticamente la posicion final de la lista

print(mi_serie[: 2])
#resultado: [14, 546]
#en este caso  el inicio que no tiene un indice lo asume como 0  y fin  tiene definido = 2


##  USANDO INDICES NEGATIVOS
"""
Cuando se trata de indices de numeros negativos estos se contaran desde el final al inicio
"""

print(mi_serie[-1])
#resultado 56
#En este caso el 56 que es el ultimo numero es obtenido por el -1

#entonces usando otro ejemplo seria
print(mi_serie[-3:-1])
#resultado [34, 85], tu diras porque no tomael numero 56, esto es porque el ultimo elemento es exclusivo no entra dentro del rango establecido
#si quieres que se incluya el 56 tendrias que hacerlo de la siguiente forma
print(mi_serie[-3:])
#[34, 85, 56]
print(mi_serie[-3:-3])

print(['abc' , 'def', 'ghi', 'jkl', 'mno'][-2][-2])