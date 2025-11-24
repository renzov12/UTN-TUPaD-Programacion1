#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función 
#range. 

lista1 = list(range(1,101))

multiplosde4 = [n for n in lista1 if n % 4 == 0]

print(multiplosde4)


# 2) Crear una lista con cinco elementos y mostrar el penúltimo
elementos = ["Python" , "Moto " , True , 123 , 1.1 ]

print("El penultimo elemento es: " , elementos[-2])


# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante
lista_vacia =[]

lista_vacia.append("hola")
lista_vacia.append("mundo")
lista_vacia.append("cruel")


print(lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista “animales” y mostrar la lista resultante
animales = ["perro" , "gato" , "conejo" , "pez"]
print("Lista original",animales)

animales[1] = "loro"
animales[3] = "oso"

print("Lista actualizada",animales)

# 5) Analizar el siguiente programa y explicar qué realiza
print("Utiliza el comando remove y max en una lista y estos hacen que el mayor numero se borre de la misma ")

# 6) Crear una lista con números del 10 al 30 (incluido), haciendo saltos de 5 en 5 y mostrar los dos primeros
lista = list(range(10 , 31 , 5))


print("Lista Completa " , lista)


print("Los dos primeros elementos son: " , lista[0] , lista[1])

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
autos = ["sedan" , "polo" , "suran" , "gol"]

print("Lista original: ",autos)


autos[1:3] = ["cronos" , "fiesta"]

print("Lista actualizada: ",autos)

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append; imprimir la lista
dobles = []

dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

print(dobles)


# 9) Dada la lista “compras”, realizar las siguientes modificaciones: agregar, reemplazar y eliminar elementos, luego imprimir la lista
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 


compras[2].append("jugo")
compras[1][1] =("tallarines")
compras[0].remove("pan")


print(compras)

# 10) Elaborar una lista anidada llamada “lista_anidada” con elementos específicos y mostrarla por pantalla

lista_anidada = [
    15,          
    [25.5, 57.9, 30.6],  
    False        
]

print(lista_anidada)