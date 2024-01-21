# deteccion_so.py
"""
deteccion_so.py

Este módulo dota de capacidad para detectar el sistema operativo en el que se está ejecutando el script.
Se utiliza para determinar cómo manejar archivos comprimidos en diferentes sistemas operativos.

Funciones:
    detectar_sistema_operativo(): Devuelve el nombre del sistema operativo.
"""
import platform

# Funciones para detectar el sistema operativo
def detectar_sistema_operativo():
    """
    Detecta y devuelve el nombre del sistema operativo actual.

    La función utiliza la biblioteca 'platform' para obtener información sobre el sistema operativo.

    Returns:
        str: El nombre del sistema operativo (por ejemplo, 'Linux', 'Windows', 'Darwin').

    Ejemplo:
        >>> detectar_sistema_operativo()
        'Linux'
    """
    sistema = platform.system()
    version = platform.version()
    print(f'Sistema Operativo: {sistema}')
    print(f'Versión: {version}\n')

    return sistema
