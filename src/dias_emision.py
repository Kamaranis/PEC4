# dias_emision.py
"""
dias_emision.py

Este módulo contiene funciones para calcular y analizar la duración de emisión de series de televisión. 
Proporciona funcionalidades para procesar datos de series, incluyendo la conversión de fechas de emisión a formatos de fecha de Python y el cálculo del número total de días que cada serie ha estado en emisión.

Funciones:
    calculo_dias_emision(df): Calcula el número de días de emisión para cada serie en un DataFrame y dvuelve los 10 registros con mayor tiempo de emisión.

Ejemplo de uso:
    df_modificado, top_10_series = calculo_dias_emision(df_original)
"""

import pandas as pd
def calculo_dias_emision(df):
    """
    Calcula el número de días que cada serie ha estado en emisión y devuelve los 10 registros con mayor tiempo de emisión.

    Args:
        df (pd.DataFrame): DataFrame que contiene las columnas 'first_air_date' y 'last_air_date'.

    Returns:
        pd.DataFrame: DataFrame original con las columnas 'first_air_date' y 'last_air_date' convertidas a datetime.
        pd.DataFrame: DataFrame con los 10 registros con mayor tiempo de emisión validos para el calculo.
        pd.DataFrame: DataFrame con los 10 registros con mayor tiempo de emisión ordenados de manera descendente.
    """
    # Convertimos las columnas 'first_air_date' y 'last_air_date' a datetime
    df['first_air_date'] = pd.to_datetime(df['first_air_date'], format='%Y-%m-%d', errors='coerce')
    df['last_air_date'] = pd.to_datetime(df['last_air_date'], format='%Y-%m-%d', errors='coerce')

    # Filtramos las filas donde ambas fechas son válidas y creamos una copia independiente
    df_valid = df.dropna(subset=['first_air_date', 'last_air_date']).copy()

    # Calculamos la diferencia en días y creamos la columna 'air_days'
    df_valid['air_days'] = (df_valid['last_air_date'] - df_valid['first_air_date']).dt.days

    # Convertimos 'air_days' a entero
    df_valid['air_days'] = df_valid['air_days'].astype(int)

    # Ordenamos el DataFrame por 'air_days' de manera descendente y muestra los primeros 10 registros
    top_10_longest_airing = df_valid.sort_values(by='air_days', ascending=False).head(10)
    
    return df, df_valid, top_10_longest_airing
