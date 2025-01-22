import calculadora

dict_operaciones = {
    1: [calculadora.suma],
    2: [calculadora.resta],
    3: [calculadora.multiplicacion],
    4: [calculadora.division]
  }


# Contiene un diccionario llamado dict_operaciones, que mapea las opciones numéricas (1, 2, 3, 4) a las funciones correspondientes definidas en calculadora.py.

# Servir como un puente que conecta las opciones que el usuario selecciona con las funciones correspondientes de cálculo. Esto facilita la organización y
# la interacción entre el menú principal (main.py) y las operaciones matemáticas.
  