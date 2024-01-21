""" 
Módulo de pruebas unitarias para la función detectar_sistema_operativo del módulo deteccion_so.
"""
import unittest
from unittest.mock import patch
import sys
import os

# Añadimos el directorio padre de 'test' a sys.path para poder importar 'deteccion_so'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from deteccion_so import detectar_sistema_operativo

class TestDeteccionSO(unittest.TestCase):
    """
    Conjunto de pruebas para la función detectar_sistema_operativo del módulo deteccion_so.

    Contiene métodos de prueba para la validacion de la correcta detección del sistema operativo.

    Métodos:
        test_detectar_sistema_operativo: Prueba la función detectar_sistema_operativo.
    """

    @patch('platform.system')
    def test_detectar_sistema_operativo(self, mock_system):
        """
        Prueba la función detectar_sistema_operativo para asegurar que detecta correctamente el sistema operativo.

        Esta prueba utiliza un mock para simular la respuesta de la función platform.system.

        Args:
            mock_system: Mock para la función platform.system.
        """
        # Simulamos diferentes sistemas operativos
        for so in ['Linux', 'Windows', 'Darwin']:
            mock_system.return_value = so
            resultado = detectar_sistema_operativo()
            self.assertEqual(resultado, so)

if __name__ == '__main__':
    unittest.main()
