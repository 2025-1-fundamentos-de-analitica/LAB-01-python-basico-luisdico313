"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """



    # Leer el archivo línea por línea
    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()

    # Diccionario para almacenar las letras únicas por valor de la columna 2
    value_to_unique_letters = {}

    # Procesar cada línea
    for line in lines:
        parts = line.strip().split('\t')
        if len(parts) >= 2:  # Asegurar que haya al menos 2 columnas
            letter = parts[0]  # Letra (columna 1)
            value = int(parts[1])  # Valor numérico (columna 2)
            
            # Inicializar conjunto si el valor no existe
            if value not in value_to_unique_letters:
                value_to_unique_letters[value] = set()
            value_to_unique_letters[value].add(letter)

    # Generar lista de tuplas (valor, lista_letras_ordenadas_sin_repetir)
    result = sorted(
        [(value, sorted(letters)) for value, letters in value_to_unique_letters.items()],
        key=lambda x: x[0]
    )

    return result