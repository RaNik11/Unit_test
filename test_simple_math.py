import pytest
from simple_math import SimpleMath

@pytest.fixture
def Simple():
    return SimpleMath()

def test_square_positive(Simple):

    res = Simple.square(5)
    assert res == 25

def test_cube_positive(Simple):

    res = Simple.cube(3)
    assert res == 27


def test_square_negative(Simple):
    res = Simple.square(-4)
    assert res == 16


def test_cube_negative(Simple):
    res = Simple.cube(-10)
    assert res == -1000

@pytest.mark.skip(reason= "We already know the result")
def test_square_by_0(Simple):
    res = Simple.square(0)
    assert res == 0


def test_cube_by_0(Simple):
    res = Simple.cube(0)
    assert res == 0




