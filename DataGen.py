# многочлен, дробно-рациональная, экспонента, гармоническая
# Сгенирируем по два набора данных для каждой функции
# один с шагом через постоянный интервал и со случайным шагом
import math
import random
import matplotlib
import matplotlib.pyplot as plt
from os import path

rtl = lambda x: (x**3 + 2*x**2 - x + 1)/(x**2 - 2*x**2 + 1)
poly = lambda x: x**3 + 2*x**2 - x + 1
exp = math.exp
cos = math.cos
functions = [rtl, poly, exp, cos]

def floatRange(min, max, steps, rand):
    x = []
    step = (max - min)/steps
    for i in range(steps):
        if not rand:
            currX = min + i*step
        else:
            currX = random.uniform(min, max)

        x.append(currX)
    
    return x


def genData(func, min, max, steps, rand):
    y = {}
    for x in floatRange(min, max, steps, rand):
        try:
            y[x] = func(x)
        except ZeroDivisionError:
            pass

    return y


# Нарисовать
def draw(fileName):
    file = open("{}".format(fileName), 'r')
    x1 = []
    y1 = []
    for line in file:
        l = line.split()
        x1.append(l[0])
        y1.append(l[1])
    file.close()
    plt.scatter(x1, y1)
    plt.show()

# Записать данные в файл
def createFile(y, name):
    my_file = open("Data/DataFor{}".format(name), 'w')
    for x in y:
        my_file.write("{} {} \n".format(x, y[x]))
    my_file.close()




if __name__ == '__main__':
    # 
    # createFile(genData(cos, 0, 4, 100, False), "Cos")
    # createFile(genData(cos, 0, 4, 100, True), "Cos(Rand)")
    createFile(genData(exp, -1, 1, 100, False), "Exp")
    # createFile(genData(exp, -10, 10, 100, True), "Exp(Rand)")
    # createFile(genData(rtl, -10, 10, 100, False), "Rtl")
    # createFile(genData(rtl, -10, 10, 10000, True), "Rtl(Rand)")
    # createFile(genData(poly, -10, 10, 100, False), "Poly")
    # createFile(genData(poly, -10, 10, 100, True), "Poly(Rand)")
    draw("Data/DataForExp")