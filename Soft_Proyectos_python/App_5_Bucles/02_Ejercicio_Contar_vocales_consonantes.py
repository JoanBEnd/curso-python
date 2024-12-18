
#Ejercicio:
# Solicita al usuario una palabra y utiliza un bucle for para contar cuántas vocales y cuántas consonantes tiene la palabra.


def calcular_vocales_consonantes(palabra):
    vocales=0
    consonantes= 0
    #Pasamos todo el texto a minúscula
    for letra in palabra.lower():
        #Acá consideramos las vocales con y sin tildes.
        if letra in 'aeiouáéíóú':
            vocales += 1
        else:
            consonantes +=1

    return vocales, consonantes



str_palabra = input("Ingrese una palabra: ")

vocal, consontante = calcular_vocales_consonantes(str_palabra)

print(f"En la palabra {str_palabra} existente {vocal} vocal(es) y {consontante} consonante(s)")