import pytest

from calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator()
def test_sum(calculator):
    res = calculator.sum(1, 4)
    assert res == 5

def test_sub(calculator):
    res = calculator.sub(7, 4)
    assert res == 3

def test_divide(calculator):
    res = calculator.div(6, 3)
    assert res == 2

def test_miltiplay(calculator):
    res = calculator.multiplay(1, 4)
    assert res == 4
