import DataGen
import ChebyshevPols

import matplotlib
import matplotlib.pyplot as plt
import math


def getData(filename):
    x = []
    y = {}
    file = open('Data/{}'.format(filename), 'r')
    for line in file:
        l = line.split()
        x.append(float(l[0]))
        y[l[0]] = float(l[1])
    file.close()
    x.sort()
    return x, y

def weight(x):
    v1 = x**2
    root = math.sqrt(1 - v1)
    val = 1/root
    return val

if __name__ == "__main__":
# Отсортированные данные из файла:
    x, y = getData("DataForExp")
    n = 100
    N = 4
    c = [0 for _ in range(N)]
    for i in range(N):
        for x1 in x:
            c[i] += ChebyshevPols.chebPol(i, x1) * y[x1] * weight(x1) / math.pi
    x_test = []
    step = 2/1000
    for i in range(1000):
        x_temp = -1 + (i * step)
        x_test.append(x_temp)
    y_test = []
    for x1 in x_test:
        y_value = 0
        for i in range(N):
            y_value += c[i] * ChebyshevPols.chebPol(i, x1)
            y_test.append(y_value)
    
    plt.scatter(x_test, y_test)
    plt.show()