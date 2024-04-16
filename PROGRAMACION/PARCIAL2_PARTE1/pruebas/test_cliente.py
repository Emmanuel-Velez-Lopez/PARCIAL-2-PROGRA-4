import unittest
import sys

sys.path.append("PARCIAL2_PARTE1") 
from modelo.cliente import Cliente

class TestCliente(unittest.TestCase):
    def test_creacion_cliente(self):
        cliente = Cliente("Juan Perez", "1234567890")
        self.assertEqual(cliente.nombre, "Juan Perez")
        self.assertEqual(cliente.cedula, "1234567890")

if __name__ == '__main__':
    unittest.main()