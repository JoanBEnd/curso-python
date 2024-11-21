"""
En esta sección, aprendiste que:
Un programa Python puede obtener información del usuario a través de la función de entrada:
La función de entrada detiene la ejecución del programa y obtiene entrada de texto del usuario:

"""

name = input("Ingresa un nombre: ")

#La función de entrada convierte cualquier entrada en una cadena, pero puedes volver a convertirla a int o float:

experience_months = input("Ingresa tu experiencia en meses: ")
experience_years = int(experience_months) / 12

#También puedes formatear cadenas con:

name = "Marco"
años = 8.5
print("Hola {}, tu tienes {} años de experiencia".format(name, años))

#Output: Hi Sim, you have 1.5 years of experience.