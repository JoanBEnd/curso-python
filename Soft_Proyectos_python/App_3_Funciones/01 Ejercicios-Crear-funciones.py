
#Crea una función para calcular el área de un cuadrado
# a = l*l   ó   l**2 
def calcular_area_cuadrado(lado):
    return lado**2



#Crea una funcion para calcular el área de un rectangulo
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