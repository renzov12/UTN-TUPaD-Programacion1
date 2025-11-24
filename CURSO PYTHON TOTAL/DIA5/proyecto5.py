import random


# FUNCIONES
def pedir_letra():
    letra = input("Decime una letra: ").lower()
    return letra


def validar_letra(letra):
    # Que sea UNA sola letra
    if len(letra) != 1:
        print("Tenés que poner UNA sola letra.")
        return False
    
    if not letra.isalpha():
        print("Solo se permiten letras.")
        return False
    
    return True


def chequear_letra(letra, palabra, progreso):
    # Actualiza el progreso si la letra está
    acierto = False
    for i in range(len(palabra)):
        if palabra[i] == letra:
            progreso[i] = letra
            acierto = True
    return acierto


def ver_si_gano(progreso):
    return "_" not in progreso




palabras = ["python", "tecla", "raton", "juego", "mesa"]
palabra = random.choice(palabras)

progreso = ["_"] * len(palabra)
vidas = 6

print("Ahorcado sencillo – 6 vidas")
print("La palabra tiene", len(palabra), "letras.\n")

while vidas > 0:
    print("Progreso:", " ".join(progreso))
    print("Vidas:", vidas)

    letra = pedir_letra()

    if not validar_letra(letra):
        continue

    if chequear_letra(letra, palabra, progreso):
        print("Bien! La letra está.\n")
    else:
        vidas -= 1
        print("Esa letra no está.\n")

    if ver_si_gano(progreso):
        print("\n¡Ganaste! La palabra era:", palabra)
        break

if vidas == 0:
    print("Perdiste. La palabra era:", palabra)
