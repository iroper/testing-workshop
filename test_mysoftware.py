from mysoftware import *

def test_square_integers():
    assert square(2) == 4
    assert square(0) == 0
    assert square(-1) == 1

def test_coulomb():
    assert coulomb(1) == 1
    

def test_coulomb_throws_error():
    try:
        coulomb(0.0)
    except ZeroDivisionError:
        raise Exception("Test failed")
    except TypeError:
        pass
