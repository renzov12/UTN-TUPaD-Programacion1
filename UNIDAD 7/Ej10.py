# Diccionario original
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}

original = {1,4,5}

# Invertir: capital a país
invertido = {capital: pais for pais, capital in original.items()}

# Mostrar resultados
print("Diccionario original:", original)
print("Diccionario invertido:", invertido)