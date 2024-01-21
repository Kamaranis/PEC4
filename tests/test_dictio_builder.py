# test_dictio_builder.py
""" 
Conjunto de pruebas para las funciones del módulo dictio_builder.
"""
import unittest
from unittest.mock import patch, MagicMock
import sys
import os
import pandas as pd

# Añadimos el directorio padre de 'test' a sys.path para poder importar 'dictio_builder'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import dictio_builder

class TestDictioBuilder(unittest.TestCase):
    """
    Conjunto de pruebas para las funciones del módulo dictio_builder.

    Esta clase contiene métodos de prueba para validar la correcta creación de diccionarios a partir de archivos CSV y DataFrames.

    Métodos:
        test_integrar_csv_en_diccionario: Prueba la función integrar_csv_en_diccionario.
        test_crear_diccionario_series: Prueba la función crear_diccionario_series.
    """

    @patch('dictio_builder.r_csv.leer_rutas_csv')
    @patch('builtins.open')
    def test_integrar_csv_en_diccionario(self, mock_open, mock_leer_rutas_csv):
        """
        Prueba la función integrar_csv_en_diccionario para asegurar que combina correctamente archivos CSV en un diccionario.

        Esta prueba utiliza mocks para simular la lectura de archivos CSV y la obtención de rutas de archivos.

        Args:
            mock_open: Mock para la función open.
            mock_leer_rutas_csv: Mock para la función leer_rutas_csv.
        """
        # Simulamos la obtención de rutas de archivos CSV
        mock_leer_rutas_csv.return_value = ['ruta1.csv', 'ruta2.csv']

        # Simulamos el contenido de los archivos CSV
        contenido_csv = [
            "id,name\n1,Serie A\n2,Serie B",
            "id,genre\n1,Comedy\n2,Drama"
        ]
        mock_open.side_effect = [MagicMock(read=MagicMock(return_value=contenido)) for contenido in contenido_csv]

        # Llamamos a la función bajo prueba
        diccionario_combinado, tiempo_procesamiento = dictio_builder.integrar_csv_en_diccionario()

        # Verificamos que el diccionario combinado contenga los datos esperados
        self.assertEqual(diccionario_combinado, {'1': {'id': '1', 'name': 'Serie A', 'genre': 'Comedy'}, '2': {'id': '2', 'name': 'Serie B', 'genre': 'Drama'}})

        # Verificamos que el tiempo de procesamiento sea un float
        self.assertIsInstance(tiempo_procesamiento, float)

    def test_crear_diccionario_series(self):
        """
        Prueba la función crear_diccionario_series para asegurar que crea un diccionario a partir de un DataFrame.

        Esta prueba utiliza un DataFrame de pandas simulado para verificar la correcta creación del diccionario.
        """
        # Creamos un DataFrame de pandas simulado
        df = pd.DataFrame({
            'name': ['Serie A', 'Serie B'],
            'homepage': ['http://homepageA.com', pd.NA],
            'poster_path': ['/posterA.jpg', '/posterB.jpg']
        })

        # Llamamos a la función bajo prueba
        series_dict = dictio_builder.crear_diccionario_series(df)

        # Verificamos que el diccionario contenga los datos esperados
        self.assertEqual(series_dict, {'Serie A': 'http://homepageA.com/posterA.jpg', 'Serie B': 'NOT AVAILABLE/posterB.jpg'})

if __name__ == '__main__':
    unittest.main()
