"""
Las tuplas es una estructura de datos similares a las listas solo que en vez de estar delimitadas por [] se usan () y 
A diferencia de las listas, las tuplas son inmutables, lo que significa que, una vez creadas, no pueden
ser modificadas (no se pueden agregar, eliminar o cambiar elementos). Esto hace que las tuplas sean útiles 
para almacenar datos que no deben alterarse a lo largo del programa.

"""

mi_tupla = (12, 43, 21)

""" 
Si se quiere agregar o eliminar elementos de las tuplas usando las siguientes atributos
se obtendra error:
"""
mi_tupla.append(22) # >>>>>  AttributeError: 'tuple' object has no attribute 'append'
mi_tupla.remove(12) # >>>>> AttributeError: 'tuple' object has no attribute 'remove'

#Por lo que si necesitas una estructura de datos la cual no se modifique durante la ejecución de tu programa es recomendable esta estructura.