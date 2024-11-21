#Empezemos :


#Creamos la funcion que nos permitira concatenar cada mensaje ingresado.
#2
def mensaje_ingresado(mensaje):        
    #acá es donde recorre la lista para sacar cada texto ingresado y concatenar en una sola linea todo.
    mensaje_final =  " ".join( f"{texto.title()}." for texto in mensaje)        
    #se devuelve el mensaje
    return mensaje_final


#Creamos una lista
lista_texto = []

#Este bucle While siempre se ejecutará hasta que ingresemos la palabra "fin"

#1
while True:  
    #ingresamos el mensaje que deseamos.
    texto_ingresado = input("Ingresa algo: ")    
    
    #Se valida si el texto ingresado es fin.
    if texto_ingresado == 'fin':        
        #aquí es donde ingresará a la funcion para poder armar todo el texto contatenado.
        imprimir_mensaje = mensaje_ingresado(lista_texto)
        #despues de armar el texto contatenado lo imprime
        print(imprimir_mensaje)
        #acá es donde rompe el bucle while y se termina de ejecutar el programa
#3  
        break
    else:
        #Mientras la condicion no se cumpla se irá almacenando cada texto que se ingrese en la lista
        lista_texto.append(texto_ingresado)
        


"""
leyenda:
1. Acá es donde parte el programa, para que sea ciclico y vaya pidiendo los mensajes que iremos ingresando
   hasta que se tope con la palabra fin y deje de ejecutarse.

2. la funcion se ejecutará cuando hayamos ingresado la palabra fin, para cerrar el programa y mostrar en 
   la consola el resultado final.

3. rompre el ciclo y es el fin del programa



*** En el archivo 02_Segunda_forma.py : se hará el mismo proceso pero de otra forma.
"""        