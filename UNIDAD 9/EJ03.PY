def potencia(b , p):
    if p == 0:
        return 1 
    else:
        return b * potencia(b , p-1)
    
base = int(input("Ingrese Base "))
pote = int(input("Ingrese Potencia "))
resultado = potencia(base , pote)
print(resultado)


    
    