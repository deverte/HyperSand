import pandas as pd
from scipy.interpolate import InterpolatedUnivariateSpline

"""
Интерполяция функций.
"""

def get_interpfs(data):
    """
    Получает словарь из интерполяционных функций для данных.

    Параметры:
        data - таблица в столбцах которой находятся данные. Тип - pandas.DataFrame.

    Возвращает словарь. Тип - dict.
    """
    interpfs = {}
    for key in data.keys():
        interpfs[key] = InterpolatedUnivariateSpline(data.index, data[key])
    return interpfs
