"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """


    with open("files/input/data.csv","r") as file:
        lines = file.readlines()

    month_counts = {}

    for line in lines:
        parts = line.strip().split('\t')
        
        if len(parts) >= 3:
            date = parts[2]
            month = date.split('-')[1]
            month_counts[month] = month_counts.get(month,0) + 1
    
    sorted_months = sorted(month_counts.items(), key=lambda x:int(x[0]))

    return sorted_months