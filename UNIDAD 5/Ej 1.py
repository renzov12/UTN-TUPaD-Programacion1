
#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función 
#range. 

lista1 = list(range(1,101))

multiplosde4 = [n for n in lista1 if n % 4 == 0]

print(multiplosde4)