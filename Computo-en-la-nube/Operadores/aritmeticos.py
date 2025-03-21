def sumar(a, b, c):
    return a + b + c

def restar(a, b, c):
    return a - b - c

def multiplicar(a, b, c):
    return a * b * c

def dividir(a, b, c):
    try:
        return a / b / c
    except ZeroDivisionError:
        return None