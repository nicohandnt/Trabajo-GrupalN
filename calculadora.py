## Proyecto calculadora en Python
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
 if b == 0:
    return "Error: División por cero"
 return a / b
 
def calculadora():
    print("Calculadora simple")
    print("Operaciones disponibles: +, -, *, /")

    a = float(input("Ingresa el primer número: "))
    operacion = input("Ingresa la operación (+, -, *, /): ")
    b = float(input("Ingresa el segundo número: "))

    if operacion == '+':
        resultado = suma(a, b)
    elif operacion == '-':
        resultado = resta(a, b)
    elif operacion == '*':
        resultado = multiplicacion(a, b)
    elif operacion == '/':
        resultado = division(a, b)
    
    else:
        resultado = "Operación no válida"

    print("Resultado:", resultado)

calculadora()
