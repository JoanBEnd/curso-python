# En esta parte lo que haremos es que se pueda insertar un texto mas largo con multiples lineas
# Para ello reutilizaremos el codigo anterior, pero adicional a ello
# tendremos un bucle que cada vez que demos enter nos vuelva a pedir otra nueva linea de texto
# asi hasta que ingresemos un texto unico que diga cerrar, y el programa termine y recien se cree el archivo
# con todo lo digitado.

def crear_archivo_texto_multiple(ruta, texto):
#encoding="utf-8" nos permite utilizar este estandar para garantizar el uso de caracteres especiales.

    with open(ruta, "w", encoding="utf-8") as file:
        file.write(texto)

mi_texto = ""
#1 Creamos un bucle while para que nos pida siempre ingresar un texto despues de haber ingresado un texto previo
#2 cuando ingresamos la palabra  cerrar, el programa se cierra y recien se ejecuta el código para crear el archivo y 
#3 guardar el texto que hemos ido almacenando en una variable.

#1
while True:
    ing_texto = input("Ingresar un texto: ")
#2
    if ing_texto == "cerrar":
        ruta ="Soft_Proyectos_python/App_7_Files/data/documento_multilineal.txt"
        crear_archivo_texto_multiple(ruta, mi_texto)
        break
    else:
#3        
        mi_texto = mi_texto + "\n" + ing_texto

    
    
