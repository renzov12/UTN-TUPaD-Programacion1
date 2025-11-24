
#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad"))
if edad >= 18:
    print("Eres mayor de edad")


    #2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
#mensaje “Desaprobado”. 


nota = int(input("Ingrese su nota"))

if nota >= 6:
    print("APROBADO")
else:
    print("DESAPROBADO")


    #3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
#operador de módulo (%) en Python para evaluar si un número es par o impar.


numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
#siguientes categorías pertenece: 
#● Niño/a: menor de 12 años. 
#● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Eres un Niño")
elif 12 <= edad < 18:
    print("Eres un Adolescente")
elif 18 <= edad < 30:
    print("Eres un Joven")
else:
    print("Eres un Adulto")




#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
#como una lista o un string. 

contraseña = input("Ingrese su cntraseña: ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")

else:
    print("Por favor , ingrese una contraseña de entre 8 y 14 caracteres")


#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números 
#y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el 
#siguiente:     


import random
from statistics import mode, median, mean

# Generar 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular media, mediana y moda
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Lista de números:", numeros_aleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

# Determinar el sesgo
if media > mediana > moda:
    print("La distribución tiene SESGO POSITIVO (a la derecha)")
elif media < mediana < moda:
    print("La distribución tiene SESGO NEGATIVO (a la izquierda)")
elif media == mediana == moda:
    print("La distribución NO tiene sesgo (simétrica)")
else:
    print("No cumple exactamente con las condiciones de sesgo")



#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
#pantalla. 


texto = input("Ingrese una frase o palabra: ")

if texto[-1].lower() in "aeiou" :
    texto += "!"
    print(texto)

else:

    print(texto)


    #8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# Pedimos al usuario que ingrese su nombre
nombre = input("Ingresa tu nombre: ")

# Mostramos las opciones
print("Elige una opción:")
print("1. Nombre en mayúsculas")
print("2. Nombre en minúsculas")
print("3. Nombre con la primera letra en mayúscula")

# Pedimos la opción
opcion = input("Ingresa 1, 2 o 3: ")

# Transformamos el nombre según la opción elegida
if opcion == "1":
    resultado = nombre.upper()
elif opcion == "2":
    resultado = nombre.lower()
elif opcion == "3":
    resultado = nombre.title()
else:
    resultado = "Opción no válida"

# Mostramos el resultado
print("Resultado:", resultado)


#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
#por pantalla: 
#● Menor que 3: "Muy leve" (imperceptible). 
#● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
#generalmente no causa daños). 
#● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
#débiles). 
#● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).


# Pedimos al usuario la magnitud del terremoto
magnitud = float(input("Ingresa la magnitud del terremoto: "))


if magnitud < 3:
    categoria = "Muy leve (imperceptible)"
elif 3 <= magnitud < 4:
    categoria = "Leve (ligeramente perceptible)"
elif 4 <= magnitud < 5:
    categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif 5 <= magnitud < 6:
    categoria = "Fuerte (puede causar daños en estructuras débiles)"
elif 6 <= magnitud < 7:
    categoria = "Muy Fuerte (puede causar daños significativos)"
else:  # magnitud >= 7
    categoria = "Extremo (puede causar graves daños a gran escala)"


print("El terremoto es:", categoria)


#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año 
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
#si el usuario se encuentra en otoño, invierno, primavera o verano. 

# Pedimos los datos al usuario
hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("Ingresa el mes en número (1-12): "))
dia = int(input("Ingresa el día del mes: "))


def estacion(hemisferio, mes, dia):
    if hemisferio == "N":
        if (mes == 12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia <= 20):
            return "Invierno"
        elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
            return "Primavera"
        elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
            return "Verano"
        elif (mes == 9 and dia >= 21) or (mes in [10,11]) or (mes == 12 and dia <= 20):
            return "Otoño"
    elif hemisferio == "S":
        if (mes == 12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia <= 20):
            return "Verano"
        elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
            return "Otoño"
        elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
            return "Invierno"
        elif (mes == 9 and dia >= 21) or (mes in [10,11]) or (mes == 12 and dia <= 20):
            return "Primavera"
    else:
        return "Hemisferio inválido"

print("La estación en tu hemisferio es:", estacion(hemisferio, mes, dia))
