
#Crea una función para calcular el área de un cuadrado
# a = l*l   ó   l**2 
def calcular_area_cuadrado(lado):
    return lado**2



#Crea una función para calcular el área de un rectangulo
#  a = lado* ancho
def calcular_area_rectangulo(lado, ancho):
    return lado * ancho





"""
LLamemos a las funciones
"""

#Funcion 1
lado_cuadrado = 15
resultado_cuadrado = calcular_area_cuadrado(lado_cuadrado)
print(f"El resultado obtenido para el área del cuadrado es: {resultado_cuadrado}")




#Funcion 2
lado_rec = 15
ancho_rec = 20
resultado_recttangulo = calcular_area_rectangulo(lado_rec, ancho_rec)
print(f"El resultado obtenido para el área del rectangulo es: {resultado_recttangulo}")




 



#Crear una función donde pases los siguientes paramentros:
# texto 
# indice_inicio
# indice_fin
#Lo que debes hacer es al texto que pases a la funcion te devuelva una parte de ella usando los otros 2 paramentros de indices 


#Usando slicing
def slicing_texto(texto, indice_ini, indice_fin):
     
     #Usaremos los indices para poder hacer uso del slicing
     return texto[indice_ini:indice_fin]

#Declaramos nuestras variables con la información correspondiente:
texto = "Estamos comprometidos en aprender constantemente"
indice_ini = 0
indice_fin = 21

resultado_slicing = slicing_texto(texto, indice_ini, indice_fin)
print(f"Resultado del texto recortado: {resultado_slicing}")




#Crea una función que reciba una lista de números y devuelva la suma de todos ellos.

def sumar_lista(lista):
    #usando solo la funcion sum, nos permite sumar toda la lista, ahorrandonos hacer un bucle for y recorrer toda la lista
    #e ir sumando 1 x 1
    return sum(lista)


mi_lista = [5, 10, 50]
resultado_lista_sum = sumar_lista(mi_lista)
print(f"Resultado de la lista sumada: {resultado_lista_sum}")



#Crea una función que permita contar vocales en un texto

def contar_vocales(texto):    
    sumando = 0
    #recoremos el texto
    for letra in texto:
        #validamos si es un vocal para contar, usamos lower() para que toda mayuscula sea convertido en minuscula
        if letra.lower() in "aeiou":
            sumando += 1

    return sumando

mi_texto = "Encontremos cuantas vocales existen en este texto"
result_vocales = contar_vocales(mi_texto)
print(f"Resultado total vocales: {result_vocales}")
