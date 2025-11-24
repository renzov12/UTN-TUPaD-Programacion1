def devolver_distintos(a , b ,c):
    
    suma = a+b+c

    if suma > 15: 
        return max(a,b,c)
    elif suma < 10:
        return min(a,b,c)
    else:
        lista = [a,b,c]
        lista.sort()
        return lista[1]
    
n1=int(input("Ingrese el primer numero: "))
n2=int(input("Ingrese el segundo numero: "))
n3=int(input("Ingrese el tercer numero: "))

print(devolver_distintos(n1 , n2, n3))
