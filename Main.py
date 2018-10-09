import math
import matplotlib
import matplotlib.pyplot as plt

def getData(filename):
    file = open("Data/{}".format(filename))
    x = []
    y = {}
    for line in file:
        temp = line.split()
        x.append(float(temp[0]))
        y[float(temp[0])] = float(temp[1])
    # Сортируем х
    x.sort()
    return x, y

def chebPol(n, x):
    if n == 0:
        return 0
    elif n == 1:
        return x
    else:
        return 2 * x * chebPol(n-1, x) - chebPol(n-2, x)
    
def coeff(x, y, n):
    N = len(x)
    step = 2 / N
    c = 0
    for i in range(N):
        try:
            c += chebPol(n, x[i]) * y[x[i]] * 1 / (math.sqrt(1 - (x[i])**2)) * step /math.pi
        except ZeroDivisionError:
            pass
    return c


if __name__ == "__main__":
    x, y = getData("DataForExp")
    stepsTest = 1000
    N = 10
    xTest = [-1 + (2/stepsTest)*i for i in range(stepsTest)]
    yTest = {}
    for x1 in xTest:
        yTest[x1] = 0
        for i in range(N):
            yTest[x1] += coeff(x, y, i) * chebPol(i, x1)
    xTest.sort()
    yPlot = []
    for temp in xTest:
        yPlot.append(yTest[temp])
    plt.plot(xTest, yPlot)
    plt.show()
    
    
