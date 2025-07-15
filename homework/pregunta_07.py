"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """



    # Leer el archivo línea por línea
    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()

    # Diccionario para almacenar las letras agrupadas por valor de la columna 2
    value_to_letters = {}

    # Procesar cada línea
    for line in lines:
        parts = line.strip().split('\t')
        if len(parts) >= 3:  # Asegurar que haya al menos 3 columnas
            col1 = parts[0]  # Letra (columna 1)
            col2 = int(parts[1])  # Valor numérico (columna 2)
            
            # Agregar la letra al grupo correspondiente al valor de col2
            if col2 not in value_to_letters:
                value_to_letters[col2] = []
            value_to_letters[col2].append(col1)

    # Generar lista de tuplas (valor_col2, lista_letras) ordenada por valor_col2
    result = sorted([(value, letters) for value, letters in value_to_letters.items()])

    return result



