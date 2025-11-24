from funciones import *
from ejercicio_3.plato import Plato
from ejercicio_3.ingrediente import Ingrediente

class Menu_restaurant():
    def __init__(self):
        platos_menu = []
    
    def main(self):
        seguir_platos = True
        menu = []
        while seguir_platos:
            try:
                print("--------------------Cargar plato--------------------")
                nombre_plato = input("Ingrese el nombre del nuevo plato: ")
                precio_plato = pedir_float_rango(f"Ingrese el precio de {nombre_plato}: ", 0)

                es_bebida = input(f"¿{nombre_plato} es una bebida? [S/N]: ").upper()
                while es_bebida not in ["S", "N"]:
                    print("ERROR: Ingresa S o N")
                    es_bebida = input(f"¿{nombre_plato} es una bebida? [S/N]: ").upper()
                if es_bebida == "S": es_bebida = True
                else: es_bebida = False

                ingredientes_plato = []
                if not es_bebida:
                    print("--------------------Cargar ingredientes--------------------")
                    seguir_ingredientes = True
                    while seguir_ingredientes:
                        nombre_ingrediente = input("Ingrese el nombre del ingrediente: ")
                        cantidad_ingrediente = pedir_float_rango(f"Ingrese la cantidad de {nombre_ingrediente}: ", 0)
                        unidad_medida_ingrediente = input("Ingrese la unidad de medida de esa cantidad: ")

                        ingrediente_nuevo = Ingrediente(nombre_ingrediente, cantidad_ingrediente, unidad_medida_ingrediente)
                        ingredientes_plato.append(ingrediente_nuevo)

                        otro_ingrediente = input(f"¿Desea añadir otro ingrediente a {nombre_plato}? [S/N]: ").upper()
                        while otro_ingrediente not in ["S", "N"]:
                            print("ERROR: Ingresa S o N")
                            otro_ingrediente = input(f"¿Desea añadir otro ingrediente a {nombre_plato}? [S/N]: ").upper()
                        if otro_ingrediente == "N": seguir_ingredientes = False

                plato_nuevo = Plato(nombre_plato, precio_plato, es_bebida, ingredientes_plato)
                menu.append(plato_nuevo)

            except( ValueError, TypeError) as error:
                print(error)
                print("El plato no pudo ser cargado. Intentalo de nuevo")

            otro_plato = input("¿Desea añadir otro plato al menu? [S/N]: ").upper()
            while otro_plato not in ["S", "N"]:
                print("ERROR: Ingresa S o N")
                otro_plato = input("¿Desea añadir otro plato al menu? [S/N]: ").upper()

            if otro_plato == "N": seguir_platos = False

        print("-----------MENÚ----------------")
        for plato in menu:
            print(f"{plato.nombre_completo}\nPrecio: ${plato.precio}")

            if plato.ingredientes:
                print("Ingredientes:")
                print("Nombre               Cantidad               Unidad de medida")
                for ingrediente in plato.ingredientes:
                    print(ingrediente.nombre, end="")
                    print(" " * (21-len(ingrediente.nombre)), end="")

                    print(ingrediente.cantidad, end="")
                    print(" " * (23-len(str(ingrediente.cantidad))), end="")

                    print(ingrediente.unidad_de_medida)
                print("---------------------------")

