# Crear un archivo y escribir texto
#Crea un programa que pida al usuario un texto y lo guarde en un archivo llamado archivo.txt.
#Input:
#   Ingrese un texto: Hola, este es un archivo de prueba.
#Output (contenido del archivo):
#   Hola, este es un archivo de prueba.


def generar_archivo(texto):

    with open("Soft_Proyectos_python/App_7_Files/data/libro_educativo.txt", "w") as file:
       file.write(texto)


ing_texto = input("Ingrese un texto: ")

generar_archivo(ing_texto)