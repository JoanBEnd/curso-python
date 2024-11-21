"""
Ejercicio 01:

Defina una función que obtenga un carácter de cadena única
 y una ruta de archivo como parámetros y devuelva el número
de apariciones de ese carácter en el archivo.
"""

def conteo_caracter(letra, ruta):
    conteo = 0
        
    with open(ruta, "r") as mi_archivo:
        mi_documento = mi_archivo.read()
        

    for caracter in mi_documento:
        if caracter == letra:
            conteo += 1
    
    return conteo
        
ruta = "Seccion_9_files/fruits.txt"        
resultado = (conteo_caracter("a", ruta))

print(f"El resultado usando la primera forma: {resultado}")
    
"""
    Segunda forma
"""

def contando_string(letra, ruta):
    with open(ruta, "r") as mi_archivo:
        mi_documento = mi_archivo.read()
    
    return mi_documento.count(letra)
    



rutina = "Seccion_9_files/fruits.txt"        
resultado = (contando_string("e", rutina))

print(f"El resultado usando la segunda forma: {resultado}")






"""
Ejercicio 02:

el contenido existente en el archivo decimales.txt tiene la siguiente
estructura:

21.56, 21.51

32.3, 42.75

usando Python modifica el contendido de decimales.txt ,
para que tenga el siguiente aspecto:

21.56, 21.51

32.3, 42.75

21.56, 21.51

32.3, 42.75

21.56, 21.51

32.3, 42.75

Asi que encuentra la forma de poder ingresar y repetir 2 veces mas 
los datos iniciales y si puedes hacerlo para que la insercion 
sea n veces posibles:

"""

 
def llenar_data_txt(maximo):
    #Obtenemos la informacion del archivo decimales
    with open("seccion_9_files/decimales.txt") as mi_datos:
        contenido_datos = mi_datos.read()
    i=1
    #De esta forma hacemos el insert o agregamos la cantidad de veces
    #que le mandemos como parametro a la funcion
    while i <= maximo:
        with open("seccion_9_files/decimales.txt", "a+") as mi_ingresos:
            mi_ingresos.write(f"\n{contenido_datos}")
            i += 1
        

llenar_data_txt(maximo=2) 