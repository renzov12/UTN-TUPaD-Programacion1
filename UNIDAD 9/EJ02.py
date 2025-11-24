def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
    




#----------------------------------#
numero = int(input("Ingrese un numero "))
fibo(numero)

for i in range(numero):
    print(fibo(i))
    
