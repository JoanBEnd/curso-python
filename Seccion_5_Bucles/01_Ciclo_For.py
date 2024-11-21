"""
Los Loop o bucle nos permite realizar una determinada
tarea repetitiva en menos lineas de código

Si yo tengo lo siguiente:

"""

lista_numeros = [12, 32, 43]

"""
y deseo imprimir cada valor dentro de la lista, hasta donde
conocemos como acceder hariamos los siguiente:
"""

print(lista_numeros[0])
print(lista_numeros[1])
print(lista_numeros[2])

"""
Esto implica escribir 3 veces el codigo de imprimir en cada linea de codigo
agregar el index [1],[2], etc, para poder mostrar cada valor, que pasa si tenemos
muchos mas valores, esto va a ir crecimiento haciendose mas largo

            print(lista_numeros[0])
            print(lista_numeros[1])
            print(lista_numeros[2])
            print(lista_numeros[3])
                    ...
                    ...
                    ...
            print(lista_numeros[n])
"""
print(f"\n======================\n")
"""
Ahora para ahorrarnos lineas de codigo, podemos utilizar bucles o *loops* 
para reducir líneas de código y evitar la repetición.

Uno de ellos es el ciclo for el cual se utiliza para iterar sobre elementos en una secuencia o 
(ya sea una lista, tupla, cadena, diccionario, o rango de números). Con `for`, puedes ejecutar un bloque 
de código una vez por cada elemento en la secuencia.

 
Estructura basica:

 for i in expresion:
    #codigo

Entonces para imprimir la lista seria de la siguiente forma:    

Usando lista:
"""

for elemento in lista_numeros:
    print(elemento)


#En este caso, `elemento` es una variable temporal que toma el valor de cada elemento en la secuencia (que es la lista) conforme el bucle avanza.



"""
Usando Cadena:
"""
print(f"\n======================\n")

mi_nombre = "Santiago"

for letra in mi_nombre:
    print(letra)

"""
Lo que imprimira, será lo siguiente:
    S
    a
    n
    t
    i
    a
    g
    o
"""


"""
Usando tupla
"""

print(f"\n======================\n")
mi_tupla = (23, 43 ,23, "Saludos")

for elemento in mi_tupla:
    print(elemento)

#El recorrido es parecido al de una lista

"""
Usando un rango de numeros
"""
print(f"\n======================\n")
for numero in range(10):
    print(numero)

#Imprimira los numeros desde el 0 al 9 que es un rango que estas definiendo
print(f"\n======================\n")


"""
Usando un diccionario
"""
mi_diccionario = {
    "Asesor" : 2500,
    "Analista": 6500,
    "Programador": 6000
}

for key, valor in mi_diccionario.items():
    print( f"llaves: {key}, valor: {valor}")


mi_dict = {
    "John Smith": +37682929928,
    "Marry Simpons": +423998200919
}

for key, value in mi_dict.items():
    print(f"{key}: {value}")




phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print(str.replace(value, "+", "00"))