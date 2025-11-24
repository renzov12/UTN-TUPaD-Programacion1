def letras_sin_repetir(palabra):
    letras = set(palabra)
    ordenadas = sorted(letras)
    return ordenadas


#main 

palabra = input("Ingrese la palabra deseada: ")

print(letras_sin_repetir(palabra))