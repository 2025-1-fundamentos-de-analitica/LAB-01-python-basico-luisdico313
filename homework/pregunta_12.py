"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    # Leer el archivo línea por línea
    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()

    # Diccionario para almacenar las sumas por letra de la columna 1
    sum_dict = {}

    # Procesar cada línea
    for line in lines:
        parts = line.strip().split('\t')
        if len(parts) >= 5:  # Asegurar que haya al menos 5 columnas
            letter = parts[0]  # Letra de la columna 1
            dict_str = parts[4]  # Quinta columna (formato clave:valor)
            
            # Sumar los valores de la columna 5
            total = 0
            for pair in dict_str.split(','):
                if ':' in pair:
                    value = int(pair.split(':')[1])  # Extraer el valor numérico
                    total += value
            
            # Acumular la suma para la letra correspondiente
            if letter in sum_dict:
                sum_dict[letter] += total
            else:
                sum_dict[letter] = total

    return sum_dict