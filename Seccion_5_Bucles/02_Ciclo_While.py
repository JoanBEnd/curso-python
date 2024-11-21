"""
El ciclo While a diferencia del For donde su ciclo termina de recorrer ciertos 
elementos dentro de un rango, cadena lista,etc.
EL ciclo while se basa en que mientras no se cumpla una condicion en especifica 
este se va a seguir ejecutando.

while  a < 10:
    #ejecutar codigo

Ejemplo    
"""

mi_numero = 1
total = 10

while mi_numero <= total:
    print(mi_numero)
    mi_numero += 1
"""
Lo que estamos haciendo acá es:
    Mientras que la condición de la variable "mi_numero" sea menor o igual al "total", el while
    se va a ejecutar.
    Entonces cuando ingresa al while imprime el valor y luego a la variable "mi_numero" le sumamos 1.
    Esto hara que mi_numero ya no sea 1 sino 2 y vuelve a ejecutar el ciclo while volviendo
    a comparar y esto va a seguir hasta que la variable mi_numero llegue a 11 y porque 11 y no 10
    porque si es 10 va a validar la condicion y lo dejará seguir porque la condicion indica <=,
    entonces cuando sea 11 la condicion del while ya no se cumple y ya no se vuelve a ejecutar
    el código que se encuentra internamente en el while.
"""

"""
A tener en consideracion:
 nosotros tambien podemos tener un :
    while True:
        #ejecutar código
Ejemplo
"""
#while True:
#    print("imprmir -- 1")
    
 
"""
En estos casos si hay un codigo de esta forma lo que sucederá es que elc odigo se ejecutará
de manera infinita y nunca terminará de ejecutarse.
Esto es un problema porque puede generar errores en el codigo o que el proyecto no correa de 
manera correcta.

Para ello podemos aplicar un break, el cual permita romper ese ciclo
"""

a = 1
while True:
    if a > 10:
        break
    else:
        print(f"el valor es: {a}")
        a += 1