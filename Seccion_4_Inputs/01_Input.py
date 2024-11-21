"""
Hasta ahora hemos venido ejecutando funciones llamando 
a la funcion de la siguiente manera: 
    print(mi_temperatura(15))
Con el cual nos mostraba el resultado en pantalla y teniamos que cambiar
el valor de temperatura en el mismo código.

Con la funcion input lo que podemos hacer es interactuar con nuestro codigo
desde la terminal. Para ello crearemosla funcion de validar temperatura
y veremos como hacer el uso de la funcion input

"""

def validar_temperatura(parametro):
    if parametro > 20:
        return "Calor"
    else:
        return "Frio"
    

#El input viene a ser como una caja donde ingresamosla temperatura que queremos validar
#Ese input lo asigamos a una variable para que esta pueda ser usada en la funcion
mi_temperatura = input("Ingrese la temperatura:")


print(validar_temperatura(mi_temperatura))

"""
Ahora tal cual esta este codigo desarrollado y ejecutamos el programa
En la terminal nos pedira ingresar el varlo de la temperatura y despues de ingresar
persionamos Enter, para que pueda ejecutar la función
"""

"""
Bien, pues al dar enter para ejecutar el código, nos mostrará un error en pantalla 

    if parametro > 20:
       ^^^^^^^^^^^^^^
TypeError: '>' not supported between instances of 'str' and 'int'

Esto que nos dice:
Que el valor ingresado es un str y no se puede comparar o validar en la condicion if un str con un int
porque son tipos distintos.

Ahora te preguntarás porque sale ese error si tu has ingresado correctamente el numero digamos 15 y
te cuestionas de que es un numero y no un string.

Pues para python al inrgesar un numero en un input este lo considera como un string y no un numero, ya que
podemos ingresar distintos tipos de datos desde el input y siempre el input por defecto lo tomará como un string

Entonces que podemos hacer:
Pues la solución seria convertir ese input en un float para este caso

    
    ===== Esto lo veremos en el siguiente archivo 01.01_Input_solucionado.py ======
    ===== Esto lo veremos en el siguiente archivo 01.01_Input_solucionado.py ======
"""