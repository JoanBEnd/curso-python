# Escribe un programa que lea un archivo txt que tenga una lista de datos , imprima su contenido en una lista.
#Archivo de entrada (archivo.txt):
#Output: lista--> ["palabra 1", "palabra 2", "palabra 3"]


def imprimir_contenido_archivo(archivos):
    with open(archivos, "r", encoding="utf-8") as my_file:
        contenido = my_file.read()                
        #splitlines() nos permite convertir cada linea de texto en una lista
        return contenido.splitlines()

mi_archivo = "Soft_Proyectos_python/App_7_Files/data/articulos.txt"

print(imprimir_contenido_archivo(mi_archivo))