"""
Continuando con la solución del problema
Copiamos todo el código del archivo anterior y haremos la correción
"""


def validar_temperatura(parametro):
    if parametro > 20:
        return "Calor"
    else:
        return "Frio"
    

mi_temperatura = int(input("Ingrese la temperatura:")) #aquí estamos convirtiendo el valor ingresado en el input a float


print(validar_temperatura(mi_temperatura))

"""
Si ejecutamos este código nos pedirá ingresar una temperatura, ahora si ingresamos el valor
y después de darle Enter, nos mostrará el resultado dependiendo del valor que ingresaste

Ahora porqué le asignamos o convertirmos a un float y no a un int (que es entero)
bueno la respuesta es la siguiente:
Porque si tú en el input donde te solicita ingresar un valor le pones 17.6, 14.2, etc, que
son números decimales y en el codigo lo quieres convertir a entero :

        int(input("Ingrese la temperatura:"))

Te saldrá un error, porque no podra convertir ese valor a entero, haciendo el cambio y probandolo el error es el siguiente:

     mi_temperatura = int(input("Ingrese la temperatura:")) 
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ValueError: invalid literal for int() with base 10: '17.5'

Por eso para solucionar este caso y cuando se trabaje con números y la lógica del negocio permita o deje abierta la opción 
de no solo trabjar con enteros sino con decimales seria mejor hacer la conversion de ese input en float(
)
Si la lógica de negocio es estricta y te indica que es sólo números enteros entonces si se puede hacer la conversión a int()
"""