import numpy as np

def midpoint(f, a, b, eps, n=1, I=0):
    h = (b - a) / n
    s = 0
    for i in range(n):
        xi = a + h / 2 + i * h
        s += f(xi)
    I_new = h * s
    if abs(I_new - I) < eps:
        return I_new
    else:
        return midpoint(f, a, b, eps, n * 2, I_new)

def f(x):
    return (2 - x) * np.cos(x ** 2)

def F(x):
    a = 0
    b = 0.4
    e = 0.001
    k = midpoint(f, a, b, e)
    return  k*((2 * (x ** 2)) + (3 * np.exp(-x)))

def find_min(c, d, e):
    while abs(d - c) > e:
        mid = (c + d) / 2
        if F(mid - e) < F(mid + e):
            d = mid
        else:
            c = mid
    return (c + d) / 2


a = 0
b = 0.4
c = 0
d = 1
e = 0.001

min_x = find_min(c, d, e)
print("Аргумент минимального значения функции: ")
print(min_x)
print("Минимальное значение функции: ")
print(F(min_x))
xarr = np.arange(a, b, e)
y = f(xarr)


