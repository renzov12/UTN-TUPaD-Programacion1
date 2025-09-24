
# FUNCIONES
def calcular_area_circulo(radio):
    return 3.14 * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * 3.14 * radio


#PROGRAMA 

radio = float(input("Ingrese el radio del circulo "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio )


print("El área del círculo es: ", area)
print("El perímetro del círculo es: ", perimetro)