import math

def add (a, b):
    return a+b

def sub (a, b):
    return a-b

def mul (a,b):
    return a*b

def div (a,b):
    if b == 0:
        raise ValueError("Can't divide by zero")
    return a/b
    
def log (a, base=math.e):
    if a <= 0:
        raise ValueError("Can't calculate log of non-positive number")
    if base <= 0 or base == 1:
        raise ValueError("Base must be positive and not equal to 1")
    return math.log(a, base)

def square (a):
    return a*a

def sqrt(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def percent(a,b):
    if b == 0:
        raise ValueError("Cannot calculate percentage with zero as the total")
    return (a / b) * 100