def mostrar_texto(ruta_archivo_md: str):
    """
    Lee y muestra el contenido de un archivo de texto.

    Args:
        ruta_archivo_md (str): Ruta al archivo Markdown.

    Returns:
        None
    """
    while True:
        try:
            with open(ruta_archivo_md, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                print(contenido)
                break  # Salimos del bucle si el archivo se encuentra y se lee con éxito
        except FileNotFoundError:
            print("El archivo no se encontró en la ruta especificada.")
            ruta_archivo_md = input("Por favor, introduce la ruta correcta al archivo: ")
