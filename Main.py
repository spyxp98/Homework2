# TODO: автоматизировать процесс для всех типов функций
#       

import math

Rtl = lambda x: (x**5 + 2*x**4 - 10 * x **2 + x + 1)/(x**2 + 1)
Poly = lambda x: x**5 + 2*x**4 - 10 * x **2 + x + 1
Exp = math.exp
Cos = math.cos
functions = [Rtl, Poly, Exp, Cos]

def getData(filename):
    file = open("Data/{}".format(filename))
    x = []
    y = {}
    for line in file:
        temp = line.split()
        x.append(float(temp[0]))
        y[float(temp[0])] = float(temp[1])
    return x, y

def chebPol(n, x):
    return math.cos(n * math.acos(x))

    
def coeff(x, y, n):
    c = 0
    if n == 0:
        norm = len(x)
    else:
        norm = len(x) / 2
    for i in range(len(x)):
        c += y[x[i]] * chebPol(n, x[i]) / norm 
    return c

def error(func, x, y):
    err = {}
    for i in range(len(x)):
        try:
            err[x[i]] = func(x[i]) - y[i]
        except ZeroDivisionError:
            pass
    return err

def writeResults(funcType, N, fileName):
    x, y = getData("DataFor{}({})".format(fileName, N))
    xTest = [-1 + (2/1000) * i for i in range(1000)]
    yExp = []
    yTrue = []
    for x1 in xTest:
        temp = 0
        for n in range(N):
            c = coeff(x, y, n)
            temp += c * chebPol(n, x1)
        yExp.append(temp)
    
    err = error(funcType, xTest, yExp)

    file = open("Results/{}({})".format(fileName, N), 'w')
    for i in range(len(xTest)):
        file.write("{} {} \n".format(xTest[i], yExp[i]))
    file.close()

    file = open("Results/Error for {}({})".format(fileName, N), 'w')
    for i in range(len(err)):
        try:
            file.write("{} {} \n".format(xTest[i], err[xTest[i]]))
        except KeyError:
            pass
    file.close()

if __name__ == "__main__":
    N = 0
    while N < 50:
        N += 10
        writeResults(Cos, N, "Cos")
        writeResults(Exp, N, "Exp")
        writeResults(Rtl, N, "Rtl")
        writeResults(Poly, N, "Poly")      
    
