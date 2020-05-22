import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
Вывод графиков.
"""

def plt2d(data, types):
    """
    Строит двумерный график из произвольного количества таблиц.

    Параметры:
        data - список из таблиц данных типа pandas.DataFrame. Таблицы должны
    иметь два столбца - ось X и ось Y. Тип - list.
        types - список из типов графиков. Значения: "plot" - график из точек,
    соединенных прямой, "scatter" - график из точек.
    """
    # Определяем оси, на которых будем строить графики
    ax = plt.figure().gca()
    # Строим графики в зависимости от типа
    for i in range(len(types)):
        element = data[i]
        keys = element.keys()
        if types[i] == "plot":
            ax.plot(element[keys[0]], element[keys[1]])
        if types[i] == "scatter":
            ax.scatter(element[keys[0]], element[keys[1]])
    plt.show()

def plt3d(data, types):
    """
    Строит трехмерный график из произвольного количества таблиц.

    Параметры:
        data - список из таблиц данных типа pandas.DataFrame. Таблицы должны
    иметь три столбца - ось X, ось Y и ось Z. Тип - list.
        types - список из типов графиков. Значения: "plot" - график из точек,
    соединенных прямой, "scatter" - график из точек.
    """
    # Определяем оси, на которых будем строить графики
    ax = plt.figure().gca(projection='3d')
    # Строим графики в зависимости от типа
    for i in range(len(types)):
        element = data[i]
        keys = element.keys()
        if types[i] == "plot":
            ax.plot(element[keys[0]], element[keys[1]], element[keys[2]])
        if types[i] == "scatter":
            ax.scatter(element[keys[0]], element[keys[1]], element[keys[2]])
    plt.show()
