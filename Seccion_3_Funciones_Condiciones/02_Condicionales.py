"""
Las condicionales permiten controlar el flujo del programa al evaluar ciertas condiciones 
o expresiones. Si una condición se cumple (es decir, si la expresión es verdadera), el código
dentro de esa condición se ejecuta; de lo contrario, se omite o se ejecuta otra parte del código 
definida por el programador. Esto hace que el código sea más flexible y fácil de leer, ya que diferentes
acciones pueden realizarse según las circunstancia

    if condición:
        # código que se ejecuta si la condición es verdadera
    elif otra_condición:
        # código para una segunda opción
    else:
        # código que se ejecuta si ninguna condición anterior se cumple
"""

def calcular_promedio(parametro):
    if type(parametro) == dict:
        promedio_cal = sum(parametro.values()) / len(parametro)
    else:
        promedio_cal = sum(parametro) / len(parametro)
    
    return promedio_cal

##Lo que hace esta funcion es lo siguiente:
##En la primera linea de codigo valida el tipo de datos =>  if type(parametro) == dict:
##Si eso se cumple entonces se ejecuta el codigo de calculo correspondiente a un diccionario =>  promedio_cal = sum(parametro.values()) / len(parametro)
##En cambio si no se cumple ello ejecuta el siguiente codigo de la suma =>  promedio_cal = sum(parametro) / len(parametro)

parametro = [1, 4, 5, 6]
primer_resultado = calcular_promedio(parametro)
print(primer_resultado)



parametro ={"Maria": 15,
            "Pablo": 17,
            "Renato": 14
            }
segundo_resultado = calcular_promedio(parametro)
print(segundo_resultado)



parametro = (3, 4, 5, 6)
primer_resultado = calcular_promedio(parametro)
print(primer_resultado)


"""
Vamos a realizar algunos ejercicios:

"""

x = 10
 
if x == 10:
    print("Yes")
else:
    print("No")


y = 20
z = 10

#Se puede hacer mas de una validacion en una condición:

if y == 20 and z == 10:
    print("cumple con la codición")
else:
    print("No cumple la condición")


#Usando condiciones con valores booleanos
bool_va = True

if bool_va:
    print("Esta validación es verdadera")
else:
    print("Esta validación no es verdadera")

bool_pe = False

if bool_pe:
    print("Esta validación es verdadera")
else:
     print("Esta validación no es verdadera")






"""
-------------Ejercicios-------------

Caliente o Frío (E)
Defina una función que:

(1) toma una temperatura como parámetro
(2) devuelve "Cálido" si la temperatura es superior a 7
(3) devuelve "Frío" si la temperatura es igual o inferior a 7
Si llamara a su función con temp(10), devolvería Warm. Si lo llamo con temp(7) o temp(5), devolverá Cold en ambos casos, y así sucesivamente.
"""     




"""
-------------Ejercicios-------------

Defina una función que:

(1) toma una cadena como parámetro
(2) devuelve False si la cadena contiene menos de 8 caracteres
(3) devuelve Verdadero si la cadena contiene 8 o más caracteres
En otras palabras, si llamo a su función con foo("mypass") devolverá False. Si lo llamé con foo("mylongpassword") devolvería True, y así sucesivamente.
"""




