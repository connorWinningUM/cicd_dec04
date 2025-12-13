import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


from app import add, sub, mul, div, log, square, sin, cos, sqrt, percentage
import math

addTestCases = [
    (5, 6, 11),
    (0, 0, 0),
    (-5, 5, 0),
    (-3, -7, -10),
    (2.5, 2.5, 5.0),
    ("sdsadf", 1, TypeError),
    (None, 1, TypeError),
]

def test_add():
    for a, b, expected in addTestCases:
        if isinstance(expected, type) and issubclass(expected, Exception):
            try:
                add(a, b)
            except Exception as e:
                assert isinstance(e, expected)
            else:
                assert False, f"Expected exception {expected} for inputs ({a}, {b})"
        else:
            result = add(a, b)
            assert result == expected, f"add({a}, {b}) = {result}, expected {expected}"

def test_sub():
    assert sub(10, 5) == 5
    assert sub(0, 0) == 0
    assert sub(-5, -5) == 0
    assert sub(2.5, 1.5) == 1.0

def test_mul():
    assert mul(3, 4) == 12
    assert mul(0, 100) == 0
    assert mul(-2, 3) == -6
    assert mul(2.5, 2) == 5.0

def test_div():
    assert div(10, 2) == 5
    assert div(-9, 3) == -3
    assert div(7.5, 2.5) == 3.0
    try:
        div(5, 0)
    except ZeroDivisionError:
        pass
    else:
        assert False, "Expected ZeroDivisionError for division by zero"

def test_log():
    import math
    assert log(100, 10) == 2
    assert log(math.e, math.e) == 1
    try:
        log(-10)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for log of negative number"

def test_square():
    assert square(4) == 16
    assert square(-3) == 9
    assert square(2.5) == 6.25

def test_sin():
    assert sin(math.pi/2) == 1
    assert sin(0) == 0
    assert sin(math.pi) == 0.0

def test_cos():
    assert cos(0) == 1
    assert cos(math.pi) == -1
    assert cos(math.pi/2) == 0.0

def test_square():
    assert sqrt(16) == 4
    assert sqrt(0) == 0
    try:
        sqrt(-4)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for square root of negative number"

def test_percentage():
    assert percentage(50, 200) == 25.0
    assert percentage(23, 100) == 23.0
    try:
        percentage(10, 0)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for percentage with denominator of zero"
