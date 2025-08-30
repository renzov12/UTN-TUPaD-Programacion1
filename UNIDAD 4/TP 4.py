#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(0 , 100):
    print("numero" , i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

num = input("Ingrese un numero: ")

print (len(num))



#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))


if a > b:
    a, b = b, a  

suma = 0


for i in range(a + 1, b):
    suma += i

print("La suma de los números entre", a, "y", b, "es:", suma)


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.



suma = 0

print("Ingrese números enteros para sumarlos (0 para terminar):")


while True:
    numero = int(input("Número: "))
    if numero == 0:
        break
    suma += numero

print("La suma total es:", suma)


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.


import random
secreto = random.randint(0 ,9)

intento = 0
correcto = False

print("Advina el numero entre el 0 y el 9 ")
while not correcto:

    numero = int(input ("Ingrese tu numero "))
    intento += 1

    if numero == secreto:
        correcto = True

        print("Correcto , usted adivino el numero!! ")

    else:

        print("No es correcto  , vuelve a intentarlo ")

print("Usted lo logro en {intento} intentos" )


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente. 


for i in range(100 , 0 , -1):
  if i % 2 == 0:  
    print("numero" ,i )


#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario.     


n = int(input("Ingrese un número entero positivo: "))

suma = 0

for i in range(1, n):   
    suma += i

print("La suma de los números entre 0 y", n, "es:", suma)



#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio). 



pares=0
impares=0
negativo=0
positivos=0

cantidad = 100

for i in range(cantidad):

    numero = int(input(f"Ingrese el numero {i+1}: "))


    if numero % 2==0:
        pares += 1


    else:
        impares += 1

    if numero > 0:
        
        positivos += 1

    elif numero < 0:
        negativo += 1

print("Cantidad de numeros pares" ,pares)
print("Cantidad de numeros inpares" ,impares)
print("Cantidad de numeros positivos" ,positivos)
print("Cantidad de numeros negativos" ,negativo)



#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor). 



suma = 0


cantidad = 100   

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i+1}: "))
    suma += numero

media = suma / cantidad

print("La media de los números ingresados es:", media)


#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.


numero = input("Ingrese un número: ")

# Invertir la cadena
invertido = numero[::-1]

print("Número invertido:", invertido)