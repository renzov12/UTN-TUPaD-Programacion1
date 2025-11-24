from funciones import *
from ejercicio_4.computadora import Computadora
from ejercicio_4.componente_cpu import Componente_cpu

class Costo_computadora():
    def main(self):
        seguir_computadora = True
        while seguir_computadora:
            try:
                marca_computadora = input("Ingrese la marca de la computadora: ")
                modelo_computadora = input("Ingrese el modelo de la commputadora: ")

                seguir_componente = True
                list_componentes = []
                while seguir_componente:
                    nombre_componente = input("Ingrese el nombre del componente: ")
                    marca_componente = input("Ingrese la marca del componente: ")
                    cantidad_componente = pedir_int_rango(f"Ingrese la cantidad de {nombre_componente} de la computadora: ", 1)
                    precio_componente = pedir_float_rango(f"Ingrese el precio de cada {nombre_componente}: ", 0)

                    nuevo_componente = Componente_cpu(nombre_componente, marca_componente, cantidad_componente, precio_componente)
                    list_componentes.append(nuevo_componente)

                    otro_componente = input("¿Desea añadir otro componente? [S/N]: ").upper()
                    while otro_componente not in ["S", "N"]:
                        print("ERROR: Ingresa S o N")
                        otro_componente = input("¿Desea añadir otro componente? [S/N]: ").upper()
                    if otro_componente == "N": seguir_componente = False
                
                computadora_usuario = Computadora(marca_computadora, modelo_computadora, list_componentes)

                precio_computadora = 0 #acumulador
                print("-------------Computadora-------------")
                print(f"Marca: {computadora_usuario.marca}\nModelo: {computadora_usuario.modelo}\nComponentes:")
                print("Componente          Marca          Cantidad        Precio X Unidad          SubTotal")
                for componente in list_componentes:
                    print(componente.componente, end="")   
                    print(" " * (20 - len(componente.componente)), end="")     

                    print(componente.marca, end="")   
                    print(" " * (15 - len(componente.marca)), end="") 

                    print(componente.cantidad, end="")   
                    print(" " * (16 - len(str(componente.cantidad))), end="")

                    print(componente.precio, end="")   
                    print(" " * (25 - len(str(componente.precio))), end="")      

                    subtotal = componente.precio * componente.cantidad
                    precio_computadora += subtotal

                    print(subtotal)         

                print(" " * 51, end="")
                print("Costo Total", end="")
                print(" " * 14, end="")
                print(precio_computadora)

                if precio_computadora >= 50000: recargo = 1.3 
                else: recargo = 1.4
                precio_sugerido = precio_computadora * recargo

                print(f"El precio sugerido de venta es {precio_computadora} + {precio_sugerido - precio_computadora} = {precio_sugerido}")
            except (ValueError, TypeError) as error:
                print(error)
                print("No se puedo cotizar la computadora. Intentalo de nuevo")


            otra_computadora = input("¿Desea cotizar otra computadora? [SI o NO]: ").upper()
            while otra_computadora not in ["SI", "NO"]:
                print("ERROR: Ingresa SI o NO")
                otra_computadora = input("¿Desea cotizar otra computadora? [SI o NO]: ").upper()
            if otra_computadora == "NO": seguir_computadora = False