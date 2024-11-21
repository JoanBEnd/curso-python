"""
Obtener informacion de un archivo

usamos la funcion open() con ella buscamos la ubicacion del archivo
para almacenar la informacion en una variable
luego a la variable le aplicamos la funcion read() para leer el contenido
del documento.

Al final podemos imprimir la informacion
"""

my_file = open("Seccion_9_Files/fruits.txt")
mi_lectura = my_file.read()
#De esta forma cerramos el acceso a leer el libro.
my_file.close()

print(mi_lectura)

#Si queremos leer nuevamente, nos saldrá un error ya que el archivo o el acceso al archivo se cerró
my_file.read()






