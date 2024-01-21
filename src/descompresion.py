# descompresion.py
"""
descompresion.py

Este módulo proporciona funcionalidades para descomprimir archivos en 
varios formatos (zip, tar.gz, rar) en sistemas Unix y Windows. 
Utiliza las bibliotecas integradas de Python y herramientas de 
línea de comandos para manejar diferentes formatos de archivos 
comprimidos.

    Dependencias:
    - zipfile: Para manejar archivos zip.
    - tarfile: Para manejar archivos tar.gz.
    - subprocess: Para ejecutar comandos de descompresión en la línea de comandos.
    - os: Para manipulación de rutas de archivos y directorios.

    Este módulo contiene las siguientes funciones:
    - descomprimir_archivos_unix(ruta): Descomprime archivos en sistemas Unix.
    - descomprimir_archivos_nt(ruta): Descomprime archivos en sistemas Windows.

    Ejemplos de uso:
    descomprimir_archivos_unix('path/to/archivo.zip')
    descomprimir_archivos_nt('path/to/archivo.rar')

    Otrosidigo:
Ha sido probado en sistemas Linux y Windows.
El soporte para macOS (Darwin) se ha implementado siguiendo las mismas convenciones
que para sistemas Unix-like, pero no ha sido probado exhaustivamente.
"""
import zipfile
import tarfile
import os
import subprocess

# Funciones para descomprimir archivos en sistemas Unix y Windows
def descomprimir_archivos_unix(ruta: str):
    """
        Descomprime archivos en formatos zip, tar.gz o rar en sistemas Unix.

        Args:
            ruta (str): Ruta completa al archivo comprimido.

        Returns:
            None: La función no devuelve ningún valor.

        Raises:
            ValueError: Si el archivo no tiene una extensión .zip, .tar.gz, o .rar.
            subprocess.CalledProcessError: Si hay un error al ejecutar el comando de descompresión.
            Exception: Para otros errores generales.
        """
    try:
        if ruta.endswith('.zip'):
            with zipfile.ZipFile(ruta, 'r') as archivo_zip:
                archivo_zip.extractall(os.path.dirname(ruta))
                print(f"Archivo {ruta} descomprimido con éxito.")
        elif ruta.endswith('.tar.gz'):
            with tarfile.open(ruta, 'r:gz') as archivo_tar:
                archivo_tar.extractall(os.path.dirname(ruta))
                print(f"Archivo {ruta} descomprimido con éxito.")
        elif ruta.endswith('.rar'):
            comando = ['unrar', 'e', ruta, os.path.dirname(ruta)]
            subprocess.run(comando, check=True)
            print(f"Archivo {ruta} descomprimido con éxito.")
        else:
            raise ValueError("El archivo no es .zip ni .tar.gz ni .rar")
    except subprocess.CalledProcessError as e:
        print(f'Error al descomprimir el archivo: {e}\n')
        print(f"Código de retorno: {e.returncode}")
    except Exception as e:
        print(f"Error al descomprimir el archivo: {e}")


def descomprimir_archivos_nt(ruta: str):
    """
    Descomprime archivos en formatos zip, tar.gz o rar en sistemas Unix.

    Args:
        ruta (str): Ruta completa al archivo comprimido.

    Returns:
        None: La función no devuelve ningún valor.

    Raises:
        ValueError: Si el archivo no tiene una extensión .zip, .tar.gz, o .rar.
        subprocess.CalledProcessError: Si hay un error al ejecutar el comando de descompresión.
        Exception: Para otros errores generales.
    """
    try:
        if ruta.endswith('.zip'):
            with zipfile.ZipFile(ruta, 'r') as archivo_zip:
                archivo_zip.extractall(os.path.dirname(ruta))
                print(f"Archivo {ruta} descomprimido con éxito.")
        elif ruta.endswith('.tar.gz'):
            with tarfile.open(ruta, 'r:gz') as archivo_tar:
                archivo_tar.extractall(os.path.dirname(ruta))
                print(f"Archivo {ruta} descomprimido con éxito.")
        elif ruta.endswith('.rar'):
            comando = ["C:\\Program Files\\WinRAR\\WinRAR.exe", "x", ruta]
            subprocess.run(comando, check=True)
            print(f"Archivo {ruta} descomprimido con éxito.")
        else:
            raise ValueError("El archivo no es .zip ni .tar.gz ni .rar")
    except subprocess.CalledProcessError as e:
        print(f'Error al descomprimir el archivo: {e}\n')
        print(f"Código de retorno: {e.returncode}")
    except Exception as e:
        print(f"Error al descomprimir el archivo: {e}")
