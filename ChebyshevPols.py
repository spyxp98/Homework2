  #TODO: реализовать полиномы чебышева
  # * Шпаргалка: T_{n+1} (x) = 2xT_n (x) - T_{n-1} (x)
  # *            T_0 = 1, T_1 = x

import matplotlib.pyplot as plt



def chebPol(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return (2*x*chebPol(n-1, x) - chebPol(n-2, x))
    
if __name__ == "__main__":
    n = 100
    step = 2/n
    x1 = [-1 + i * step for i in range(n)]
    y1 = []
    for x in x1:
        y1.append(chebPol(7, x))
    plt.plot(x1, y1)
    plt.show()