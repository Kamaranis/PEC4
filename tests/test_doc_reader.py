# test_doc_reader.py
"""
Este módulo contiene pruebas unitarias para la función mostrar_texto del módulo doc_reader.
Las pruebas incluyen la verificación del correcto manejo de archivos y la salida esperada cuando se lee un archivo Markdown. Se utilizan mocks para simular la apertura de archivos y la impresión de su contenido, habilitand probar la funcionalidad de mostrar_texto sin necesidad de crear archivos reales.
"""

import unittest
from unittest.mock import patch, mock_open
import sys
import os
from io import StringIO

# Añadimos el directorio padre de 'test' a sys.path para poder importar 'doc_reader'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from doc_reader import mostrar_texto

class TestMostrarTexto(unittest.TestCase):
    """
    Clase de prueba para la función mostrar_texto del módulo doc_reader.

    Esta clase implementa pruebas unitarias para asegurar que la función mostrar_texto
    lee correctamente el contenido de un archivo Markdown y lo imprime en la consola.
    Se utilizan mocks para simular la apertura de archivos y la impresión de su contenido.
    """
    @patch('builtins.open')  # Mocking de la función open
    @patch('builtins.print')  # Mocking de la función print
    def test_mostrar_texto(self, mock_print, mock_file):
        """
        Prueba que la función mostrar_texto lee y muestra correctamente el contenido de un archivo Markdown.

        Esta prueba utiliza mocks para simular la apertura de un archivo de formato texto y la impresión de su contenido.
        Se verifica que el contenido impreso en la consola sea igual al contenido simulado del archivo, asegurando así que la función mostrar_texto funciona como se espera.
        """
        # Contenido simulado del archivo
        file_content = "This is the content of the sample file."

        # Configuramos el mock de open para que devuelva un objeto StringIO con el contenido simulado
        mock_file.return_value.__enter__.return_value = StringIO(file_content)

        # Llamamos a la función mostrar_texto con una ruta de archivo ficticia
        mostrar_texto('/path/to/sample/file.md')

        # Obtenemos lo que se imprimió en la consola
        printed_output = mock_print.call_args[0][0]

        # Comprobamos que el contenido impreso sea igual al contenido simulado del archivo
        self.assertEqual(printed_output, file_content)

if __name__ == '__main__':
    unittest.main()

