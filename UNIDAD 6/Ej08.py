# FUNCION
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# PROGRAMA PRINCIPAL
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)

print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")
