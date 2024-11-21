"""
Listas:
Nos permite almacenar multiples datos
Las listas son mutables, es decir que se pueden modificar agregando o eliminado elementos que contiene la lista.
"""

notas_estudiantes = [15.8, 16.7, 13.4, 16.2]

"""
Usando range:
la funcion range() nos permite generar una secuencia de números donde podemos especificar 
el valor de inicio y el valor de fin. Sin embargo, es importante notar que el valor de fin 
no está incluido en la secuencia generada.
"""
lista_rango = list(range(1,11))
print(lista_rango)

"""
Adicionalmente, range() nos permite un tercer parámetro que define el "paso", es decir, 
el intervalo entre los números de la secuencia. En el siguiente ejemplo, generamos una 
secuencia que empieza en 2, termina en 12 (sin incluirlo), y avanza de 2 en 2: [2, 4, 6, 8, 10].
"""

lista_rango_saltando = list(range(2,12, 2))
print(lista_rango_saltando)

color_codes = (("green",), (True,), (2,))
print(color_codes)