import matplotlib.pyplot as plt
import numpy as np


def function(x):
    return (3*x+4)/(2*x+7)

def rightRectangle(x, N):
    sum = float(0.0)
    for i in range(0,N-1):
        sum += function(x[i+1])*(x[i+1]-x[i])
    return sum

def leftRectangle(x, N):
    sum = float(0.0)
    for i in range(1,N):
        sum += function(x[i-1])*(x[i]-x[i-1])
    return sum

def centralRectangle(x, N):
    sum = float(0.0)
    for i in range(1,N):
        sum += ((3*((x[i] + x[i-1])/2)+4)/(2*((x[i] + x[i-1])/2)+7))*h
    return sum

def trapezoid(x, N):
    sum = float(0.0)
    for i in range(1, N):
        sum += (function(x[i])+function(x[i-1]))*(h/2)
    return sum

def simpson(x):
    sum = float(0.0)
    N = len(x)
    for i in range(1, N-1, 1):
        sum += 4*((function(x[i])+function(x[i-1]))/2)

    for i in range(1, N-1):
        sum += 2*function(x[i])
    sum += function(x[0])+function(x[N-1])
    sum *= h/6
    return sum




a = -2
b = 2
h = float(0.2)
y = []
xarr = np.arange(a, b+1, h)
N = len(xarr)
print(xarr)
#for i in range(N):
#    y.append(function(xarr))

# for i in range(N):
#     print(y[i])






print('Результаты:')
print('Метод левых треугольников:', leftRectangle(xarr, N))
print('Метод правых треугольников:', rightRectangle(xarr, N))
print('Метод средних прямоугольников:',  centralRectangle(xarr, N))
print('Метод трапеций:', trapezoid(xarr, N))
print('Метод Симпсона:', simpson(xarr))

plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.plot(xarr, function(xarr))
plt.show()