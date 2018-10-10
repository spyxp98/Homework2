import matplotlib
import matplotlib.pyplot as plt

def drawAll(funcName):

    file = open("Results/Error for {}(10)".format(funcName), 'r')
    x1, y1 = [], []
    for line in file:
        temp = line.split()
        x1.append(temp[0])
        y1.append(temp[1])
    file.close()

    file = open("Results/Error for {}(20)".format(funcName), 'r')
    x2, y2 = [], []
    for line in file:
        temp = line.split()
        x2.append(temp[0])
        y2.append(temp[1])
    file.close()

    file = open("Results/Error for {}(30)".format(funcName), 'r')
    x3, y3 = [], []
    for line in file:
        temp = line.split()
        x3.append(temp[0])
        y3.append(temp[1])
    file.close()

    file = open("Results/Error for {}(40)".format(funcName), 'r')
    x4, y4 = [], []
    for line in file:
        temp = line.split()
        x4.append(temp[0])
        y4.append(temp[1])
    file.close()

    file = open("Results/Error for {}(50)".format(funcName), 'r')
    x5, y5 = [], []
    for line in file:
        temp = line.split()
        x5.append(temp[0])
        y5.append(temp[1])
    file.close()

    file = open("Results/{}(10)".format(funcName), 'r')
    xFunc1, yFunc1 = [], []
    for line in file:
        temp = line.split()
        xFunc1.append(temp[0])
        yFunc1.append(temp[1])
    file.close()

    file = open("Results/{}(20)".format(funcName), 'r')
    xFunc2, yFunc2 = [], []
    for line in file:
        temp = line.split()
        xFunc2.append(temp[0])
        yFunc2.append(temp[1])
    file.close()

    file = open("Results/{}(30)".format(funcName), 'r')
    xFunc3, yFunc3 = [], []
    for line in file:
        temp = line.split()
        xFunc3.append(temp[0])
        yFunc3.append(temp[1])
    file.close()

    file = open("Results/{}(40)".format(funcName), 'r')
    xFunc4, yFunc4 = [], []
    for line in file:
        temp = line.split()
        xFunc4.append(temp[0])
        yFunc4.append(temp[1])
    file.close()

    file = open("Results/{}(50)".format(funcName), 'r')
    xFunc5, yFunc5 = [], []
    for line in file:
        temp = line.split()
        xFunc5.append(temp[0])
        yFunc5.append(temp[1])
    file.close()

    file = open("Data/DataFor{}(10)".format(funcName), 'r')
    xData1, yData1 = [], []
    for line in file:
        temp = line.split()
        xData1.append(temp[0])
        yData1.append(temp[1])
    file.close()

    file = open("Data/DataFor{}(20)".format(funcName), 'r')
    xData2, yData2 = [], []
    for line in file:
        temp = line.split()
        xData2.append(temp[0])
        yData2.append(temp[1])
    file.close()

    file = open("Data/DataFor{}(30)".format(funcName), 'r')
    xData3, yData3 = [], []
    for line in file:
        temp = line.split()
        xData3.append(temp[0])
        yData3.append(temp[1])
    file.close()

    file = open("Data/DataFor{}(40)".format(funcName), 'r')
    xData4, yData4 = [], []
    for line in file:
        temp = line.split()
        xData4.append(temp[0])
        yData4.append(temp[1])
    file.close()

    file = open("Data/DataFor{}(50)".format(funcName), 'r')
    xData5, yData5 = [], []
    for line in file:
        temp = line.split()
        xData5.append(temp[0])
        yData5.append(temp[1])
    file.close()


    plt.subplot(5, 2, 1)
    plt.plot(x1, y1)
    plt.title("N = 10")
    plt.grid(True)

    plt.subplot(5, 2, 3)
    plt.plot(x2, y2)
    plt.title("N = 20")
    plt.grid(True)

    plt.subplot(5, 2, 5)
    plt.plot(x3, y3)
    plt.title("N = 30")
    plt.grid(True)

    plt.subplot(5, 2, 7)
    plt.plot(x4, y4)
    plt.title("N = 40")
    plt.grid(True)

    plt.subplot(5, 2, 9)
    plt.plot(x5, y5)
    plt.title("N = 50")
    plt.grid(True)

    plt.subplot(5, 2, 2)
    plt.plot(xFunc1, yFunc1)
    plt.scatter(xData1, yData1)
    plt.title("N = 10")
    plt.grid(True)

    plt.subplot(5, 2, 4)
    plt.plot(xFunc2, yFunc2)
    plt.scatter(xData2, yData2)
    plt.title("N = 20")
    plt.grid(True)

    plt.subplot(5, 2, 6)
    plt.plot(xFunc3, yFunc3)
    plt.scatter(xData3, yData3)
    plt.title("N = 30")
    plt.grid(True)

    plt.subplot(5, 2, 8)
    plt.plot(xFunc4, yFunc4)
    plt.scatter(xData4, yData4)
    plt.title("N = 40")
    plt.grid(True)

    plt.subplot(5, 2, 10)
    plt.plot(xFunc5, yFunc5)
    plt.scatter(xData5, yData5)
    plt.title("N = 50")
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    funcType = input("Cos, Exp, Poly, Rtl \n")
    drawAll(funcType)