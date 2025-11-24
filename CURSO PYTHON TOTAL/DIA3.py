print("===ANALIZADOR DE TEXTO===\n")


texto = input("Ingrese el texto que desee analizar: ").lower()

letra1 = input("Ingrese la primer letra: ")
letra2 = input("Ingrese la segunda letra: ")
letra3 = input("Ingrese la tercer letra: ")



print("===RESULTADOS===\n")

#CANTIDAD DE VECES QUE APARECE LA LETRA
print("1)-Cantidad de veces que aparece las letras elegidas")

print(f"Primer Letra: {letra1} :  {texto.count(letra1)}" )
print(f"Primer Letra: {letra2} :  {texto.count(letra2)}" )
print(f"Primer Letra: {letra3} :  {texto.count(letra3)}" )


#CUANTAS PALABRAS HAY EN TOTAL

print("2)-Cantidad de palabras TOTALES ")

palabrastotales = texto.split()
print(f"La cantidad de palabras son:  {len(palabrastotales)}")


#PRIMERA Y ULTIMA PALABRA DEL TEXTO


print("3)-Ultima y Primer letra: ")

print(f"Primer letra {texto[0]}")
print(f"Segunda letra {texto[-1]}")



# 4. Palabras en orden inverso
palabras_inverso = palabrastotales[::-1]
print("4) Palabras en orden inverso:")
print("   " + " ".join(palabras_inverso) + "\n")

#aparece python en el texto?


print("APARECE PYTHON EN EL TEXTO? ")

if "python" in texto:
    print("SI APARECE ")
else:
    print("NO APARECE")

