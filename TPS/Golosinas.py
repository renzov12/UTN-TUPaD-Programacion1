# -------------------------------
# Funciones
# -------------------------------

def menu():
    seguir = True
    while seguir:
        eleccion_usuario = input(
            "Ingrese la opcion deseada\n[a]- Pedir golosina\n[b]- Mostrar golosinas\n[c]- Rellenar golosinas\n[d]- Apagar maquina\n"
        ).lower()
        
        while eleccion_usuario not in ["a", "b", "c", "d"]:
            print("ERROR: Ingresa una opcion valida")
            eleccion_usuario = input(
                "Ingrese la opcion deseada\n[a]- Pedir golosina\n[b]- Mostrar golosinas\n[c]- Rellenar golosinas\n[d]- Apagar maquina\n"
            ).lower()
        
        if eleccion_usuario == "a":
            PedirGolosinas(golosinas)         
        elif eleccion_usuario == "b":
            imprimir_tabla()
        elif eleccion_usuario == "c":
            Rellenar_Golosinas()
        elif eleccion_usuario == "d":
            mostrar_golosinas_pedidas()  # mostramos resumen antes de salir
            print("\nApagando la máquina. ¡Hasta luego!")
            seguir = False


# -------------------------------
# Pedir Golosinas
# -------------------------------
def PedirGolosinas(golosinas):
    legajo = int(input("Ingrese su legajo: "))
    
    if legajo in empleados:
        print("Ingreso correctamente")
        print("Lista de golosinas disponibles:")
        imprimir_tabla()
        
        continuar = True
        while continuar:
            legajo_de_golosina = pedir_legajo_de_golosina()
            encontrada = False

            for golosina in golosinas:
                if golosina[0] == legajo_de_golosina:
                    encontrada = True
                    if golosina[2] > 0:
                        golosina[2] -= 1
                        print(f"Golosina '{golosina[1]}' pedida correctamente. Stock restante: {golosina[2]}")

                        # -----------------------------
                        # Registramos la golosina pedida
                        # -----------------------------
                        encontrada_pedida = False
                        for gp in golosinasPedidas:
                            if gp[0] == golosina[0]:
                                gp[2] += 1  # sumamos cantidad pedida
                                encontrada_pedida = True
                                break
                        if not encontrada_pedida:
                            golosinasPedidas.append([golosina[0], golosina[1], 1])

                    else:
                        print(f"Lo sentimos, la golosina '{golosina[1]}' no se encuentra disponible.")
                    break

            if not encontrada:
                print("Golosina no encontrada. Intente nuevamente.")

            eleccion = input("¿Desea elegir otra golosina? (1-Sí / 2-No): ")
            if eleccion != "1":
                continuar = False
    else:
        print("Usted no es un empleado de la empresa")


# -------------------------------
#pedir legajo de golosina
# -------------------------------
def pedir_legajo_de_golosina():
    while True:
        try:
            legajo_de_golosina = int(input("Ingrese el legajo de la golosina: "))
            return legajo_de_golosina
        except ValueError:
            print("Debe ingresar un número válido.")


# -------------------------------
# Mostrar tabla de golosinas
# -------------------------------
def imprimir_tabla():
    print("\n--- Golosinas Disponibles ---")
    for g in golosinas:
        print(f"{g[0]} - {g[1]} (Stock: {g[2]})")


# -------------------------------
# Rellenar Golosinas
# -------------------------------
def Rellenar_Golosinas():
    # Validación de las 3 contraseñas
    clave1 = input("Ingrese la primera contraseña de administrador: ")
    clave2 = input("Ingrese la segunda contraseña de administrador: ")
    clave3 = input("Ingrese la tercera contraseña de administrador: ")

    if clave1 == clavesTecnico[0] and clave2 == clavesTecnico[1] and clave3 == str(clavesTecnico[2]):
        # Contraseña correcta: pedimos código de golosina
        legajo_golosina = pedir_legajo_de_golosina()
        encontrada = False

        for golosina in golosinas:
            if golosina[0] == legajo_golosina:
                encontrada = True
                # Pedimos cantidad a recargar
                cantidad_recarga = int(input("Ingrese la cantidad a recargar: "))
                if cantidad_recarga > 0:
                    golosina[2] += cantidad_recarga  # sumamos al stock actual
                    print(f"Se han recargado {cantidad_recarga} unidades de '{golosina[1]}'. Stock total: {golosina[2]}")
                else:
                    print("Cantidad inválida. Debe ser mayor a 0.")
                break

        if not encontrada:
            print("Código de golosina incorrecto.")
    else:
        print("No tiene permiso para ejecutar la función de recarga.")


# -------------------------------
# Mostrar Golosinas Pedidas
# -------------------------------
def mostrar_golosinas_pedidas():
    if not golosinasPedidas:
        print("No se han pedido golosinas.")
        return
    
    total_golosinas_pedidas = 0
    print("\n--- Golosinas Pedidas ---")
    for i in golosinasPedidas:
        print(f"Código golosina {i[0]}  Denominación Golosina {i[1]}  Cantidad total pedida {i[2]}")
        total_golosinas_pedidas += i[2]
    print(f"\nCantidad total de golosinas pedidas: {total_golosinas_pedidas}")


# -------------------------------
# Main
# -------------------------------

# Lista de golosinas
golosinas = [
    [1, "KiTKat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de menta", 50],
    [4, "Huevo kinder", 10],
    [5, "Chetos", 10],
    [6, "Twix", 10],
    [7, "M&M'S", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15],
    [11, "Lata Coca", 20],
    [12, "Chitos", 10]
]

# Diccionario de empleados
empleados = {
    1100: "Jose Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gastón Garcia"
}

# Claves del técnico
clavesTecnico = ("admin", "CCCDDD", 2020)

# Lista de golosinas pedidas
golosinasPedidas = []

# Ejecutamos menú
menu()