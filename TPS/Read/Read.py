def pedir_int_rango(mensaje, limite_inf = float("inf"), limite_sup = float("inf")):
    """
    Pide un numero entero y valida que este dentro dentro del rango solicitado\n
    mensaje = mensaje a mostrar en input\n
    limite_inf = limite inferior del rango\n
    limite_sup = limite superior del rango\n
    retorna int
    """
    while True:
        n = input(mensaje)
        try: int(n)
        except: 
            print("ERROR: Ingresa un numero entero")
            continue
        n = int(n)
        if not limite_inf<=n<=limite_sup:
            print(f"ERROR: El numero ingresado no esta entre {limite_inf} y {limite_sup}")
            continue
        return n

def pedir_float_rango(mensaje, limite_inf = float("inf"), limite_sup = float("inf")):
    """Pide un numero flotante y valida que este dentro dentro del rango solicitado"""
    while True:
        n = input(mensaje)
        try: float(n)
        except: 
            print("ERROR: Ingresa un numero")
            continue
        n = float(n)
        if not limite_inf<=n<=limite_sup:
            print(f"ERROR: El numero ingresado no esta entre {limite_inf} y {limite_sup}")
            continue
        return n

def pedir_alpha(mensaje):
    string = "1,." #especifico para evitar que el usuario ingrese esa cadena
    while not string.isalpha():
        if string != "1,.": print("ERROR: Ingrese una cadena de solo letras")
        string = input(mensaje)
    return string

def leer_alumnos(txt):
    with open(txt,"r") as archivo:
        for linea in archivo:
            nombre,apellido,legajo,nota_promedio = linea.strip().split(";")
            print(f"{nombre} {apellido} | Legajo: {legajo} | Nota promedio: {nota_promedio}")

def agregar_alumno():
    #pedir datos
    nombre = pedir_alpha("Ingrese el nombre del nuevo alumno: ")
    apellido = pedir_alpha("Ingrese el apellido del nuevo alumno: ")
    legajo = pedir_int_rango("Ingrese el legajo del alumno nuevo: ", 10000, 99999)
    while validar_existe_alumno(legajo):
        print(f"El legajo {legajo} ya existe en el archivo alumnos.txt, no se permite su escritura. Intentelo de nuevo")
        legajo = pedir_int_rango("Ingrese el legajo del alumno nuevo: ", 10000, 99999)
    promedio = pedir_float_rango("Ingrese el promedio de notas del alumno nuevo: ", 1, 10)

    #añadir al archivo
    with open("alumnos.txt", "a") as archivo:
        archivo.write(f"{nombre};{apellido};{legajo};{promedio}\n")
    
    #añadir al dict
    alumnos_dict[legajo] = [nombre, apellido, promedio]

def validar_existe_alumno(legajo):
    return legajo in alumnos_dict.keys()

def guardar_aprobados():
    #crear archivo
    with open("Aprobados.txt", "w") as archivo:
        for legajo, (nombre, apellido, promedio) in alumnos_dict.items():
            if float(promedio) >= 6: archivo.write(f"{nombre};{apellido};{legajo};{promedio}\n")

    leer_alumnos("Aprobados.txt")

def menu():
    seguir = True
    texto_eleccion = "Ingrese una opcion\n[1]- Ver alumnos\n[2]- Agregar alumno\n[3]- Ver aprobados\n[4]- Salir\n"
    while seguir:
        eleccion = pedir_int_rango(texto_eleccion, 1, 4)
        if eleccion == 1: leer_alumnos("alumnos.txt")
        elif eleccion == 2: agregar_alumno()
        elif eleccion == 3: guardar_aprobados()
        else: seguir = False

#main
alumnos_dict = {}
with open("alumnos.txt", "r") as archivo:
    for linea in archivo:
        valores = linea.strip().split(";")
        alumnos_dict[valores[2]] = [valores[0], valores[1], valores[3]]

print(alumnos_dict)
guardar_aprobados()
menu()