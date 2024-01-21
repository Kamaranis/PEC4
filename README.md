UOC. Programacion para la ciencia de datos (PEC4)
============
[![Current Version](https://img.shields.io/badge/version-1.0-green.svg)](https://github.com/Kamaranis/PEC4) 

Repositiorio para la PEC4 de la asignatura Programacion para la ciencia de datos del Master en Ciencia de Datos de la UOC en el curso 2023-2024: 
#### Codigo fuente: https://github.com/Kamaranis/PEC4
# Análisis de Series de Televisión

En este proyecto de ciencia de datos se realiza un análisis de un conjunto de datos de series de televisión. Utiliza Python para cargar, procesar, filtrar y visualizar datos relacionados con series de televisión, incluyendo géneros, duración de emisión, idiomas y más.

## Características

- Carga y combinación de múltiples archivos CSV.
- Creación de diccionarios para manejo eficiente de datos.
- Filtrado de datos basado en criterios específicos (por ejemplo, idioma, género, estado de producción).
- Análisis gráfico de tendencias a lo largo del tiempo, distribución por género, y más.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal.
- **Pandas**: Biblioteca de Python para manipulación y análisis de datos.
- **Matplotlib**: Biblioteca de Python para la creación de visualizaciones estáticas, animadas e interactivas.

## Estructura del Proyecto

- `src/`: Contiene los módulos de Python para cargar datos, filtrar y generar gráficos.
- `data/`: Directorio para los archivos de datos en formato CSV.
- `tests/`: Pruebas unitarias para los módulos.
- `docs/`: Documentación adicional y archivos Markdown para respuestas y análisis.

## Requisitos
```
Python 3.10.1
pandas
matplotlib
```
Dependiendo del SO:
```
Winrar
gzip
unrar
```

## Instalación
Para instalar las dependencias del proyecto, ejecute:

```bash
pip install -r requirements.txt
```

## Ejecución
```
python main.py
```
El programa solo admite archivos comprimidos con extensiones .zip, rar y .gz. Si se desea ejecutar con otros tipos de archivos, se debe modificar el código fuente. Asimismo depende del sisrtema operativo, pueden darse problemas para descomprimir archivos .rar. en linux y viceversa con archivos .gz en windows.
Se requeriria instalar el paquete unrar para linux y el paquete gzip para windows, asi como tener instalado winrar en windows en el directorio pro defecto

## Test o pruebas unitarias
El proyecto incluye un conjunto exhaustivo de pruebas unitarias diseñadas para verificar la funcionalidad y fiabilidad de los distintos módulos y funciones. Estas pruebas son esenciales para identificar errores, garantizar la calidad del código y facilitar el mantenimiento del software, aunque cubren solo una pequeña parte de los posibles casos de uso y solo el 60% de los modulos.

### Estructura de las Pruebas
Las pruebas unitarias se organizan en módulos separados, cada uno correspondiente a un módulo específico del código fuente:

- test_carga_datasets.py: Pruebas para el módulo carga_datasets, asegurando que la función integrar_csv_en_dataframe lee y combina correctamente los archivos CSV.
- test_descompresion.py: Verifica que el módulo descompresion maneje adecuadamente la extracción de archivos comprimidos en diferentes formatos.
test_dictio_builder.py: Pruebas para el módulo dictio_builder, enfocadas en la creación correcta de diccionarios a partir de archivos CSV y DataFrames.
- test_doc_reader.py: Asegura que la función mostrar_texto del módulo doc_reader lee y muestra correctamente el contenido de archivos Markdown.
- test_deteccion_so.py: Pruebas para la función detectar_sistema_operativo, validando la correcta detección del sistema operativo en uso.

### Ejecución de las Pruebas
Para ejecutar las pruebas unitarias, asegúrate de que estás en el directorio raíz del proyecto y que tu entorno virtual está activado. Luego, utiliza el siguiente comando:

```bash
python -m unittest discover -s tests

```
este codigo buscara automáticamente todos los archivos de prueba en el directorio tests y ejecutará las pruebas contenidas. Se mostrará un resumen, incluyendo cualquier error o fallo encontrado durante la ejecución.


## Contribuciones
Si desea contribuir a [este proyecto](https://github.com/Kamaranis/PEC4), por favor envíe un pull request. Todas las contribuciones son bienvenidas.

## Autor:
- Anton Barrera Mora (abarreramo@uoc.edu)

## License
Este proyecto esta bajo licencia `MIT`.
