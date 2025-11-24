def suma_digitos(n):

    if n < 10:
        return n
    else : 
        return (n % 10 ) + suma_digitos(n // 10)
    

    #main

numero = int(input("Ingrese un numero para hacer la suma de sus numeros "))

resultado = suma_digitos(numero)
print(resultado)




