"""
Los tipos de datos:
En este caso vamos a ver los tipos int, string, float

Los int: son los numeros enteros
Los string: son cadenas o cadenas de texto(que pueden estar conformado por textos y numeros)
Los float: Son los numeros decimales
A continuacion tenemos 3 variables con cada tipo de dato
"""
primer_valor = 10
segundo_valor = "20"
tercer_valor = 13.4

"""
Una vez definido los valores en cada variable veremos el resultado que se 
tiene al hacer una operacion con cada variable definida
"""


"""
En este primer ejercicio vermos que estamos sumando la variable 1 y variable 3
que es la suma de un int y un float. Como sabemos por matematica sumar un entero y un decimal
es algo comun y el resultado de este caso seria 23.4
"""
primer_resultado = primer_valor + tercer_valor
print(primer_resultado) #23.4


"""
En este segundo ejercicio veremos que estamos sumando la misma variable, pero como sabemos, esta variable es un string. 
Cuando sumamos un string, en lugar de hacer una operación matemática, lo que ocurre es una concatenación: las cadenas 
se unen formando una sola. Así que el resultado será la unión de los valores, en este caso "2020". Ojo, aunque la variable
almacene números, al ser un string no se sumarán de forma aritmética, sino que simplemente se unirán debido al tipo de dato.
"""
segundo_resultado = segundo_valor + segundo_valor
print(segundo_resultado) #2020




"""
En este tercer ejercicio, estamos intentando sumar dos variables de tipos diferentes: un entero (int) y una cadena de texto (string). 
Python interpretará esto como un error, ya que no es posible realizar operaciones aritméticas ni concatenaciones entre estos tipos de datos
 sin convertir uno de ellos.
Para resolver esto, sería necesario transformar el número a un string para concatenar, o el string a un número si se desea realizar una 
operación matemática.
"""
tercer_resultado = primer_valor + segundo_valor
print(tercer_resultado)



