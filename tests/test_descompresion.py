# test_descompresion.py
"""
Conjunto de tests para verificar que descomprimir_archivos_unix maneja correctamente una gama de posibilidades de archivos comprimidos, en este caso zip, tar.gz o rar.
Puesto que de base se requiere una maquina con sistema operativo Unix, se diseñan
los test para que se ejecuten en una maquina con esta arquitectura
"""
import unittest
from unittest.mock import patch, MagicMock
import os
import sys
import subprocess

# Añadimos el directorio padre de 'test' a sys.path para poder importar 'doc_reader'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import descompresion

class TestDescompresion(unittest.TestCase):
    @patch('zipfile.ZipFile')
    def test_descomprimir_zip(self, mock_zipfile):
        """
        Test para verificar que descomprimir_archivos_unix maneja correctamente los archivos zip.
        Utiliza un mock para simular la apertura y extracción de un archivo zip.
        Asegura que se llamen las funciones correctas con los argumentos esperados.
        """
        ruta = 'test_files/TMDB.zip'
        descompresion.descomprimir_archivos_unix(ruta)
        mock_zipfile.assert_called_once_with(ruta, 'r')
        mock_zipfile.return_value.extractall.assert_called_once_with(os.path.dirname(ruta))
    
    @patch('tarfile.open')
    def test_descomprimir_tar_gz(self, mock_tarfile):
        """
        Test para verificar que descomprimir_archivos_unix maneja correctamente los archivos tar.gz.
        Utiliza un mock para simular la apertura y extracción de un archivo tar.gz.
        Asegura que se llamen las funciones correctas con los argumentos esperados.
        """
        ruta = 'test_files/consultasPR3.gz'
        descompresion.descomprimir_archivos_unix(ruta)
        mock_tarfile.assert_called_once_with(ruta, 'r:gz')
        mock_tarfile.return_value.extractall.assert_called_once_with(os.path.dirname(ruta))
    
    @patch('subprocess.run')
    def test_descomprimir_rar(self, mock_subprocess):
        """
        Test para verificar que descomprimir_archivos_unix maneja correctamente los archivos run.
        Utiliza 'subprocess.run' como mock para simular la ejecución de 'unrar'.
        """
        ruta = 'test_files/consultasPR3.rar'
        descompresion.descomprimir_archivos_unix(ruta)
        mock_subprocess.assert_called_once_with(['unrar', 'e', ruta, os.path.dirname(ruta)], check=True)
    
    def test_descomprimir_invalid_extension(self):
        """
        Test para verificar que la función descomprimir_archivos_unix lanza una excepción ValueError cuando se le pasa un archivo con una extensión no válida o no soportada.
        En este test se simula simula un escenario donde se intenta descomprimir un archivo con una extensión '.txt',que no es una de las extensiones soportadas por la función (zip, tar.gz, rar).
        Se espera que la función reaccione a esta situación lanzando una excepción `ValueError`.
        """
        ruta = 'test_files/dummy.txt'
        with self.assertRaises(ValueError):
            descompresion.descomprimir_archivos_unix(ruta)
    
    @patch('subprocess.run')
    def test_descomprimir_subprocess_error(self, mock_subprocess):
        """
        Test para verificar que la función descomprimir_archivos_unix maneja correctamente los errores del proceso de subprocess cuando se intenta descomprimir un archivo .rar.
        Simula un escenario donde el proceso de subprocess falla al intentar descomprimir un archivo .rar, lo que se espera que resulte en una excepción `subprocess.CalledProcessError`.
        Se utiliza un mock de subprocess.run con un side_effect configurado para simular este error.
        Verifica que la función descomprimir_archivos_unix efectivamente lanza la excepción `subprocess.CalledProcessError` cuando se encuentra con este error.
        """
        ruta = 'test_files/consultasPR3.rar'
        mock_subprocess.side_effect = subprocess.CalledProcessError(1, 'unrar')
        with self.assertRaises(subprocess.CalledProcessError):
            descompresion.descomprimir_archivos_unix(ruta)
    
    @patch('subprocess.run')
    def test_descomprimir_general_error(self, mock_subprocess):
        """
        Test para verificar que la función descomprimir_archivos_unix maneja correctamente errores generales no específicos durante el proceso de descompresión de archivos.
        Se simula un escenario donde ocurre un error general (no específico a subprocess.CalledProcessError) durante el intento de descompresión de un archivo .rar. Se utiliza un mock de subprocess.run con un side_effect configurado para simular un error general. El test verifica que la función
        descomprimir_archivos_unix efectivamente lanza una excepción general cuando se encuentra con este tipo de error.
        """
        ruta = 'test_files/consultasPR3.rar'
        mock_subprocess.side_effect = Exception('General error')
        with self.assertRaises(Exception):
            descompresion.descomprimir_archivos_unix(ruta)

if __name__ == '__main__':
    unittest.main()