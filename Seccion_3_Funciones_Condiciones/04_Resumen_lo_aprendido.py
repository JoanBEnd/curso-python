"""
En esta sección hemos aprendido:
"""



#Definir Funciones

def cube_volume(a):
    return a * a * a


#Escribir if-else condicionales:

message = "hello there"
 
if "hello" in message:
    print("hi")
else:
    print("I don't understand")


#Escribir if-elif-else condicionales:

message = "hello there"
 
if "hello" in message:
    print("hi")
elif "hi" in message:
    print("hi")
elif "hey" in message:
    print("hi")
else:
    print("I don't understand")


#El uso del operador "and" para revisar si ambas condiciones son True al mismo tiempo:

x = 1
y = 1
 
if x == 1 and y==1:
    print("Yes")
else:
    print("No")


#El uso del operador "or" para revisar si al menos una de las 2 condiciones es True:

x = 1
y = 2
 
if x == 1 or y==2:
    print("Yes")
else:
    print("No")


#Validar el tipo de dato en uno de los ejercicios

#if type("abc") == str
#if type([1, 2, 3]) == lst