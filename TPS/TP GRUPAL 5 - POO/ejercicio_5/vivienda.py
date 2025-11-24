from ejercicio_5.habitacion import Habitacion

class Vivienda():
    def __init__(self, calle: str, numero: int, manzana: str, nro_casa: int, superficie_terreno: float, habitaciones: list):
        if not isinstance(calle, str):
            raise TypeError("ERROR: El tipo de dato de calle debe ser un str")
        self.calle = calle

        if not isinstance(numero, int):
            raise TypeError("ERROR: El tipo de dato de numero debe ser un int")
        if numero <= 0:
            raise ValueError(f"ERROR: El numero de la calle {self.calle} debe ser mayor a 0")
        self.numero = numero

        if not isinstance(manzana, str):
            raise TypeError("ERROR: El tipo de dato de manzana debe ser un str")
        self.manzana = manzana

        if not isinstance(nro_casa, int):
            raise TypeError("ERROR: El tipo de dato de nro_casa debe ser un int")
        if nro_casa <= 0:
            raise ValueError(f"ERROR: El numero de la casa debe ser mayor a 0")
        self.nro_casa = nro_casa

        if not isinstance(superficie_terreno, float):
            raise TypeError("ERROR: El tipo de dato de superficie_terreno debe ser un float")
        if superficie_terreno <= 0:
            raise ValueError(f"ERROR: La superficie del terreno debe ser mayor a 0")
        self.superficie_terreno = superficie_terreno

        if not isinstance(habitaciones, list):
            raise TypeError("ERROR: El tipo de dato habitaciones debe ser un list")
        for habitacion in habitaciones:
            if not isinstance(habitacion, Habitacion):
                raise TypeError(f"ERROR: Los habitaciones deben ser de tipo Habitacion")
        self.habitaciones = habitaciones

    def get_metros_cuadrados_cubiertos(self):
        total_metros = sum([habitacion.metros_cuadrados for habitacion in self.habitaciones])
        if total_metros > self.superficie_terreno:
            raise ValueError("ERROR: La superficie cubierta no puede ser mayor a la superficie del terreno")
        return total_metros