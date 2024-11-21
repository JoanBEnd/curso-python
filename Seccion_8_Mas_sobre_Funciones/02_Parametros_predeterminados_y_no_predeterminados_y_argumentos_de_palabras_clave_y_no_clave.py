
def resta (a, b):
    return a - b


print(resta(a=5, b=2))

print(resta(b=5, a=3))

print(resta(5, 3))


print("\n===============================================\n")

def suma(a = 4, b= 12):
    return a + b


print(suma(a=12, b= 32))

print(suma())



print("\n===============================================\n")


def multiplicar(a, b=4):
    return a * b


print(multiplicar(15, 12))


## En este caso el primer parametro tiene un valor por defecto, pero el segundo parametro no lo tiene
# acá se estaria cometiendo un error porque no se puede secundar un parametro sin valor por defecto si es que el primero ya lo tiene
# si habilitamos el codigo de abajo el mismo IDE nos lo marcara como un error y si lo ejecutamos nos mostrara el error

#def dividir(a=2, b):
#    return a * b

#print(dividir(15, 3))


