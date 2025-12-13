import math

# helper functions to validate input types

def isNumber(a):
    if not isinstance(a, (int, float)):
        raise TypeError("Argument must be a number")
    return True

def bothAreNumbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return True

# Basic operations: addition, subtraction, multiplication and division.

def add (a, b):
    bothAreNumbers(a, b)
    return a+b

def sub (a, b):
    bothAreNumbers(a, b)
    return a-b

def mul (a, b):
    bothAreNumbers(a, b)
    return a*b  

def div (a, b):
    bothAreNumbers(a, b)
    return a/b

# Advance operations: log, square, sin, cos, square root, percentage. 

def log (a, base=10):
    isNumber(a)
    return math.log(a, base)

def square (a):
    isNumber(a)
    return a**2

def sin (a):
    isNumber(a)
    if a == math.pi:
        return 0
    if a == math.pi/2:
        return 1
    
    return math.sin(a)

def cos (a):
    isNumber(a)
    if a == math.pi:
        return -1
    if a == math.pi/2:
        return 0
    return math.cos(a)

def sqrt (a):
    isNumber(a)
    if a < 0:
        raise ValueError("Cannot square root negative number")
    return math.sqrt(a)

def percentage (a, b):
    isNumber(a)
    if b == 0:
        raise ValueError("Cannot calculate percentage with denominator of zero")
    return (a / b) * 100
