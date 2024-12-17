"""
Ingresa una palabra y determina si es un palíndromo (se lee igual de izquierda a derecha y de derecha a izquierda).
Ejemplo
ana
anilina
"""

def palindromo(palabra):
    new_word = ""
    #Recorremos la palabra ingresada al revés desde el final al inicio y vamos concatenando
    #para formar la nueva palabra
    for i in reversed(palabra):
        new_word += i
    #luego validamos si se cumple o no 
    if palabra == new_word:
        return f"{palabra} y {new_word} son iguales, así que es un palíndromo"
    else:
        return f"{palabra} y {new_word} no son iguales, así que no es un palíndromo"



 
mi_palindromo = (input("Ingrese una palabra: "))
resultado_palindromo = palindromo(mi_palindromo)
print(resultado_palindromo)
 

