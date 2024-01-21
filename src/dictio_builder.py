# dictio_builder
"""
Este módulo `dictio_builder` proporciona funcionalidades para crear diccionarios a partir de datos extraídos de archivos CSV y DataFrames de pandas. 

Funciones:
    - integrar_csv_en_diccionario: Lee archivos CSV desde rutas especificadas y los combina en un único diccionario utilizando 'id' como clave.
    - crear_diccionario_series: Crea un diccionario ordenado con el nombre de la serie como clave y la dirección web completa del póster como valor.

Ejemplos de uso y aplicaciones de este módulo incluyen la creación de diccionarios para el manejo eficiente de datos en aplicaciones de análisis de datos y la preparación de datos para visualizaciones o procesamientos adicionales.
"""

import csv
import time
import src.rutas_csv as r_csv
import pandas as pd

def integrar_csv_en_diccionario():
    """
    Lee varios archivos CSV y los combina en un único diccionario utilizando 'id' como clave.

    Esta función itera sobre una lista de rutas a archivos CSV, lee cada archivo y combina sus contenidos en un diccionario.
    Cada fila de los archivos CSV se agrega al diccionario con el valor de 'id' como clave única. Si un 'id' ya existe en el diccionario,
    los datos se actualizan con la nueva información encontrada.

    Args:
        lista_rutas_csv (list): Lista de rutas a los archivos CSV.

    Returns:
        dict: Diccionario combinado que contiene los datos de todos los archivos CSV leídos.
        float: Tiempo de procesamiento en segundos, indicando cuánto tardó la operación.
    """
    lista_rutas_csv = r_csv.leer_rutas_csv() # utilizamos la funcion leer_rutas_csv del modulo rutas_csv
    inicio = time.time() # tiempo de inicio
    diccionario_combinado = {} # inicializamos el diccionario combinado

    for ruta in lista_rutas_csv:
        with open(ruta, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                id = fila['id']
                if id not in diccionario_combinado: # si el id no esta en el diccionario lo añadimos
                    diccionario_combinado[id] = fila
                else:
                    diccionario_combinado[id].update(fila)

    fin = time.time()
    tiempo_procesamiento = fin - inicio

    return diccionario_combinado, round(tiempo_procesamiento, 2)


def crear_diccionario_series(df):
    """
    Crea un diccionario ordenado con el nombre de la serie como clave y la dirección web del póster como valor.

    Esta función procesa un DataFrame que contiene las columnas 'name', 'homepage', y 'poster_path'.
    Para cada serie, combina 'homepage' y 'poster_path' para formar una URL completa con el póster.
    Si 'homepage' o 'poster_path' están vacíos o son NaN, se reemplazan con "NOT AVAILABLE".

    Args:
        df (pd.DataFrame): DataFrame que contiene las columnas 'name', 'homepage' y 'poster_path'.

    Returns:
        dict: Diccionario ordenado con nombres de series y URLs de pósters.
    """
    # Creamos una copia del DataFrame para evitar modificar el original
    df_copy = df.copy()

    # Sustituimos los NaN y cadenas vacías con "NOT AVAILABLE"
    df_copy['homepage'] = df_copy['homepage'].fillna("NOT AVAILABLE").replace("", "NOT AVAILABLE")
    df_copy['poster_path'] = df_copy['poster_path'].fillna("NOT AVAILABLE").replace("", "NOT AVAILABLE")

    # Combinamos 'homepage' y 'poster_path'
    df_copy['full_poster_url'] = df_copy['homepage'] + df_copy['poster_path']

    # Creamos un diccionario ordenado
    series_dict = pd.Series(df_copy['full_poster_url'].values, index=df_copy['name']).to_dict()

    return series_dict
