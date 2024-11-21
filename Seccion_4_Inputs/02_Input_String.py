"""
Ahora veremos un ejercicio usando multiples inputs
y nos devolvera una mensaje
"""


def mensaje_bienvenida(nombre, apellido, correo):

    return f"Hola {nombre} {apellido}, bienvenido a Social Club, sus credenciales las podrá ver en el siguiente correo: {correo}"




nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese sus apellidos: ")
correo = input("Ingrese el correo:")

mensaje = mensaje_bienvenida(nombre, apellido, correo)
print(mensaje)

"""
En el siguiente programa estamos solicitando al usuario que ingrese
3 datos personales que corresponde al nombre, apellidos y correo del usuario
con eso se le muestra un mensaje de bienvenida.
Como vieron acá no hubo necesidad de hacer una conversión de datos, porque es un string lo que estamos ingresando
en cada input.
"""