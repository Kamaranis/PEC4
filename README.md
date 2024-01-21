UOC. Programacion para la ciencia de datos (PEC4)
============
[![Current Version](https://img.shields.io/badge/version-1.0-green.svg)](https://github.com/Kamaranis/PEC4) 

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

## Contribuciones
Si desea contribuir a [este proyecto](https://github.com/Kamaranis/PEC4), por favor envíe un pull request. Todas las contribuciones son bienvenidas.

## Autor:
- Anton Barrera Mora (abarreramo@uoc.edu)

## License
Este proyecto esta bajo licencia `MIT`.
