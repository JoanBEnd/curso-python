
nuevas_temperaturas = [14, 16, 18, 21]

"""
si consultamos el comando dir(list), nos mostrara una serie de atributos o metodos especiales del objeto list, de los cuales nosotros
debemos enfocarnos en los que estan en la ultima linea dentro del [] que son los que mas se utilizan comunmente
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
 '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__',
  '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', 
'__sizeof__', '__str__', '__subclasshook__', 
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
"""

"""
N°1
Para ello usaremos los metodos
append: Nos permite agregar un nuevo elemento y se expresa de la siguiente forma:
hagamos uso de variables para ir practicando
"""

new_t = 17 #declaramos la variable con la nueva temperatura a agregar
nuevas_temperaturas.append(new_t)
print(f"La nueva temperatura agregada es {new_t}: {nuevas_temperaturas}")


"""
N°2
index: Nos permite saber la ubicación de un valor que esta en la lista
hagamos uso de variables para ir practicando
"""

search_temp = 21
ubicacion = nuevas_temperaturas.index(search_temp)
print(f"el número {search_temp} se encuentra en la posición: {ubicacion}")

#En este caso nos muestra que la ubicacion es en la posición 3 ya que el index se comienza a contar desde la posición 0
"""
Que quiere decir esto, que dentro de la lista [14, 16, 18, 21] en la posición 0 esta el número 14, en la posición 1 esta el
número 16 y asi  sucesivamente.
"""


"""
N°3
pop: Nos permite eliminar un registro de lista que por defecto está al ultimo.
"""
#De esta forma se puede eliminar el ultimo registro de la lista:

nuevas_temperaturas.pop()

#Lo que tambien se puede hacer es capturar ese elemento que se esta eliminando y almacenarlo en otra variable
#De la siguiente forma

del_element = nuevas_temperaturas.pop()
print(f"El elemento eliminado es {del_element} y la lista quedaria así: {nuevas_temperaturas}")


"""
Con pop() tambien podemos eliminar un numero de lista pasandole el indice

"""
secuencia_numbers = [2,4, 6, 8, 10, 12]
secuencia_eliminada = secuencia_numbers.pop(3) #indice 3 que es la posición donde se encuentre ese numero
print(f"El numero de la secuencia eliminada es {secuencia_eliminada} y la lista de la secuencia quedaria así: {secuencia_numbers}")





"""
N°4
remove: Remueve la primera aparicion de un elemento de la lista que le definimos para ser borrado, si existe mas de un mismo de elemento solo elimina el primero

"""
notas_academicas = [15.4, 16.9, 14.5, 19.8]
notas_academicas.remove(16.9)#Especificamos que nota eliminar
print(f"La lista quedaria así: {notas_academicas}")

"""
En este ejercicio tenemos un numero repetido que es 18 y si queremos remover quitara el primero que encuentro revisando de izquierda a derecha
"""
numeros_aleatorios = [17, 18, 20, 18, 26, 15]
numeros_aleatorios.remove(18)
print(f"La lista de los numeros aleatorios queda así: {numeros_aleatorios}") # => [17, 20, 18, 26, 15]
