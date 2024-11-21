
"""
Usando el with podemos acceder al archivo, y podemos leer o escribir dentro de la estructura with
una vez que se salga de la estructura with el archivo se cierra automaticamente
"""
with open("Seccion_9_files/fruits.txt") as my_file:
    content = my_file.read()

print(content)

#Si volvemos a consulta, nos saldra el error de que el archivo se cerro
#my_file.read()


#lectura
with open("seccion_9_files/fruits.txt", "r") as mi_archivos:
    contenido = mi_archivos.read()

print(contenido)


#escritura
with open("seccion_9_files/fruits.txt", "w") as mi_documento:
    mi_documento.write("pear\napple\norange\nmandarin\nwatermelon\npomegranate")



#escritura  
# Tambien podemos crear un archivo como el siguiente caso usando el de escritura:
#   
with open("seccion_9_files/vegetables.txt", "w") as mi_documento:
    mi_documento.write("lettuce\nlima\npineapple")




with open("seccion_9_files/decimales.txt", "w") as mi_documento:
    mi_documento.write("21.56, 21.51\n32.3, 42.75")