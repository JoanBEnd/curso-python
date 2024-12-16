#Crea una funcion donde pasemos como parametro una lista y esta me filtre solo los
#numeros pares en una nueva lista

#Una primera forma y para ir practicando lo aprendido con los bucles y condicionales 

def filtrar_numeros_pares(list_numeros):
    new_list = []
    for i in list_numeros:
        if i % 2 == 0:
            new_list.append(i)
    
    return new_list




list_numbers = [1,2,54,6,43,13,87,52]

resultado = filtrar_numeros_pares(list_numbers)
print(f"Este es el resultado: {resultado}")



#segunda forma: Podemos aplicar el list comprehension

def filtro_de_pares(list_numeros):

        return [i  for i in list_numeros if i %2 == 0]


 #usando la misma lista deberiamos obtener el mismo resultado

resultado_pares = filtro_de_pares(list_numbers)
print(f"Este es el resultado con list comprehesion: {resultado_pares}")


 #Crea una funcion que permita calcular el factorial de un numero:

#Primera forma:

#Creamos la funcion y tendra un solo parametro
def calcular_factorial(numero):
#validamos si el valor ingresado es un numero entero
    
    if type(numero) is int:
        #Si el numero es 0 o 1 devolvemos 1
        if numero == 0 or numero == 1:
             return 1
        else:
            factorial = 1
            #En este for utilizamos un range para hacer un rango entre el 1 y el numero ingresado y el reversed es para obtener el listado en reversa
            #Si ingresamos un 10, entonces el recorrido usando reversed() sera desde el 10,9,8,7...,1
            for a in reversed(range(1,numero+1)):
                factorial = factorial * a
            return factorial
    else:
#En caso de no cumplir con la condicion se muestra un mensaje         
         return "Error, valor ingresado no es un número"
resultado_factorial = calcular_factorial(11)
print(f"El resultado del factorial es: {resultado_factorial}")



#Segunda forma:
#usando las funciones incorporadas math factorial:
#Para ello impoortamos la funcion math
import math

def mi_factorial(numero):
     if isinstance(numero,int):
        return math.factorial(numero)
     else:
        return "Error, valor ingresado no es un número"

resultado_fact = mi_factorial(33)
print(f"El resultado del factorial es: {resultado_fact}")







"""
Crea una función que determine si un número es primo.
Numeros primos: Aquellos que se dividen entre 1 y en si mismo

Acá tenemos varias condicionales

1 Validar que numero 1 no es primo (ya que solo tiene 1 divisor)
2 Validar que numero 2 y 3 son primos de manera rapida
3 Validar que todos los numero pares despues del 2 no son primos
4 Ultima condicion donde validamos el resto de números. Lo que buscamos es al numero ingresado elevarlo al cuadrado para poder hacer un recorrido
  en el rango del 3 al limite para validar
5 En el recorrido lo haremos partiendo desde el 3 en adelante pero de 2 en 2 es decir (3, 5, 7, 9, ....)
6 Validamos que el numero ingresado con el valor i del rango nos de residuo 0. Si ninguno se cumple sale del bucle y retornaria que es primo.
  En caso alguno cumpla con la condicion retornaria que no es primo
  

"""

def es_primo(numero):


#1
    if numero == 1 :
        return "no es primo"
#2
    elif numero in (2, 3):
        return "es primo"
#3
    elif numero % 2 == 0:
        return "no es primo"
#4
    else:
        limite = (numero ** 2) + 1
#5         
        for i in range(3, limite, 2):
#6            
            if numero % i == 0:                
                return "no es primo"

        return "es primo"       
        

    

number=27
resultado_primo = es_primo(number)
print(f"El numero {number}: {resultado_primo}")