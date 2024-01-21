# carga_datasets.py
"""
carga_datasets.py

Este módulo proporciona funcionalidades para cargar y combinar múltiples
conjuntos de datos CSV.
Utiliza pandas para leer y fusionar archivos CSV basándose en una columna común 'id'.

Funciones:
    integrar_csv_en_dataframe(): Lee y combina archivos CSV en un único DataFrame.
"""
import pandas as pd
import time
import src.rutas_csv


def integrar_csv_en_dataframe():
    """
       Lee varios archivos CSV de la carpeta 'data' y los combina en un único DataFrame.

       Esta función busca archivos CSV en la carpeta 'data', los lee y los combina en un
       único DataFrame utilizando la columna 'id' como clave para la combinación.
       Se utiliza un merge interno para asegurar
       que solo se incluyan en el DataFrame final aquellos registros que tienen un 'id'

    Returns:
        DataFrame: Un DataFrame que combina todos los archivos CSV encontrados en la carpeta 'data'.
        float: El tiempo total en segundos que tardó el proceso de carga y combinación.

    Ejemplo:
        dataframe_combinado, tiempo_procesamiento = integrar_csv_en_dataframe()
        print(dataframe_combinado.head())
        print(f"Tiempo de procesamiento: {tiempo_procesamiento} segundos redondeado")
       """
    # Inicializamos el tiempo de procesamiento
    inicio = time.time()

    # Obtenemos la lista de rutas de archivos CSV
    lista_rutas_csv = src.rutas_csv.leer_rutas_csv()

    # Inicializamos un DataFrame vacío para el resultado final
    dataframe_combinado = pd.DataFrame()

    # Iteramos sobre cada archivo CSV
    for ruta in lista_rutas_csv:
        df = pd.read_csv(ruta)
        if dataframe_combinado.empty:
            dataframe_combinado = df
        else:
            # Combinamos el DataFrame actual con el DataFrame combinado existente
            dataframe_combinado = pd.merge(dataframe_combinado, df, on='id', how='inner')

    # Calculamos el tiempo de procesamiento
    fin = time.time()
    tiempo_procesamiento = fin - inicio

    return dataframe_combinado, round(tiempo_procesamiento, 2)
