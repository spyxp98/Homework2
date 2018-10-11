# многочлен, дробно-рациональная, экспонента, гармоническая
# Сгенирируем по два набора данных для каждой функции
# один с шагом через постоянный интервал и со случайным шагом
import math
import random
import matplotlib
import matplotlib.pyplot as plt
from os import path

rtl = lambda x: (x**5 + 2*x**4 - 10 * x **2 + x + 1)/(x**2 + 1)
poly = lambda x: x**5 + 2*x**4 - 10 * x **2 + x + 1
exp = math.exp
cos = math.cos
functions = [rtl, poly, exp, cos]

def chebPolZeros(n):
    x_k = []
    for i in range(n):
        x_k.append(math.cos(math.pi * (i + 0.5) / n))
    return x_k

def xRange(N):
    x = []
    x = chebPolZeros(N)
    return x


def genData(func, x):
    y = {}
    for temp in x:
        y[temp] = func(temp)
    return y


# Нарисовать
def draw(fileName):
    file = open("Data/{}".format(fileName), 'r')
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
    my_file = open("Data/DataFor{}({})".format(name, len(y)), 'w')
    for x in y:
        my_file.write("{} {} \n".format(x, y[x]))
    my_file.close()




if __name__ == '__main__':
    N = 0
    while N < 50:
        N += 10
        createFile(genData(exp, xRange(N)), "Exp")
        createFile(genData(cos, xRange(N)), "Cos")
        createFile(genData(rtl, xRange(N)), "Rtl")
        createFile(genData(poly, xRange(N)), "Poly")