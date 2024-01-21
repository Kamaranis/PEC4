# filtrado_series.py
"""
Este módulo ofrece funcionalidades para filtrar series de televisión basadas en criterios específicos como el idioma original, palabras clave en el resumen, el año de inicio y el estado de producción. Estas funciones permiten analizar y extraer subconjuntos de datos relevantes para análisis posteriores o visualizaciones.

Funciones:
    filtrar_series_por_idioma_y_palabras: Filtra series por el idioma original y la presencia de palabras clave en el resumen.
    filtrar_series_2023_canceladas: Identifica series que comenzaron en 2023 y han sido canceladas.
    filtrar_series_japonesas: Extrae series que incluyen el idioma japonés, mostrando detalles específicos como nombres y productoras.

Estas son útiles para explorar tendencias y patrones en la producción de series de televisión, habilitando la realizacion de analisis detallados sobre la diversidad linguistica, tematica y la dinamica de produccian a lo largo del tiempo.
"""

import pandas as pd

# Funcion para filtrar series por idioma y palabras

def filtrar_series_por_idioma_y_palabras(df, idioma='en', palabras=['mystery', 'crime']):
    """
    Filtra y muestra los nombres de las series cuyo idioma original sea el especificado y 
    cuyo resumen contenga alguna de las palabras dadas.

    Args:
        df (pd.DataFrame): DataFrame que contiene los datos de las series.
        idioma (str): Idioma original de las series a filtrar.
        palabras (list): Lista de palabras a buscar en el resumen.

    Returns:
        pd.DataFrame: DataFrame filtrado con los nombres de las series que cumplen los criterios.
    """
    # Filtramo por idioma originaln y hacemos una copia del DataFrame independiente
    df_filtrado = df[df['original_language'] == idioma].copy()

    # Convertimos la columna 'overview' a minúsculas
    df_filtrado['overview'] = df_filtrado['overview'].str.lower()

    # Filtramos por palabras en el resumen
    palabras_regex = '|'.join(palabras)  # Creamos una expresión regular para buscar cualquiera de las palabras
    df_filtrado = df_filtrado[df_filtrado['overview'].str.contains(palabras_regex, na=False)]

    return df_filtrado['name']

# Funcion para filtrar series de 2023 que han sido canceladas

def filtrar_series_2023_canceladas(df, year='2023', status='canceled'):
    """
    Filtra y devuelve los nombres de las series que comenzaron en el año especificado y han sido canceladas.
    En este caso asibamos el valor por defecto de 'status' a 'canceled' y especificamos el valor por defecto 
    de 'year' a '2023'.

    Args:
        df (pd.DataFrame): DataFrame que contiene los datos de las series.
        year (str): Año de inicio de las series a filtrar.
        status (str): Estado final de las series a filtrar ('Canceled').

    Returns:
        pd.Series: Serie de pandas con los nombres de las series que cumplen los criterios.
    """
    # Convertimos 'first_air_date' a datetime
    df['first_air_date'] = pd.to_datetime(df['first_air_date'], errors='coerce')
    
    # Filtramos por año y status y hacemos una copia del DataFrame independiente
     # Aseguramos que el año extraído sea igual al año especificado y que el estado sea 'canceled'
    df_filtrado = df[(df['first_air_date'].dt.year == int(year)) & 
                     (df['status'].str.lower() == status)]
    # Hacemos una copia del DataFrame filtrado
    df_filtrado = df_filtrado.copy()

    return df_filtrado['name']


# Funcion para filtrar series japonesas

def filtrar_series_japonesas(df):
    """
    Filtra y devuelve un DataFrame con los nombres, nombres originales, plataformas de emisión y 
    empresas productoras de todas las series que incluyan el idioma japonés.

    Args:
        df (pd.DataFrame): DataFrame que contiene los datos de las series.

    Returns:
        pd.DataFrame: DataFrame filtrado con las columnas especificadas.
    """
    # Filtramos las series que incluyen el idioma japonés
    df_filtrado = df[df['languages'].str.contains('ja', na=False)]

    # Seleccionamos las columnas relevantes
    columnas = ['name', 'original_name', 'networks', 'production_companies']
    df_filtrado = df_filtrado[columnas]

    return df_filtrado
