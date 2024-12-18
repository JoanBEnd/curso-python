

#Adivina el número
#El programa elige un número aleatorio entre 1 y 10  y el usuario adivine el número hasta que lo haga correctamente.
#A diferencia con los otros ejercicios anteiories, en esta ocasión usaremos el bucle while, que viene bien para estos
#tipos de ejercicios.

import random
#Importamos el modulo random para poder generar un numero aleatorio   y este sea entre el 0 y 10
numero_aleatorio = int(random.random() * 10)
#print(numero_aleatorio)

#Luego creamos la funcion que hará la valicacion de ambos numeros, el que se genera de manera aleatoria
#y el que ingresa el usuario
def adivinar_un_numero(numero_ingresado):
    if numero_ingresado == numero_aleatorio:
        return True
    else:
        return False

#La funcion While se ha a estar ejecutando hasta que se logre encontrar el numero.
while True:

    numero_ingresado = int(input("Ingresar un numero aleaotorio entre el 0 y 10: "))

    if adivinar_un_numero(numero_ingresado):
        #cuando se cumpla la condicion de que ambos numero son iguales se muestra el mensaje
        #y se romple el bucle con la expresion break. Terminando el programa.
        print("Felicidades!!. Haz encontrado el número oculto.")
        break

    else:
        print("El número es incorrecto, volver a intentar.\n")
