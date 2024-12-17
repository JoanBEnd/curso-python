#Crea una función que permita ingresar un numero n y me genere los primeros n números de la secuencia de Fibonacci.

#Seccion de la función
def secuencia_fibonacci(numero):
    
    #Por defecto tenemos armado las 2 primeros número del fibonacci.    
    lista_fibonacci = [0, 1]
    
    #Aca recorremos la lista_fibonacci donde obtendremos los 2 ultimos numeros para poder crear el nuevo numero de la lista fibonacci mediante una suma
    #La cual la estamos agregando a la lista_fibonacci con el metodo append()
    for i in range(2, numero):       
        penultimo = int(lista_fibonacci[-2] )
        ultimo = int(lista_fibonacci[-1])

        lista_fibonacci.append(penultimo + ultimo)

    #una vez terminado el recorrido devolvemos el resultado para mostrarlo en consola
    return lista_fibonacci


# Seccion de entrada
try:
    #Ingresamos el numero que nos solicita por consola
    numero_fibonacci = int(input("Por favor ingrese el número para generar la secuencia fibonacci: "))
    
    #Aplicamos las validaciones, en donde solicitamos que el valor ingresado sea un numero entero
    if type(numero_fibonacci) != int:
        print(f"El valor ingresado no es un número, volver a intentar")
    #Otra validacion es que el numero no sea negativo y/o igual a 0
    elif int(numero_fibonacci) <= 0:
        print(f"El numero ingresado es menor o igual a 0")
    else:
    #Cuando se cumplan las condiciones recien podemos a consultar la función
        resultado_fibonacci = secuencia_fibonacci(int(numero_fibonacci))
        print(f"El resultado de la secuencia fibonacci es: {resultado_fibonacci}")
except ValueError:
    #Hemos aplicado un try:
    #El cual nos permite en caso exita un error nos devuelva este mensaje: En este caso si se ingresa un valor distinto a un valor numerico
    #el error saltara y nos mostrar el mensaje
    print("No se ingreso un valor numerico. Por favor volver a intentar.")


    