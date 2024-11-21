
"""
Los diccionarios en Python son estructuras de datos que almacenan pares de clave y valor en un formato que facilita la organización y
 acceso a la información. La sintaxis básica es la siguiente:
{
 key: value
}

Cada elemento del diccionario consiste en una clave (key) que se asocia con un valor. Esto permite una forma estructurada y legible de manejar datos,
ya que podemos acceder rápidamente a los valores utilizando sus claves específicas. Los diccionarios son útiles para almacenar información relacionada y organizada.
Ejemplo: A continuacion tenemos un diccionario de estudiantes con sus notas:
"""

students_grades = {"Mary": 17.5,
                   "Jhon": 16.7,
                   "Melody": 17.2}


"""
Para calcular el promedio de notas del diccionario que tenemos, debemos ingresar a la parte de los valores
Para  ello usamos una funcion el cual es values() que es el obtiene los valores de cada "Key" que son los nombres de cada estudiante
"""

print(students_grades.values()) # Al ejecutar esta consulta veran los valores que son las notas de los estudiantes

#entonces:

notas_estudiantes = sum(students_grades.values()) # Las notas obtenidas de todos los estudiantes con la funcion values() al final se estan sumando
total_estudiantes = len(students_grades) #Obtenemos el total de estudiantes con la funcion len() que nos permite saber la cantidad.
promedio = notas_estudiantes / total_estudiantes #aplicando matematicas simples obtenemos el promedio

print(f"El promedio de la nota de los estudiantes es: {promedio}")


""""
Ejemplos
"""

temperatura = {
    "Celcius": [15, 22, 35],
    "Farenheit": [195, 156, 180],
    "Kelvin": [60, 48, 16]
}
print(temperatura)

#En este ejemplo podemos aprecia que se puede tener diccionarios dentro de otro diccionarios

Ciudades ={
    "Lima": {
                "Distritos": ["La victoria", "Lince", "Jesús Maria"]
             },
    "Trujillo": {
                "Distritos": ["La Esperanza", "Florencia de Mora", "Laredo"]
                }
}
print(Ciudades)