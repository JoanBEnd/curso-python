"""
Las funciones son una parte importante dentro de la programación,
ya que nos ayudan a darle mejor legibilidad y estructura al código, 
dividiéndolo en tareas específicas y reutilizables.

En que consiste una funcion:
Una función encapsula una porción de código que realiza una tarea específica y nos
permite llamarla en cualquier parte del programa cuando sea necesario.

La estructura de una función en python es la siguiente:
    
        def nombre_funcion(param1, param2):

1. Palabra clave: La palabra def inicia la definición de la función.

2. Nombre de la función: El nombre debe describir claramente lo que hace la función para facilitar su comprensión.

3. Parámetros: Los paréntesis () pueden contener uno o más parámetros, que actúan como variables que la función utiliza para recibir datos externos y
    trabajar con ellos.
    *Los parámetros son opcionales; una función puede no requerir parámetros si la tarea que realiza no los necesita.

4. Cuerpo de la función: Después del : se indenta el código que se ejecutará cuando la función sea llamada. Aquí se establecen las operaciones 
    o instrucciones que llevará a cabo.
    IDENTAR: significa dar espacio entre una linea de codigo y la siguiente

Veremos un ejemplo
"""

def calcular_suma(param1, param2):
    sumatoria = param1 + param2
    return sumatoria
"""
En la funcion que tenemos arriba se está haciendo lo siguiente:
    Calcular la suma de 2 numeros
    Como sé que son 2 numeros?
        Bueno, es por los parametros que estoy definiendo dentro del parentesis.
    Ahora vemos una palabra nueva que es return, que significa esto?
        Pues el return, lo que hace es devolver el resultado del calculo de la suma
        Cada vez que se use o se llame una funcion esta contiene un "return" que es el quenos devuelve el resultado 
        para poder usarlo dentro de nuestro codigo general o para mostrar pantalla el resultado.

Sigamos viendo como funciona esta funcion valga la redundancia
"""

resultado_suma = calcular_suma(15, 17)
"""
Lo que estamos haciendo en la linea de arriba es lo siguiente:
primero creamos una variable a la cual le asignamos la funcion calcular_sum()
esta variable resultado_suma almacenara el resultado que se obtenga al ejecutar la funcion calcular_suma()
"""

print(resultado_suma)
"""
Y para el ver el resultado imprimimos esa variable
"""

"""
Como podria mejorar esto
"""
#declaramos variables, que van a contener los numeros a sumar y estas variables
#son las que pasamos por la funcion calcular_suma
primer_numero = 15
segundo_numero = 17

resultado_suma = calcular_suma(primer_numero, segundo_numero)
print(resultado_suma)

"""
En programación real, los valores que pasan a una función generalmente son variables y no números o string, etc directos, para hacer
el código más flexible y reutilizable
"""



"""
A continuacion dejo algunos ejercicios para desarrollar
"""

"""
----------------- EJERCICIO 1--------------

Define una función que calcule el área de un cuadrado.

Por ejemplo, si llamara a su función con area_cuadrado(5), la salida sería 25. Si la llamara con area_cuadrado(8), devolvería 64, y así sucesivamente.
Tenga en cuenta que no es necesario que nombre su función area_cuadrado. Dale el nombre que quieras.

Guia:
Si quieres elevar al cuadrado en python es de la siguiente forma: 5**2
"""






"""
----------------- EJERCICIO 2--------------

Defina una función que convierta onzas líquidas a mililitros sabiendo que 1 onza líquida es igual a 29,57353 mililitros. Por ejemplo, 
si llamara a su función con convertir(1) obtendría un resultado de 29.57353. Si lo llamara con convertir(5) obtendría 147.86765, y así sucesivamente.

Guia:
ya sabemos que 1 onza = 29,57353 =>  quiere  decir que vas a necesitar este valor siempre para que cualquier numero que pases
a la funcion lo uses para convertirlo a mililitros
"""

