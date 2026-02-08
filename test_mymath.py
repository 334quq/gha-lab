import pytest
import mymath

def test_add():
    assert mymath.add(2, 3) == 5

def test_div():
    assert mymath.div(6, 3) == 2

def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        mymath.div(1, 0)