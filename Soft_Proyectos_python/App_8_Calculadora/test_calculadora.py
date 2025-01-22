import unittest
import calculadora

class TestCalculadora(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(calculadora.suma(2, 3), "El resultado de la suma es: 5")
        self.assertEqual(calculadora.suma(32, 13), "El resultado de la suma es: 45")
        self.assertEqual(calculadora.suma(-2, 13), "El resultado de la suma es: 11")

    def test_resta(self):
        self.assertEqual(calculadora.resta(12, 3), "El resultado de la resta es: 9")
        self.assertEqual(calculadora.resta(67, 34), "El resultado de la resta es: 33")
        self.assertEqual(calculadora.resta(-12, -13), "El resultado de la resta es: -25")



    def test_multiplicar(self):
        self.assertEqual(calculadora.multiplicacion(3, 3), "El resultado de la multiplicación es: 9")
        self.assertEqual(calculadora.multiplicacion(8, 14), "El resultado de la multiplicación es: 112")
        self.assertEqual(calculadora.multiplicacion(10, -13), "El resultado de la multiplicación es: -130")


    def test_dividir(self):
        self.assertEqual(calculadora.division(3, 3), "El resultado de la división es: 1.0")
        self.assertEqual(calculadora.division(14, 2), "El resultado de la división es: 7.0")
        self.assertEqual(calculadora.division(10, 0), "No se puede dividir por 0")


if __name__ == '__main__':
    unittest.main()



 


# Explicación:
# Importamos el módulo unittest: Este módulo permite crear y ejecutar pruebas unitarias.
# Importamos el módulo calculadora: El módulo que contiene las funciones a probar.
# Clase de prueba: Creamos una clase que hereda de unittest.TestCase. Dentro de esta clase, escribimos los métodos que prueban las funciones de calculadora.py.
# Métodos de prueba (test_*): Cada función de prueba comienza con el prefijo test_. Esto es importante porque unittest busca automáticamente los métodos que empiezan 
# con test_ para ejecutarlos.

# Aserciones: Usamos métodos como self.assertEqual() para comparar el resultado de las funciones con el valor esperado. Por ejemplo:
# self.assertEqual(calculadora.suma(2, 3), "El resultado de la suma es: 5")
# Si el resultado de calculadora.suma(2, 3) no es igual al valor esperado "El resultado de la suma es: 5", la prueba fallará.

# Casos especiales:
# La división por cero es un caso especial. Comprobamos que la función devuelve el mensaje adecuado.
# Ejecución del archivo: Al final, usamos:
# if __name__ == '__main__':
#     unittest.main()
# Esto permite ejecutar las pruebas directamente desde este archivo.