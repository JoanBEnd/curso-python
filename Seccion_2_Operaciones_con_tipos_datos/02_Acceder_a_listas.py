"""
Hemos visto que usando el metodo index, podemos acceder a la posicion de una valor dentro de la lista
Pero hay otra forma de hacerlo y es sin usar el metodo index sino los []
"""
serie_numeros = [123, 452, 625, 758, 693]

"""
Si quiero acceder al numero 625 debo saber
primero la posicion que en este caso es la posición 2, tengamos en cuenta
que los indices parten desde el 0
Entonces al saber la posicion hago lo siguiente:
"""

print(serie_numeros[2])

#De esta forma es como ubicamos de manera mas rapida un valor dentro de una lista

"""
UNA VEZ ENTENDIDO ESTO, HAGAMOS UN EJERCICIO USANDO APPEND
"""

dia_Semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
Fin_Semana = ["Sábado", "Domingo"]

#Elimina un elemento de Fin_Semana y agregalo al dia_Semana
#Para ello hacemos lo siguiente:

#creo una variable y aplico el metodo pop a Fin_Semana

sat = Fin_Semana.pop(1)
dia_Semana.append(sat)

print(f"El resultado de los dias de semana es: {dia_Semana}")
print(f"El resultado de fin de semana es: {Fin_Semana}")

##Al ejecutar el ejercicio ,se está quitando el dia domingo de Fin_Semana y se está agregando a dia_Semana