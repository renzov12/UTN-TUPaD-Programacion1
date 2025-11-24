# Ejercicio 1
# Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.


#FUNCION

def imprimir_hola_mundo():
    return print("Hola Mundo!")

#PROGRAMA PRINCIPAL

imprimir_hola_mundo()


# Ejercicio 2
# Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.


#FUNCION


def saludar_usuario(nombre):
    return "Hola " + nombre +"!"


#FUNCION PRINCIPAL

nombre_ingresado = input("Ingrese su nombre ")
saludo = saludar_usuario(nombre_ingresado)

print(saludo)

# Ejercicio 3
# Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

#FUNCION 

def informacion_personal(nombre , apellido , edad , residencia):
     return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."

#PROGRAMA PRINCIPAL

nombre_ingresado = input("Ingrese su Nombre ")
apellido_ingresado = input("Ingrese su Apellido ")
edad_ingresado = input("Ingrese su Edad ")
residencia_ingresado = input("Ingrese su Residencia ")

presentacion = informacion_personal(nombre_ingresado , apellido_ingresado , edad_ingresado , residencia_ingresado)

print(presentacion)


# Ejercicio 4
# Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
# dio como parámetro y devuelva el área del círculo. calcular_peri
# metro_circulo(radio) que reciba el radio como parámetro y devuel
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am
# bas funciones para mostrar los resultados.


# FUNCIONES
def calcular_area_circulo(radio):
    return 3.14 * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * 3.14 * radio


#PROGRAMA 

radio = float(input("Ingrese el radio del circulo "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio )


print("El área del círculo es: ", area)
print("El perímetro del círculo es: ", perimetro)


# Ejercicio 5
# Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mos
# trar el resultado usando esta función.
#FUNCIONES

def segundo_a_horas(segundos):
    horas = segundos/3600

    return horas     




#PROGRAMA 

segundos_ingresados = int(input("Ingrese la cantidad de SEGUNDOS "))

ressultado = segundo_a_horas(segundos_ingresados)

print(f"{segundos_ingresados}) segundos equivalentes a {ressultado} horas")



# Ejercicio 6
# Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la fun
# ción.

#FUNCION

def tabla_multiplicar(numero):

    for i in range(1 , 11):
        print(f"{numero} X {i} = {numero*i}")


#PROGRAMA

num = int(input("Ingrese un numero para hacer su tabla "))

tabla_multiplicar(num)


# Ejercicio 7
# Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resulta
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
# sultados de forma clara.
#FUNCION

def operacion_basicas(a , b):

    suma= a+b
    resta = a-b
    multiplicacion = a*b
    division = a/b

    return(suma , resta , multiplicacion , division)

#PROGRAMA 

num1 = float(input("Ingrese el primer valor"))
num2 = float(input("Ingrese el segundo valor"))

resultado = operacion_basicas(num1 , num2)

print(f"Suma: {resultado[0]}")
print(f"Resta: {resultado[1]}")
print(f"Multiplicacion: {resultado[2]}")
print(f"Division: {resultado[3]}")

# Ejercicio 8
# Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
# ción para mostrar el resultado con dos decimales.

# FUNCION
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# PROGRAMA PRINCIPAL
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)

print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

# Ejercicio 9
# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

# FUNCION
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# PROGRAMA PRINCIPAL
celsius = float(input("Ingrese la temperatura en Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

# Ejercicio 10
# Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

# FUNCION
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

# PROGRAMA PRINCIPAL
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(num1, num2, num3)

print(f"El promedio de los tres números es: {promedio:.2f}")