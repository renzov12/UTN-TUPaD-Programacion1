from ejercicio_2.notas import Nota
from ejercicio_2.alumno import Alumno
from funciones import *

class Carga_notas():
    def __init__(self):
        self._alumnos = []

    @property
    def alumnos(self):
        return list(self._alumnos) #paso copia para proteger
    
    def main(self):
        seguir_alumnos = True
        list_alumnos = []
        while seguir_alumnos:
            try:
                print("-----CARGAR ALUMNO-----")
                nombre_alumno = input("Ingrese el nombre completo del nuevo alumno: ")
                legajo_alumno = pedir_int_rango(f"Ingrese el legajo de {nombre_alumno}: ", 10000, 99999)
                
                seguir_notas = True
                notas_alumno = []
                while seguir_notas:
                    print("-----CARGAR NOTA-----")
                    catedra_nota = input("Ingrese la catedra de la nueva nota: ")
                    nueva_nota = pedir_float_rango("Ingrese el valor de la nueva nota: ", 1, 10)
                    notas_alumno.append(Nota(catedra_nota, nueva_nota))

                    #preguntar si continua
                    eleccion = input(f"¿Desea seguir cargando notas para el alumno {nombre_alumno}? [S/N]: ").upper()
                    while eleccion not in ["S", "N"]:
                        print("ERROR: Ingrese S o N")
                        eleccion = input(f"¿Desea seguir cargando notas para el alumno {nombre_alumno}? [S/N]: ").upper()
                    if eleccion == "N": seguir_notas = False
                
                alumno_nuevo = Alumno(nombre_alumno, legajo_alumno, notas_alumno)
                list_alumnos.append(alumno_nuevo)

            except (ValueError, TypeError) as error:
                print(error)
                print("No se puedo cargar el alumno. Intentelo de nuevo")

            #preguntar si continua
            eleccion = input(f"¿Desea cargar otro alumno? [S/N]: ").upper()
            while eleccion not in ["S", "N"]:
                print("ERROR: Ingrese S o N")
                eleccion = input(f"¿Desea cargar otro alumno? [S/N]: ").upper()
            if eleccion == "N": seguir_alumnos = False
            
        for alumno in list_alumnos:
            print("") #separacion
            print(f"--------------{alumno.nombre_completo} {alumno.legajo}-----------------")
            for notas in alumno.notas:
                print(f"{notas.catedra} -> {notas.nota}")
            print(f"Promedio: {alumno.calcular_promedio()}")