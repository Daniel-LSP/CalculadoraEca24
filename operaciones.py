def suma(a, b):
    """Suma dos números."""
    return a + b

def resta(a, b):
    """Resta el segundo número del primero."""
    return a - b

def multiplicacion(a, b):
    """Multiplica dos números."""
    return a * b

def division(a, b):
    """Divide el primer número por el segundo. Maneja división por cero."""
    if b == 0:
        return "Error: División por cero"
    return a / b

def modulo(a, b):
    """Calcula el residuo de la división entre dos números."""
    return a % b