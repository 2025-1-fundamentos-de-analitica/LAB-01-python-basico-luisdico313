"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """



    # Leer el archivo línea por línea
    with open("files\input\data.csv", "r") as file:
        lines = file.readlines()

    # Diccionario para almacenar las sumas por letra de la columna 4
    sum_dict = {}

    # Procesar cada línea
    for line in lines:
        parts = line.strip().split('\t')
        if len(parts) >= 5:  # Asegurar que haya al menos 5 columnas
            value_col2 = int(parts[1])  # Valor de la columna 2
            letters_col4 = parts[3].split(',')  # Letras de la columna 4
            
            # Actualizar sumas para cada letra en la columna 4
            for letter in letters_col4:
                if letter in sum_dict:
                    sum_dict[letter] += value_col2
                else:
                    sum_dict[letter] = value_col2

    # Ordenar el diccionario alfabéticamente por clave
    sorted_sum_dict = {k: sum_dict[k] for k in sorted(sum_dict)}

    return sorted_sum_dict