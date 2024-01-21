# rutas_csv.py
"""
    Ejemplo de uso
    archivos_csv = leer_rutas_csv()
    print(archivos_csv)
"""
import os

def leer_rutas_csv():
    """
    Crea una lista de ficheros .csv contenidos en la carpeta 'data'.

    Returns:
        list: Lista de rutas completas a los archivos .csv en la carpeta 'data/'.
    """
    carpeta = 'data'  # Ruta fija a la carpeta 'data'
    lista_csv = []

    if os.path.isdir(carpeta):
        for archivo in os.listdir(carpeta):
            if archivo.endswith('.csv'):
                ruta_archivo = os.path.join(carpeta, archivo)
                lista_csv.append(ruta_archivo)
    else:
        print("La carpeta 'data' no existe o no es un directorio.")

    return lista_csv
