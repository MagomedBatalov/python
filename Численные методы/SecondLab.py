import numpy as np

def leftDerivative(y2, y1, h):
    diff = float(0.0)
    diff = (y2-y1)/h
    return diff

def rightDerivative(y3, y2, h):
    diff = float(0.0)
    diff = (y3-y2)/h
    return diff

def centralDerivative(y3, y1, h):
    diff = float(0.0)
    diff = (y3-y1)/(2*h)
    return diff

def secondDerivative(y3, y2, y1, h):
    diff = float(0.0)
    diff = (y3-2*y2+y1)/(h**2)
    return diff

y0 = float(0.0)
y1 = float(1.0)
y2 = float(1.4142)
y3 = float(1.7321)
y4 = float(2.0)
x0 = float(0.0)
x1 = float(1.0)
x2 = float(2.0)
x3 = float(3.0)
x4 = float(4.0)
xx = float(2.0)
h = xx - x1

print(leftDerivative(y2, y1, h))
print(rightDerivative(y3, y2, h))
print(centralDerivative(y3, y1, h))
print(secondDerivative(y3, y2, y1, h))