import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError
    return a / b

def power(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError
    return math.log(a, b)
