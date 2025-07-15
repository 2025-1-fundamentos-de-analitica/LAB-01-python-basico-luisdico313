"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    # Leer el archivo línea por línea
    with open("files\input\data.csv", "r") as file:
        lines = file.readlines()

    # Diccionarios para almacenar los valores mínimos y máximos por clave
    min_values = {}
    max_values = {}

    # Procesar cada línea
    for line in lines:
        parts = line.strip().split('\t')
        if len(parts) >= 5:  # Asegurar que la línea tenga al menos 5 columnas
            dict_str = parts[4]  # Quinta columna (diccionario)
            # Procesar cada par clave-valor en la quinta columna
            for pair in dict_str.split(','):
                if ':' in pair:
                    key, value_str = pair.split(':')
                    value = int(value_str)
                    # Actualizar el mínimo
                    if key not in min_values or value < min_values[key]:
                        min_values[key] = value
                    # Actualizar el máximo
                    if key not in max_values or value > max_values[key]:
                        max_values[key] = value

    # Generar lista de tuplas (clave, min, max) ordenada alfabéticamente
    result = sorted(
        [(key, min_values[key], max_values[key]) for key in min_values],
        key=lambda x: x[0]
    )

    return result