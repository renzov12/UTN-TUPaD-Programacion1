def contar_bloques(n):
    if n == 1:
        return 1

    else:
        return n + contar_bloques(n-1)
        


#main

bloques = int(input("Ingrese la cantidad de bloques que desea poner en el primer nivel: "))
resultado = contar_bloques(bloques)
print(resultado)