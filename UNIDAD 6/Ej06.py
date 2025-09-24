#FUNCION

def tabla_multiplicar(numero):

    for i in range(1 , 11):
        print(f"{numero} X {i} = {numero*i}")


#PROGRAMA

num = int(input("Ingrese un numero para hacer su tabla "))

tabla_multiplicar(num)