from funciones import *
from ejercicio_5.habitacion import Habitacion
from ejercicio_5.vivienda import Vivienda
from ejercicio_5.barrio import Barrio

class Crear_barrio():
    def main(self):
        nombre_barrio = input("Ingrese el nombre del barrio: ")
        empresa_constructora_barrio = input(f"Ingrese el nombre de la empresa constructora del barrio {nombre_barrio}: ")

        print(f"\n-----------------{nombre_barrio}-----------------")

        list_viviendas = []
        seguir_viviendas = True
        while seguir_viviendas:
            try:
                print(f"\n-------Nueva Casa-------")
                calle_vivienda = input("Ingrese la calle de la vivienda: ")
                numero_vivienda = pedir_int_rango("Ingrese el numero de calle la vivienda: ", 1)
                manzana_vivienda = input("Ingrese la manzana de la vivienda: ")
                nro_casa_vivienda = pedir_int_rango("Ingrese el numero de casa de la vivienda: ", 1)
                superficie_terreno_vivienda = pedir_float_rango("Ingrese la superficie del terreno de la vivienda: ", 0)

                seguir_habitaciones = True
                list_habitaciones = []
                while seguir_habitaciones:
                    print(f"\n-------Nueva Habitacion-------")
                    nombre_habitacion = input("Ingrese el nombre de la habitacion: ")
                    metros_cuadrados_habitacion = pedir_float_rango(f"Ingrese los metros cuadrados de la habitacion {nombre_habitacion}: ", 0)
                    list_habitaciones.append(Habitacion(nombre_habitacion, metros_cuadrados_habitacion))

                    otra_habitacion = input("¿Desea cargar otra habitacion a la vivienda? [S/N]: ").upper()
                    while otra_habitacion not in ["S", "N"]:
                        print("ERROR: Ingrese S o N")
                        otra_habitacion = input("¿Desea cargar otra habitacion a la vivienda? [S/N]: ").upper()
                    if otra_habitacion == "N": seguir_habitaciones = False

                vivienda = Vivienda(calle_vivienda, numero_vivienda, manzana_vivienda, nro_casa_vivienda, superficie_terreno_vivienda, list_habitaciones)
                vivienda.get_metros_cuadrados_cubiertos() #para verificar que no tenga mas metros cubiertos que de terreno
                list_viviendas.append(vivienda)

            except (ValueError, TypeError) as error:
                print(error)
                print("No se puedo añadir la vivienda. Intentalo de nuevo")

            otra_vivienda = input("¿Desea cargar otra vivienda al barrio? [S/N]: ").upper()
            while otra_vivienda not in ["S", "N"]:
                print("ERROR: Ingrese S o N")
                otra_vivienda = input("¿Desea cargar otra vivienda al barrio? [S/N]: ").upper()
            if otra_vivienda == "N": seguir_viviendas = False

        barrio = Barrio(nombre_barrio, empresa_constructora_barrio, list_viviendas)
        
        #ejecucion de metodos
        print(f"\n-------Terreno del Barrio-------")
        print(f"El barrio {barrio.nombre} tiene {barrio.get_superficie_total_terreno()} metros de terreno.")

        print(f"\n-------Terreno por Manzana-------")
        manzana_buscar = input("Ingrese la manzana de la cual desea saber cuantos metros tiene: ")
        metros_manzana = barrio.get_superficie_total_terreno_x_manzana(manzana_buscar)
        if metros_manzana: print(f"La manzana {manzana_buscar} tiene {metros_manzana} metros.")
        else: print(f"La manzana {manzana_buscar} no existe en el barrio {barrio.nombre}")

        print(f"\n-------Terreno Cubierto por Vivienda-------")
        for vivienda in barrio.viviendas:
            print(f"Manzana: {vivienda.manzana} | Casa: {vivienda.nro_casa} -> {vivienda.get_metros_cuadrados_cubiertos()} m2 cubiertos")

        print(f"\n-------Terreno Cubierto del Barrio-------")
        print(f"El barrio {barrio.nombre} tiene cubiertos {barrio.get_superficie_total_cubierta()} m2")