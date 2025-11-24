def binario(n):
    if n == 0:
        return ""
    else:
        cociente = n // 2 
        resto = n % 2 
        return binario(cociente) + str(resto)

#main 
entero = int(input("Ingrese un numero entero "))
resultado = binario(entero)
print(resultado)