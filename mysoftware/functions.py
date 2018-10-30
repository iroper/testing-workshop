import numpy as np

def square(x):
    """
    Takes a number x and squares it.
    
    Parameters:
    -----------
    x, float or int:
        Number which is to be squared
    
    Returns:
    --------
    float:
        Square of x
    
    Examples:
    ---------
    
    >>> square(2)
    4
    
    >>> square(8)
    64
    
    >>> square(-1)
    1
    """
    return x*x

def coulomb(r):
    return 1/abs(r)

def CentralDifference(f, x, h):
    # f(x+h) - f(x-h)
    # --------------- approx f'(x)
    #       2*h
    return (f(x+h) - f(x-h))/(2.0*h)

for i in range(2,8):
    h = 10**(-i)
    print(h, abs(CentralDifference(np.sin, 0.0, h) - 1.0))
