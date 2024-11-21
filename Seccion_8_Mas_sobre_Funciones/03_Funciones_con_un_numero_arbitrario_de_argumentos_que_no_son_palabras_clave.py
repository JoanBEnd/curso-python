"""
El nombre del archivo puede ser muy largo pero se resume a que 
si queremos mandar un sin fin de parametros podemos usar el *args
en la función, el cual nos permite recibir numerosos parametros

el *args es al fina un tipo de dato que es una tupla.

"""

def promedio(*args):
    return sum(args) / len(args)
    

print(promedio(10, 20, 30, 40))
