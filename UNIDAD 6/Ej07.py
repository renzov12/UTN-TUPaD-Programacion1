#FUNCION

def operacion_basicas(a , b):

    suma= a+b
    resta = a-b
    multiplicacion = a*b
    division = a/b

    return(suma , resta , multiplicacion , division)

#PROGRAMA 

num1 = float(input("Ingrese el primer valor"))
num2 = float(input("Ingrese el segundo valor"))

resultado = operacion_basicas(num1 , num2)

print(f"Suma: {resultado[0]}")
print(f"Resta: {resultado[1]}")
print(f"Multiplicacion: {resultado[2]}")
print(f"Division: {resultado[3]}")


