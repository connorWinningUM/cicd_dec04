import math

# Basic operations: addition, subtraction, multiplication and division.

def add (a, b):
    return a+b

def sub (a, b):
    return a-b

def mul (a, b):
    return a*b  

def div (a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a/b

# Advance operations: log, square, sin, cos, square root, percentage. 

def log (a, base=10):
    return math.log(a, base)

def square (a):
    return a**2

def sin (a):
    return math.sin(a)

def cos (a):
    return math.cos(a)

def sqrt (a):
    if a < 0:
        raise ValueError("Cannot square root negative number")
    return math.sqrt(a)

def percentage (a, b):
    if b == 0:
        raise ValueError("Cannot calculate percentage with denominator of zero")
    return (a / b) * 100
