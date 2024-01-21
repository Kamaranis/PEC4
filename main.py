#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Este módulo ejecuta el flujo principal del programa para el análisis de 
datos de series de televisión.
Incluye la descompresión de archivos en virtud del sistema operativo, 
carga de datos, generación de diccionarios y visualizaciones gráficas.
"""
# main.py

# Importamos el modulo para salir de programas:
import sys
# Importamos el modulo para descomprimir archivos comprimidos:
import src.descompresion
# Importamos modulo para detectar el sistema operativo:
from src.deteccion_so import detectar_sistema_operativo as detec_so
# Importamos modulo para cargar los datasets:
import src.carga_datasets
# Importamos modulo para crear diccionarios:
import src.dictio_builder
# Importamos modulo para mostrar texto desde un archivo:
import src.doc_reader
# Importamos modulo para mostrar las rutas de los archivos .csv:
import src.rutas_csv
# Importamos modulo para calcular los dias de emision:
import src.dias_emision
# importamos modulo para mostrar series por idioma y palabras:
from src.filtrado_series import filtrar_series_por_idioma_y_palabras as fsp
# importamos modulo y funcion para mostrar las series de 2023 que han sido canceladas:
from src.filtrado_series import filtrar_series_2023_canceladas as fsc
# importamos modulo y funcion para mostrar las series japonesas:
from src.filtrado_series import filtrar_series_japonesas as fsj
# importamos modulo para mostrar series por año de inicio:
from src.graficas import grafico_series_anyo as gsa
# importamos modulo y funcion para mostrar series por decada y tipo:
from src.graficas import grafico_series_por_decada_y_tipo as gsdt
# importamos el modulo para mostrar grafica circular de generos de series:
from src.graficas import grafico_series_por_genero as gsg


# Detectamos el sistema operativo:
sistema_operativo: str = detec_so()

# Ejecutamos la funcion acorde al so:
if __name__ == "__main__":
    if sistema_operativo in ('Linux', 'Darwin'):
        # Pedimos al usuario el nombre del archivo:
        nombre_ext_archivo: str = input("Introduce nombre y extension del archivo: ")
        # Construimos la ruta al archivo:
        ruta_archivo: str = f"data/{nombre_ext_archivo}"
        # Descomprimimos el archivo:
        src.descompresion.descomprimir_archivos_unix(ruta_archivo)
    elif sistema_operativo == 'Windows':
        # Pedimos al usuario el nombre del archivo:
        nombre_ext_archivo: str = input("Introduce nombre y extension del archivo: ")
        # Construimos la ruta al archivo:
        ruta_archivo: str = f"data/{nombre_ext_archivo}"
        # Descomprimimos el archivo:
        src.descompresion.descomprimir_archivos_nt(ruta_archivo)
    else:
        print("Sistema Operativo no soportado para la descompresión automática.")
        sys.exit()
input("\nPresiona Enter para continuar con la carga de datasets...")

# Cargamos los datasets y calculamos tiempo:
dataframe, tiempo_procesamiento = src.carga_datasets.integrar_csv_en_dataframe()
print(f"\nDataframe combinado: {dataframe}")
# print(dataframe)
print(f"\nTiempo de procesamiento: {tiempo_procesamiento} segundos")

input("Presiona Enter para continuar con la creacion de diccionarios...")

# Creamos diccionario y calculamos tiempo:
diccionario, tiempo_procesamiento_dict = src.dictio_builder.integrar_csv_en_diccionario()

i:int = 0 # Contador para limitar la salida
for k,v in diccionario.items(): # Recorremos el diccionario
    print(f"{k}:{v}") # Mostramos la clave y el valor}"
    i += 1 # Incrementamos el contador
    if i >= 2: # Limitamos los registros para no saturar la memoria
        break # Salimos del bucle

print(f"\nTiempo de procesamiento: {tiempo_procesamiento_dict} segundos\n")

# Respuesta a la pregunta 1.4
input("\nPresiona Enter para continuar mostrar la respuesta al enunciado 1.4\n")

src.doc_reader.mostrar_texto("docs/1_4.md")

# Respuesta a la pregunta 2.1 sobre tiempos de emision
input("\nPulsa para mostrar las 10 series con mayor tiempo de emisión...\n")

# Mostramos las series con mayor tiempo de emisión:
dataframe, df_valid, top_10_series = src.dias_emision.calculo_dias_emision(dataframe)
print(top_10_series[['original_name', 'name', 'air_days']])

# Creamos un diccionario con las series y sus URLs de pósters:
SERIES_DICT = src.dictio_builder.crear_diccionario_series(df_valid)

input("\nPulsa para mostrar los primeros 5 registros del diccionario...\n")

# Imprimimos los primeros 5 registros del diccionario
i = 0  # Contador para limitar el número de registros mostrados
for name, url in SERIES_DICT.items():
    print(f"Nombre de la serie: {name}, URL del póster: {url}")
    i += 1
    if i >= 5:
        break

input("\nEnter para mostrar los 10 primeros registros filtrados por idioma y keywords\n")
# Creamos variables para filtrar por idioma y palabras clave:
idioma: str = 'en'
palabras: list = ['mystery', 'crime']

# Mostramos los 10 primeros registros filtrados:
dataframe_filtrado = fsp(dataframe, idioma, palabras)
# Mostramos los 10 primeros registros filtrados:
print(dataframe_filtrado.head(10))

input("\npulsa Enter para mostrar las series de 2023 que han sido canceladas")

# Mostramos las series de 2023 que han sido canceladas:
dataframe_filtrado = fsc(dataframe)

# Mostramos las series de 2023 que han sido canceladas:
print(dataframe_filtrado.head(20))

input("\npulsa Enter para mostrar series japonesas")

# Filtramos las series japonesas:
dataframe_filtrado = fsj(dataframe)

# Mostramos las series japonesas:
print(dataframe_filtrado.head(20))

input("\n presiona Enter para mostrar una grafica de peliculas por año de inicio")

# Mostramos una gráfica de películas por año de inicio:
gsa(dataframe)

input("\n presiona Enter para mostrar una grafica de peliculas por decada y tipo")
gsdt(dataframe)

# Mostramos una gráfica circular de géneros de series:
input("\nPresiona Enter para mostrar una gráfica circular de géneros de series")
gsg(dataframe)

# Respuesta a la pregunta 1.4
input("\nPresiona Enter para mostrar el redactado de conclusiones\n")

src.doc_reader.mostrar_texto("docs/5_conclusiones.txt")


input("\nPresiona Enter para finalizar el programa...")
