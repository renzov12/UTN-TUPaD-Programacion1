from random import randint
while True:

    nombre = input("HOLA,INGRESE SU  NOMBRE: ").upper()

    print(f"BIENVENIDO {nombre} , al JUEGO DE ADIVINAR EL NUMERO!! ")

    NumeroAleatorio = randint(0 , 100)





    for intento in range(1,10):

        numero = int(input(f"Intento {intento}/10 - Ingrese un número: "))

        if numero > NumeroAleatorio:
            print("EL NUMERO ES MUY ALTO")
        elif numero < NumeroAleatorio:
            print ("EL NUMERO ES MUY BAJO")

        else:
        
            print(f"USTED ADIVINO EL NUMERO,{NumeroAleatorio}!")
            print(f"AL INTENTO {intento}")
            break

    else:
        print("SE ACABO LOS 10 INTENTOS ")
        print(" Reiniciando el juego...")


    print("\n--------------------------------------\n")