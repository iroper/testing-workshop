import numpy as np

def square(x):
    return x*x

def CentralDifference(f, x, h):
    # f(x+h) - f(x-h)
    # --------------- approx f'(x)
    #       2*h
    return (f(x+h) - f(x-h))/(2.0*h)

for i in range(2,8):
    h = 10**(-i)
    print(h, abs(CentralDifference(np.sin, 0.0, h) - 1.0))
