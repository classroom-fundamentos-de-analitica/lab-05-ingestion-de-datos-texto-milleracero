import os
import pandas as pd

def generate_csv_files(ruta):
    """
    Función para generar un archivo CSV a partir de archivos de texto organizados en directorios de sentimiento.
    
    Args:
        ruta (str): Ruta del directorio que contiene los archivos .txt organizados por sentimiento.
    """
    datos = {"frase": [], "sentimiento": []}  # Diccionario para almacenar frases y sentimientos

    # Recorrer la estructura de directorios y archivos
    for raiz, _, archivos in os.walk(ruta):
        for archivo in archivos:
            if archivo.endswith(".txt"):  # Solo procesar archivos .txt
                with open(os.path.join(raiz, archivo), "r") as f:
                    datos["frase"].append(f.read())  # Añadir el contenido del archivo
                    datos["sentimiento"].append(os.path.basename(raiz))  # Añadir el nombre de la carpeta como sentimiento

    # Crear DataFrame y guardarlo como CSV
    pd.DataFrame(datos).to_csv(f"{os.path.basename(ruta)}_dataset.csv", index=False)

# Generar los CSV para las carpetas "train" y "test"
for carpeta in ["train", "test"]:
    generate_csv_files(carpeta)


