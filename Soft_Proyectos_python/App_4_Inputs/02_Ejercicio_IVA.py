"""
Calculadora de IVA
    Crea una función que calcule el IVA de un producto dado su precio y la tasa de IVA (por defecto, 18%).

Requisitos:
    La función debe llamarse calcular_iva.
    Debe recibir dos parámetros:
    precio: El precio base del producto.
    tasa: La tasa de IVA (opcional, por defecto 18%).
    Debe devolver el precio con IVA incluido.
"""



def calcular_IVA(monto, porcentaje=18):
    
    return monto + (monto * porcentaje/100)


try:
    monto = int(input("Por favor ingresar el monto: "))
    porcentaje = input("Por favor ingresar el porcentaje. Si el porcentaje es General, dar enter: ")

    resultado_IVA = 0
    
    if len(porcentaje) == 0:
        resultado_IVA = calcular_IVA(monto)
    else:
        resultado_IVA = calcular_IVA(monto, int(porcentaje))
    
    print(f"El resultado del IVa es de : {resultado_IVA}")
except ValueError:
    #Hemos aplicado un try:
    #El cual nos permite en caso exita un error nos devuelva este mensaje: En este caso si se ingresa un valor distinto a un valor numerico
    #el error saltara y nos mostrar el mensaje
    print("No se ingreso un valor numerico. Por favor volver a intentar.")
