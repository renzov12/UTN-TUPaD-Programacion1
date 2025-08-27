#1)-Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. 
print("Hola Mundo!") 


#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
#realizar la impresión por pantalla.

nombre =input("Hola! , como te llamas?")
print(f"Hola {nombre}!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
#la impresión por pantalla. 

nombre=input("¿Como te llamas? ")
apellido=input("cual es tu apellido? ")
edad=input("Cuantos años tenes? ")
nacionalidad = input("De donde sos? ")

bienvenida = (f"Soy {nombre} {apellido} , tengo {edad} años y vivo en {nacionalidad}")
print(bienvenida)

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
#su perímetro. 

radio = float (input("Ingrese el radio del circulo "))
area = 3.14 * ( radio**2) 
circunferencia = 2 * 3.14 * radio
print("EL area es",area )
print(f"La circunferencia  es {circunferencia}" )

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
#cuántas horas equivale.

seg = float(input("Ingrese una cantidad de segundos: "))
hs = seg / 3600  
print(f"{hs} Hs")


#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
#multiplicar de dicho número. 

num = int(input("Ingrese el número para ver su tabla de multiplicar: "))


r1 = num * 1
r2 = num * 2
r3 = num * 3
r4 = num * 4
r5 = num * 5
r6 = num * 6
r7 = num * 7
r8 = num * 8
r9 = num * 9
r10 = num * 10


print(f"{num} x 1 = {r1}")
print(f"{num} x 2 = {r2}")
print(f"{num} x 3 = {r3}")
print(f"{num} x 4 = {r4}")
print(f"{num} x 5 = {r5}")
print(f"{num} x 6 = {r6}")
print(f"{num} x 7 = {r7}")
print(f"{num} x 8 = {r8}")
print(f"{num} x 9 = {r9}")
print(f"{num} x 10 = {r10}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Ingrese el primer numero distito a 0:"))
num2 = int(input("Ingrese el segundo numero distito a 0:"))

print("Suma:", num1+num2)
print("Resta:", num1-num2)
print("Multiplicacion:", num1*num2)
print("Division:", num1//num2)

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente 
#modo:                  

altura = float(input("Ingrese la altura"))
peso = float(input("Ingrese el peso"))

imc = peso//altura
print("su indice de masa corpal es de",imc)


#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 


celsius = float(input("Ingrese la temperatura en grados Celsius:"))

Fahrenheit = (9/5) * celsius + 32

print("La temperatura en Fahrenheit es:" , Fahrenheit)

#10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
#dichos números. 

num1 = float (input("Ingrese un numero "))
num2 = float (input("Ingrese un numero "))
num3 = float (input("Ingrese un numero "))

Promedio = (num1 + num2 + num3)/3
print("El promedio de los 3 numeros es de " , Promedio)