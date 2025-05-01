def factorial(n):
    if n < 0:
        return "Número inválido"
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

numero = int(input("Ingrese un número entero positivo: "))
print("El factorial es:", factorial(numero))
