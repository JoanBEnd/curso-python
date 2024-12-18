"""
Ingresa una palabra y determina si es un palíndromo (se lee igual de izquierda a derecha y de derecha a izquierda).
Ejemplo
ana
anilina
"""
#Usando bucle
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
 


#Usando slicing

def validar_palindromo(palabra):

    if palabra == palabra[::-1]:
        return "Si es palindromo"
    else:
        return "No es palindromo"

#Que es lo que llama la atencion en este ejemplo:
#En que el slicing se conforma de lo siguiente:
# secuencia[inicio:fin:paso]
#inicio: indica el índice desde donde se empieza a tomar elementos (incluido).
#fin: indica el índice donde se detiene (excluido).
#paso: indica cómo moverse a través de la secuencia. Un valor negativo invierte el recorrido.
#      En caso no se especifique el paso, la lectura de la secuencia se hara de manera normal, de izquierda a derecha


mi_palindromo = (input("Ingrese una palabra: "))
resultado_palindromo = validar_palindromo(mi_palindromo)
print(resultado_palindromo)