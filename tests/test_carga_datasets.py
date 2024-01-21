#  test_carga_datasets.py
"""
Este módulo contiene pruebas unitarias para el módulo carga_datasets.

Las pruebas se centran en verificar la correcta funcionalidad de la función
integrar_csv_en_dataframe, asegurando que lee y combina correctamente los archivos CSV.

Clases:
    TestCargaDatasets: Pruebas para la función integrar_csv_en_dataframe.
"""
import unittest
from unittest.mock import patch, call
import pandas as pd
import sys
import os

# Añadimos el directorio padre de 'test' a sys.path para poder importar 'carga_datasets'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from carga_datasets import integrar_csv_en_dataframe

class TestCargaDatasets(unittest.TestCase):
    """
    Conjunto de pruebas para la función integrar_csv_en_dataframe del módulo carga_datasets.

    Esta clase contiene varios métodos de prueba para validar la correcta ejecución y
    resultados de la función integrar_csv_en_dataframe.

    Métodos:
        test_integrar_csv_en_dataframe: Prueba la función integrar_csv_en_dataframe.
    """
    @patch('src.rutas_csv.leer_rutas_csv')
    @patch('pandas.read_csv')
    def test_integrar_csv_en_dataframe(self, mock_read_csv, mock_leer_rutas_csv):
        """
        Prueba la función integrar_csv_en_dataframe para asegurar que lee y combina
        correctamente los archivos CSV.

        Esta prueba utiliza mocks para simular la lectura de archivos CSV y la obtención de rutas de archivos. Verifica que los DataFrames se combinen correctamente y que el tiempo de procesamiento sea un valor flotante.

        Args:
            mock_read_csv: Mock para la función pandas.read_csv.
            mock_leer_rutas_csv: Mock para la función leer_rutas_csv del módulo src.rutas_csv.
        """
        # Simulamos la lista de rutas de archivos CSV
        mock_leer_rutas_csv.return_value = ['ruta1.csv', 'ruta2.csv']

        # Simulamos los DataFrames que serían leídos de los archivos CSV
        df1 = pd.DataFrame({'id': [1, 2], 'data1': ['a', 'b']})
        df2 = pd.DataFrame({'id': [1, 2], 'data2': ['c', 'd']})
        mock_read_csv.side_effect = [df1, df2]

        # Llamamos a la función bajo prueba
        dataframe_combinado, tiempo_procesamiento = integrar_csv_en_dataframe()

        # Aseguramos que se hayan leído los archivos CSV
        mock_read_csv.assert_has_calls([call('ruta1.csv'), call('ruta2.csv')])

        # Nos cercioramos que el DataFrame combinado tenga las columnas correctas y los datos combinados
        pd.testing.assert_frame_equal(dataframe_combinado, pd.DataFrame({'id': [1, 2], 'data1': ['a', 'b'], 'data2': ['c', 'd']}))

        # confirmamos que el tiempo de procesamiento sea un número flotante
        self.assertIsInstance(tiempo_procesamiento, float)

if __name__ == '__main__':
    unittest.main()
