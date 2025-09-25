frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)

recuento = {}

for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("Lista con palabras únicas:", palabras_unicas)
print("Palabras repetidas:", recuento)
