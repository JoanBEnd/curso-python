"""
Generar una tabla de multiplicar
Pide al usuario ingresar un número y genera su tabla de multiplicar del 1 al 10.

Entrada ejemplo:
Ingrese un número para generar su tabla de multiplicar: 5
"""

#Acotación la siguiente expresión \n nos permite dar un salto de linea en el texto.

def generar_tabla_multiplicar(numero):
    mensaje= f"Tabla de multiplicar del {numero}: \n\n"
#En esta primera forma usaremos un bucle for como tal la conocemos

    for i in range(1, 13):
#Vamos concatenando cada recorrido para almacenar cada nueva multiplicación         
        mensaje +=   f"{numero} x {i} = {numero*i} \n" 
    return mensaje



print(generar_tabla_multiplicar(5))


#Como podemos optimizar esto:
#Usando lista de comprension o list Comprehensions


def generar_tablas_mult(numero):
#Como hemos visto en la teoria, una forma mas eficiente es usar una lista de compresión    
    lista_mult = [f"{numero} x {i} = {numero * i}" for i in range(1, 13)]
#Y despues esa lista la unimos con la funcion join()     y a la par concatenamos con el mensaje que queremos mostrar
    mensaje = f"Tabla de multiplicar {numero}:\n\n" + "\n".join(lista_mult)
    return mensaje

try:
    mi_numero = int(input("Ingrese el número que quiere generar su tabla de multiplicar: "))
    
    resultado_tabla_multiplicar = generar_tablas_mult(mi_numero)
    print(resultado_tabla_multiplicar)
except ValueError:
    print("No se ingreso un valor numerico. Por favor volver a intentar.")



#En este caso hemos podido resolver el mismo problema usando 2 distintas formas
#Al usar la list comprehension nos ayuda a  ue el programa sea más rapido y eficiente en términos de memoria.