def contar_digito(n , d):
    if n == 0:
        return 0 
    else:
        ultimo = n % 10
        resto = n // 10 
        if ultimo == d:
            return 1+ contar_digito(resto , d)
        else:
            return contar_digito(resto , d)



#main

entero = int(input("Ingrese un valor entero: "))
digito = int(input("Ingrese un valor digito: "))
resultado = contar_digito(entero , digito)
print(resultado)