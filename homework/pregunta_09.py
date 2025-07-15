"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """



    # Leer el archivo línea por línea
    with open('files\input\data.csv', 'r') as file:
        lines = file.readlines()

    # Diccionario para contar la frecuencia de cada clave
    key_counts = {}

    # Procesar cada línea
    for line in lines:
        parts = line.strip().split('\t')
        if len(parts) >= 5:  # Asegurar que la línea tenga al menos 5 columnas
            dict_str = parts[4]  # Quinta columna (formato clave:valor)
            # Procesar cada par clave:valor
            for pair in dict_str.split(','):
                if ':' in pair:
                    key = pair.split(':')[0]  # Extraer la clave
                    key_counts[key] = key_counts.get(key, 0) + 1  # Incrementar el contador

    return key_counts
