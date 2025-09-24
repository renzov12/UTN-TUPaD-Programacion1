# FUNCION
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

# PROGRAMA PRINCIPAL
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(num1, num2, num3)

print(f"El promedio de los tres números es: {promedio:.2f}")
