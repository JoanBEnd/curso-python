

#Creamos la funcion que nos permitira darle la estructura al mensaje.
#2
def mensaje_enviado(mensaje):
    
    return f"{mensaje.capitalize()}."


#Creamos una lista

lista_general = []


#Este bucle While siempre se ejecutará hasta que ingresemos la palabra "fin"

while True:
    
    #ingresamos el mensaje que deseamos.
    user_input = input("Ingrese un texto: ")

    #Se valida si el texto ingresado es fin.
    if user_input == "fin":
        #acá es donde rompe el bucle while y se termina de ejecutar el programa
        break
    else:
        #aquí es donde ingresará a la funcion y alli mmismo despues de ejecutarse la funcion
        #se agrega el valor obtenido a la lista.
        lista_general.append(mensaje_enviado(user_input))

#aqui lo que está haciendo es unir todos los textos que se encuentran en la lista, en una sola linea, para
#mostrar el mensaje final en pantalla.
print(" ".join(lista_general))




"""
Como pueden observar, en las dos formas de resolver el ejercicio planteado a pesar de que se pueden parecer
en varias partes del codigo hay detalles que las hacen diferentes por lo que no siempre vamos a tener una 
unica solución a un problema.
Espero esto les sirva como punto de partida para que se puedan animar a probar distintas formas de como afrontar
un problema que se les presente en su camino de desarrollador.
"""


