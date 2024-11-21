"""

Implemente una función que obtenga el nombre de una persona como parámetro y salude a la persona con Hola persona. 
Por ejemplo, si llamé a su función usando foo("Marry") la función debería devolver Hi Marry.
"""




def saludar(nombre):
    return f"Hola {nombre}"

nombre = input("Ingrese su nombre: ")

saludo = saludar(nombre)
print(saludo)


"""

Implemente una función que obtenga el nombre de una persona (por ejemplo, John) como parámetro y devuelva un saludo 
(por ejemplo, Hola John). Tenga en cuenta que la primera letra del nombre de la persona siempre debe estar en mayúscula.
"""


def saludando(nombre):
    return f"Hola {nombre.title()}"

nombre = input("Ingrese su nombre:")

print(saludando(nombre))

