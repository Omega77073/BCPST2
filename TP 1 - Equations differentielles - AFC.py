## Bibliothèques
import numpy as np
import matplotlib.pyplot as plt
import random as rd

## 1
##a, b = 0, 50
##y_0, n = 1, 255
##t, y  = [a], [y_0]
##h = (b-a)/n
##for k in range(0,n):
##    y.append(y[k] + h*(np.sin(t[k])*np.sin(y[k])))
##    t.append(k*h)
##plt.plot(t, y)
##plt.show()

## 2


def euler(F, borne_a, borne_b, y_0, n):
    t_array = [a]
    y_array = [y_0]
    stepSize = (borne_b-borne_a)/n

    for index in range(0,n):
        currentY = y_array[index]
        nextY = currentY + stepSize*F(t_array[index],currentY)

        y_array.append(nextY)
        t_array.append(borne_a + stepSize * (index+1))

    return (t_array, y_array)


##
#### 3
def F(t,y):
    return y
##
##a, b, y_0 = 0,1,1
##for nMax in [10,100,1000]:
##    t, y = euler(F,a,b,y_0,nMax)
##    legende = "n = " + str(nMax)
##    plt.plot(t, y, label = legende)
##    plt.plot(t, np.exp(t), label= "exp")
##    plt.legend(loc = "best")
##    plt.show()
##
#### 4

def heun(F, borne_a, borne_b, y_0, n):
    t_array = [a]
    y_array = [y_0]
    stepSize = (borne_b-borne_a)/n

    for index in range(0,n):
        currentY = y_array[index]
        p1 = F(t_array[index], currentY)
        p2 = F(t_array[index] + stepSize, currentY + stepSize * p1)
        nextY = currentY + stepSize*((p1+p2)/2)

        y_array.append(nextY)
        t_array.append(borne_a + stepSize * (index+1))

    return (t_array, y_array)

def rk4(F, borne_a, borne_b, y_0, n):
    t_array = [a]
    y_array = [y_0]
    stepSize = (borne_b-borne_a)/n

    for index in range(0,n):
        currentY = y_array[index]
        p1 = F(t_array[index], currentY)
        p2 = F(t_array[index] + stepSize/2, currentY + stepSize * p1 * 0.5)
        p3 = F(t_array[index] + stepSize/2, currentY + stepSize * p2 * 0.5)
        p4 = F(t_array[index] + stepSize, currentY + stepSize*p3)
        nextY = currentY + stepSize*((p1+2*p2+2*p3+p4)/6)

        y_array.append(nextY)
        t_array.append(borne_a + stepSize * (index+1))

    return (t_array, y_array)
#### 5
##def F(t,y):
##    return ...
##


##a, b, y_0 = 0,1,1
##nMax = 10
####
##t,y = euler(F,a,b,y_0,nMax)
##plt.plot(t,y,label = "Euler, n=10")
####
##t,y  = heun(F,a,b,y_0,nMax)
##plt.plot(t,y ,label="Heun, n=10")
####
##t,y  = rk4(F,a,b,y_0,nMax)
##plt.plot(t,y,label="RK4, n=10")
####
##plt.plot(t, np.exp(t), label="exp")
####
##plt.legend(loc = "best")
##plt.show()
##
##
#### 8

def f2(t,x,y):
    return x,y,t

def euler2(f,a,b,y_0,n):


##
#### 9
##a, b= ...
##alpha, beta = ...
##delta, gamma = ...
##n = ...
##fig, (ax1, ax2) = plt.subplots(2)
##x0 = ...
##y0 = ...
##t, x, y =  lotkaVolterra(...)
##ax1.plot(...)
##ax2.plot(...)
##ax1.set_ylabel("proies")
##ax2.set_ylabel("prédateurs")
##plt.show()
##
#### 10
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
