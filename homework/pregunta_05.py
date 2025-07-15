"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """



    with open("files/input/data.csv","r") as file:
        lines = file.readlines()

    max_values = {}
    min_values = {}

    for line in lines:
        parts = line.strip().split('\t')
        
        if len(parts) >= 2:
            letter = parts[0]
            value = int(parts[1])

            if letter not in max_values or value > max_values[letter]:
                max_values[letter] = value

            if letter not in min_values or value < min_values[letter]:
                min_values[letter] = value
    
    result = sorted(
        [(letter,max_values[letter], min_values[letter]) for letter in max_values],
         key = lambda x:x[0]
    )

    return result




