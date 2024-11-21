
"""
El uso de `elif` nos permite agregar condiciones adicionales dentro de una estructura `if`. 
Si la primera condición no se cumple, `elif` verifica una nueva condición. Puedes tener 
varios bloques `elif` para evaluar diferentes posibilidades. Si ninguna de las condiciones 
anteriores se cumple, se ejecuta el bloque `else`, si está presente.


    if condicion:
            # ejecutar codigo
    elif condicion:
            # ejecutar codigo
    elif condicion:
            # ejecutar codigo            
    else:
            # ejecutar codigo
           
"""

y = 15
z = 2


if y > 20 and z > 10:
    print(f"Es correcto {y} es mayor que 20 y {z} es mayor que 10")
elif y < 20 and z < 10:
    print(f"Es correcto {y} es menor que 20 y {z} es menor que 10")
else:
    print("No cumple la condición")


def foo(x, array):
    if x in array:
        return True
    else:
        return False
 
print(foo(1, [1, 2, 3]))
print(foo(1, [2, 3]))
print(foo(1, ['1', 2, 3]))


def cal_temperatura(temp):
    if temp > 25:
        return "Hot"
    elif temp >= 15 and temp <= 25:
        return "Warm"
    else:
        return "Cold"



print(cal_temperatura(10))
print(cal_temperatura(15))
print(cal_temperatura(16))
print(cal_temperatura(25))
print(cal_temperatura(26))