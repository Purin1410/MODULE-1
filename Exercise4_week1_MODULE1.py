import math

def factorial(k):
    if k == 0 or k == 1:
        return 1
    else:
        return k * factorial(k - 1)

def approx_sin(x, n):
    result = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
        result += term
    return result

def approx_cos(x, n):
    result = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
        result += term
    return result

def approx_sinh(x, n):
    result = 0
    for i in range(n):
        term = (x ** (2 * i + 1)) / factorial(2 * i + 1)
        result += term
    return result

def approx_cosh(x, n):
    result = 0
    for i in range(n):
        term = (x ** (2 * i)) / factorial(2 * i)
        result += term
    return result

