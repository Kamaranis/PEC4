# graficas.py
"""
Este módulo contiene funciones para la visualización de datos 
relacionados con series de televisión. 
Utiliza la biblioteca matplotlib para generar gráficos que 
facilitan la interpretación de las tendencias 
y patrones en los datos de series, como la distribución de 
series a lo largo de los años, por décadas, 
tipos y géneros.

Funciones:
    grafico_series_anyo: Genera un gráfico de barras que muestra 
    el número de series por año de inicio.
    grafico_series_por_decada_y_tipo: Crea un gráfico de 
    líneas que representa el número de series de cada categoría 
    de 'type' producidas en cada década desde 1940.
    grafico_series_por_genero: Muestra un gráfico circular del 
    número de series por género y el porcentaje respecto al total, 
    agrupando los géneros menos representativos en "Other".

Estas tipo de graficas son esenciales para el análisis exploratorio 
de datos, habilitandonos a identificar tendencias, patrones
y anomalías en la producción y categorización de series de televisión.
"""
import matplotlib.pyplot as plt
import pandas as pd

# Función para mostrar un gráfico de barras del número de series por año de inicio
def grafico_series_anyo(df):
    """
    Muestra un gráfico de barras del número de series 
    por año de inicio.

    Args:
        df (pd.DataFrame): DataFrame que contiene los datos de 
        las series, incluyendo la fecha de inicio.
    """
    # Establecemos la fecha de inicio como datetime
    df['first_air_date'] = pd.to_datetime(df['first_air_date'], errors='coerce')

    # Extraemos el año de inicio
    df['start_year'] = df['first_air_date'].dt.year

    # Filtramos para incluir solo años menores a 2024
    df = df[df['start_year'] < 2024]
    df = df.dropna(subset=['start_year'])  # Eliminamos los valores nulos

    # Convertimos el año de inicio a entero
    df['start_year'] = df['start_year'].astype(int)

    # Agrupamos por año y contamos el número de series
    series_por_ano = df.groupby('start_year').size()

    # Creamos un gráfico de barras
    plt.figure(figsize=(12, 8))  # Ajustamos el tamaño del gráfico
    series_por_ano.plot(kind='bar')

    # Agregamos títulos y etiquetas
    plt.title('Número de series por año de inicio')
    plt.xlabel('Año de inicio')
    plt.ylabel('Número de series')

    # Rotamos las etiquetas del eje x
    # Rotamos 45 grados para que no se superpongan
    plt.xticks(rotation=45)
    # Ajustamos la escala de la cuadrícula en el eje y
    # Establecemos las marcas en el eje y cada 1000 unidades
    plt.yticks(range(0, max(series_por_ano)+1, 1000))
    # Agregamos cuadrícula al eje y
    plt.grid(True, axis='y')

    # Mostramos el gráfico
    plt.show()


def grafico_series_por_decada_y_tipo(df):
    """
    Muestra un gráfico de líneas del número de 
    series de cada categoría de 'type' producidas 
    en cada década desde 1940.

    Args:
        df (pd.DataFrame): \
            DataFrame que contiene los datos de las series, 
            incluyendo la fecha de inicio y el tipo.
    """
    # Convertimos 'first_air_date' a datetime
    df['first_air_date'] = pd.to_datetime(df['first_air_date'], errors='coerce')

    # Eliminamos filas con 'first_air_date' NaN
    df2 = df.dropna(subset=['first_air_date']).copy()

    # Extraemos la década y convertimos a entero
    df2['decade'] = (df2['first_air_date'].dt.year // 10 * 10).astype(int)

    # Filtramos para incluir solo décadas desde 1940 en adelante
    df2 = df2[df2['decade'] >= 1940]

    # Agrupamos por década y tipo, y contamos el número de series
    series_por_decada_y_tipo = df2.groupby(['decade', 'type']).size().unstack(fill_value=0)

    # Creamos el gráfico de líneas
    fig, ax = plt.subplots(figsize=(10, 6))

    # Dibujamos el gráfico de líneas
    series_por_decada_y_tipo.plot(kind='line', ax=ax)

    # Obtenemos el máximo valor en el eje y para establecer
    # el límite superior
    max_value = series_por_decada_y_tipo.max().max()
    # Ajustamos el límite superior para que sea múltiplo de 2500
    ax.set_ylim(0, max_value + (2500 - max_value % 2500))

    # Establecemos las marcas (ticks) del eje y
    ax.set_yticks(range(0, int(max_value) + 2500, 2500))

    # Agregamos títulos y etiquetas
    ax.set_title('Número de series por década y tipo desde 1940')
    ax.set_xlabel('Década')
    ax.set_ylabel('Número de series')
    ax.legend(title='Tipo de serie')

    # Agregamos cuadrícula al eje y
    ax.grid(True, axis='y')

    # Mostramos el gráfico
    plt.show()

def grafico_series_por_genero(df):
    """
    Muestra un gráfico circular del número de series por género y el porcentaje respecto al total.

    Args:
        df (pd.DataFrame): DataFrame que contiene los datos de las series, incluyendo los géneros.
    """
    # Dividimos los géneros y contamos la frecuencia de cada uno
    generos = df['genres'].dropna().str.split(', ').explode()
    conteo_generos = generos.value_counts()

    # Calculamos el total de series
    total_series = conteo_generos.sum()

    # Agrupamos géneros menores en "Other"
    conteo_generos = conteo_generos[conteo_generos / total_series >= 0.01]
    conteo_generos['Other'] = total_series - conteo_generos.sum()

     # Creamos el gráfico circular
    plt.figure(figsize=(12, 12))  # Adaptamos el tamaño para que se lean los valores
    explode = [0.1 if conteo_generos.iloc[i] / total_series >= 0.05 else 0 for i in range(len(conteo_generos))]

    # Especificamos las etiquetas y los porcentajes
    labels = \
        [f'{genre}: \
         {percent:.1f}%' for genre, percent in zip(conteo_generos.index, (conteo_generos / total_series * 100))]
    conteo_generos.plot(kind='pie', startangle=140, explode=explode, labels=labels, textprops={'fontsize': 8})

    # Agregamos título
    plt.title('Porcentaje de series por género')

    # Desactivamos las etiquetas de los ejes
    plt.axis('off')

    # Mostramos el gráfico
    plt.show()
