# Documentación

1. [Introducción](#introducción)
2. [Funciones](#funciones)
3. [Tests](#tests)
4. [Graficas y conclusiones](#conclusiones)


## Introducción
En este proyecto de ciencia de datos se realiza un análisis de un conjunto de datos de series de televisión. Utiliza Python para cargar, procesar, filtrar y visualizar datos relacionados con series de televisión, incluyendo géneros, duración de emisión, idiomas y más.
Este módulo ejecuta el flujo principal del programa para el análisis de 
datos de series de televisión.
Incluye la descompresión de archivos en virtud del sistema operativo, 
carga de datos, generación de diccionarios y visualizaciones gráficas.

## Funciones
- main.py: 

Este módulo ejecuta el flujo principal del programa para el análisis para el análisis de datos de series de televisión.
Incluye la descompresión de archivos en virtud del sistema operativo, 
carga de datos, generación de diccionarios y visualizaciones gráficas.

- carga_dataset.py:

Este módulo proporciona funcionalidades para cargar y combinar múltiples
conjuntos de datos CSV.
Utiliza pandas para leer y fusionar archivos CSV basándose en una columna común 'id'.

- Funciones:


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



