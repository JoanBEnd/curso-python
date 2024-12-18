# Usaremos funciones y dentro de ella trabajaremos con los bucles


#Ejercicio:
#Ingresa un numero y que la funcion nos permita hacer un recorrido hasta el numero ingresado
#y que vaya sumando los numeros que se recorren

def sumatoria_por_numero(numero):
    sumatoria = 0
    for number in range(1, numero+1):
        sumatoria = sumatoria + number

    return sumatoria


num_variable = int(input("Ingresa un número: "))

result_sumatoria = sumatoria_por_numero(num_variable)

print(f"El resultado es: {result_sumatoria}")