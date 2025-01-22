 

def suma(number_uno, number_dos):
    return f"El resultado de la suma es: {number_uno + number_dos}"

def resta(number_uno, number_dos):    
    if (number_uno <0 and number_dos < 0):
        return f"El resultado de la resta es: { number_uno + number_dos}"
    else:
        return f"El resultado de la resta es: { number_uno - number_dos}"

def multiplicacion(number_uno, number_dos):    
    return f"El resultado de la multiplicación es: { number_uno * number_dos}"

def division(number_uno, number_dos):    

    result =   "No se puede dividir por 0" if number_dos == 0 else  round(number_uno / number_dos , 2)
    if type(result) == str:
        return result
    else:
        return f"El resultado de la división es: { result}"
    


# Este archivo contiene las funciones básicas de las operaciones matemáticas que usará el proyecto:
#     suma: Realiza la suma de dos números y devuelve el resultado en un formato de cadena.
#     resta: Calcula la diferencia entre dos números y la devuelve como una cadena, maneja una condicion en caso ser numeros negativos los sume.
#     multiplicacion: Multiplica dos números y devuelve el resultado como cadena.
#     division: Divide dos números, maneja la excepción de división por cero devolviendo un mensaje especial si ocurre, y retorna el resultado como cadena.