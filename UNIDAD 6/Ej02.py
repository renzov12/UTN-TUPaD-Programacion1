#FUNCION


def saludar_usuario(nombre):
    return "Hola " + nombre +"!"


#FUNCION PRINCIPAL

nombre_ingresado = input("Ingrese su nombre ")
saludo = saludar_usuario(nombre_ingresado)

print(saludo)