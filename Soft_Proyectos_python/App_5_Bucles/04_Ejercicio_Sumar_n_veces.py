#Sumar hasta que el usuario quiera
#Solicita al usuario que ingrese números y súmalos. Detén el programa cuando el usuario ingrese "salir".
#Ejemplo:
#Ingresa una cantidad de numeros: 1,2,3,4
#La suma total es: 10
#Ingrese una cantidad de numeros: salir
#El resultado final dela suma es : 10

total = 0

def sumar_tupla(numeros):    
    #declaramos a total como global para no tener inconvenientes en reconocer la varialbe y poder realizar la suma interna de la funcion
    global total    
    #convertimos la data ingresada a una lista
    numeros_int = [ int(dato) for dato in numeros.split(",")] 
    total += sum(numeros_int)
    return total

while True:
    numeros = input("Ingresa una cantidad de numeros: ")
    if numeros == "salir":
        print(f"El resultado final dela suma es : {total}")
        break
    else:
        resultado = sumar_tupla(numeros)
        print(f"La suma total es: {resultado}")
