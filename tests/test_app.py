import pytest
import sys
from pathlib import Path
import math

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))
from app import add, sub, mul, div, log, square, sin, cos, sqrt, percentage

def test_add():
    assert add(5, 6) == 11
    assert add(0, 0) == 0
    assert add(-5, 5) == 0
    assert add(-3, -7) == -10
    assert add(2.5, 2.5) == 5.0
    
    with pytest.raises(TypeError):
        add("sdsadf", 1)
    with pytest.raises(TypeError):
        add(None, 1)

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
    
    # Test division by zero
    with pytest.raises(ValueError):
        div(5, 0)

def test_log():
    assert log(100, 10) == 2
    assert log(math.e, math.e) == 1
    
    # Test log of negative number
    with pytest.raises(ValueError):
        log(-10, 10)

def test_square():
    assert square(4) == 16
    assert square(-3) == 9
    assert square(2.5) == 6.25
    
    # Test invalid input
    with pytest.raises(TypeError):
        square("asasdf")

def test_sin():
    assert sin(math.pi/2) == 1
    assert sin(0) == 0
    assert math.isclose(sin(math.pi), 0.0, abs_tol=1e-10)

def test_cos():
    assert cos(0) == 1
    assert cos(math.pi) == -1
    assert math.isclose(cos(math.pi/2), 0.0, abs_tol=1e-10)

def test_square_root():
    assert sqrt(16) == 4
    assert sqrt(0) == 0
    
    # Test square root of negative number
    with pytest.raises(ValueError):
        sqrt(-1)

def test_percentage():
    assert percentage(50, 200) == 25.0
    assert percentage(23, 100) == 23.0
    
    # Test division by zero in percentage
    with pytest.raises(ValueError):
        percentage(10, 0)