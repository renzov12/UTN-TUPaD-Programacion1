def calcular_factorial(n):
    if n == 0:
        return 1
    else:

        return n * calcular_factorial(n - 1)
numero = int(input("Ingrese el numero que desea saber el factorial "))
print(calcular_factorial(numero))
    