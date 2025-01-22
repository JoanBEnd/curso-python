import operaciones
mensaje_calculadora=(
    "==================================================\n"
    "Bienvenido a la calculadora por consola:\n"
    "1. Suma\n"
    "2. Resta\n"
    "3. Multiplicar\n"
    "4. Dividir\n"    
    "5. Salir\n"
    )

while True:
    print(mensaje_calculadora)
    ingrese_el_numero = input("Ingrese el número de la operación: ")

    if not ingrese_el_numero.isdigit():
        print("No has ingresado el valor correcto, por favor volver a intentar.")
        continue
    try:
        ingrese_el_numero =  int(ingrese_el_numero)
        if ingrese_el_numero == 5:
            break
        else:
            if operaciones.dict_operaciones.get(ingrese_el_numero):
                ejecutar_funcion_reporte = operaciones.dict_operaciones[ingrese_el_numero][0]
                while True:
                    try:
                        primer_numero = int(input("Ingrese el primer número: "))
                        break
                    except ValueError:
                        print("El valor ingresado no es un número válido, intente de nuevo.")
                while True:
                    try:
                        segundo_numero = int(input("Ingrese el segundo número: "))
                        break
                    except ValueError:                        
                        print("El valor ingresado no es un número válido, intente de nuevo.")
                
                mensaje =ejecutar_funcion_reporte(primer_numero, segundo_numero)                          
                print(mensaje)
                input_continuar = input("Desea continuar Si/No: ")
                if input_continuar.upper() == "NO" or input_continuar.upper() != "SI":
                    break            
            else:
                input_continuar = input("El valor ingresado no existe, por favor volver a intentar, desea continuar Si/No: ")    
    except ValueError as e:
        raise ValueError(f"Error al cargar los datos: {e}")
    


# Este archivo es el núcleo del programa y actúa como interfaz principal para interactuar con el usuario:
# Muestra un menú con opciones para realizar operaciones matemáticas (1: Suma, 2: Resta, etc.).
# Valida que la entrada del usuario sea un número válido.
# Verifica que la operación seleccionada esté dentro del rango de opciones permitidas (1 a 5).
# Solicita al usuario dos números para realizar la operación seleccionada.
# Ejecuta la operación correspondiente llamando a la función adecuada desde el diccionario dict_operaciones de operaciones.py.
# Incluye un flujo para repetir la operación o salir del programa según la decisión del usuario.
# Maneja errores de entrada (como valores no numéricos) con mensajes claros y amigables para el usuario.
# Propósito:

# Gestionar toda la interacción con el usuario, incluyendo la entrada de datos, las validaciones y la ejecución de las funciones de las operaciones matemáticas.
