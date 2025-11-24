from funciones import *
from ejercicio_2.cargar_notas import Carga_notas
from ejercicio_3.menu_restaurant import Menu_restaurant
from ejercicio_4.costo_computadora import Costo_computadora
from ejercicio_5.crear_barrio import Crear_barrio

def ejercicio_1():
    class Celda():
        def __init__(self):
            self._fila = None
            self._columna = None
            self._valor = None
        
        @property
        def fila(self):
            return self._fila
        
        @fila.setter
        def fila(self, fila):
            if not isinstance(fila, int): raise TypeError("ERROR: El valor de fila debe ser un int")
            if fila <= 0: raise ValueError("ERROR: El valor de fila no puede ser menor a 1")
            self._fila = fila

        @property
        def columna(self):
            return self._columna
        
        @columna.setter
        def columna(self, columna):
            if not isinstance(columna, int): raise TypeError("ERROR: El valor de columna debe ser un int")
            if columna <= 0: raise ValueError("ERROR: El valor de columna no puede ser menor a 1")
            self._columna = columna

        @property
        def valor(self):
            return self._valor

        @valor.setter
        def valor(self, valor):
            if not isinstance(valor, str): raise TypeError("ERROR: El valor de la celda debe ser un str")
            if valor == "": raise ValueError("ERROR: El valor de la celda no puede ser una cadena vacia")
            self._valor = valor

    class Matriz():
        def __init__(self):
            self._celdas_matriz = []

        @property
        def celdas_matriz(self):
            return list(self._celdas_matriz) #paso copia para protegerlo
        
        def agregar_celda(self, nueva_celda):
            if not isinstance(nueva_celda, Celda): raise TypeError("ERROR: El tipo de dato a agregar debe ser una celda")
            
            for celdas in self.celdas_matriz:
                if celdas.columna == nueva_celda.columna and celdas.fila == nueva_celda.fila: raise ValueError(f"ERROR: Esa celda ya esta ocupada por el valor \"{celdas.valor}\"")

            self._celdas_matriz.append(nueva_celda)

        def mostrar_celdas(self):
            if self.celdas_matriz:
                for celda in self.celdas_matriz:
                    print (f"{celda.fila},{celda.columna} -> {celda.valor}")
            else: print("No cargó ninguna celda")

        def valor_celda(self, fila, columna):
            for celda in self.celdas_matriz:
                if [celda.fila, celda.columna] == [fila, columna]:
                    print(f"{fila},{columna} -> {celda.valor}")
                    return
            print("La fila y columna indicada no han sido asignadas en ninguna celda")

    #main
    matriz = Matriz()
    seguir = True

    #Relleno de matriz
    while seguir:
        valor_celda = input("Ingrese un valor para la celda nueva o FIN para finalizar ejecucion: ")

        if valor_celda == "FIN": 
            seguir = False
            continue

        fila_celda = pedir_int_rango("Ingrese en que fila desea añadir la celda: ", 1)
        columna_celda = pedir_int_rango("Ingrese en que columna desea añadir la celda: ", 1)

        try:
            celda = Celda()
            celda.columna = columna_celda
            celda.fila = fila_celda
            celda.valor = valor_celda

            matriz.agregar_celda(celda)
            print("Celda agregada correctammente")

        except(ValueError, TypeError) as error:
            print(error)
            print("No se puedo agregar la celda, intentalo nuevamente")

    #mostrar matriz
    print("---------Celdas Cargadas---------")
    matriz.mostrar_celdas()

    #buscar valores por coordenadas
    seguir = True
    while seguir:
        eleccion = input("¿Desea buscar algun valor por su coordenada? [S/N]: ").upper()
        while eleccion not in ["S", "N"]:
            print("ERROR: Ingrese S o N")
            eleccion = input("¿Desea buscar algun valor por su coordenada? [S/N]: ").upper()
        if eleccion == "S":
            fila_buscada = pedir_int_rango("Ingrese la fila del valor a buscar: ", 1)
            columna_buscada = pedir_int_rango("Ingrese la columna del valor a buscar: ", 1)
            matriz.valor_celda(fila_buscada, columna_buscada)
        else: seguir = False
        
def ejercicio_2():
    cargador = Carga_notas()
    cargador.main()

def ejercicio_3():
    ejecutador = Menu_restaurant()
    ejecutador.main()

def ejercicio_4():
    ejecutador = Costo_computadora()
    ejecutador.main()

def ejercicio_5():
    ejecutador = Crear_barrio()
    ejecutador.main()

def menu_ejercicios(funciones):
    """Ejecuta menu para seleccionar ejercicios\n
    Recibe list con las funciones de cada ejercicio empezada por None
    """
    seguir = True
    while seguir:
        ejercicio_elegido = pedir_int_rango(f"Ingrese el numero de ejercicio que desea ejecutar (1-{len(funciones)-1}) [0] para terminar ", 0, len(funciones)-1)
        if ejercicio_elegido == 0: 
            seguir = False
            continue
        else: 
            print(f"\n -----EJERCICIO {ejercicio_elegido}-----")
            funciones[ejercicio_elegido]()
            print() #salto de linea
            input("Presione ENTER para volver") #para no sobrecargar consola
    
#main
ejercicios = [None, ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_4, ejercicio_5]
menu_ejercicios(ejercicios)
