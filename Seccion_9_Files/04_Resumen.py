"""
Ya podemos leer un archivo desde python:
"""

with open("file.txt") as file:
    content = file.read()

#Podemos crear un archivo con Python
# y escribir un texto en el archivo:

with open("file.txt", "w") as file:
    content = file.write("Sample text")

#Podemos agregar texto a un archivo existente
# y sobreescribir :

with open("file.txt", "a") as file:
    content = file.write("More sample text")

#Y podemos hacer ambas cosas
# leer y escribir:

with open("file.txt", "a+") as file:
    content = file.write("Even more sample text")
    file.seek(0)
    content = file.read()