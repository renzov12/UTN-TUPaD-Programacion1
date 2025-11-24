class Habitacion():
    def __init__(self, nombre: str, metros_cuadrados: float):
        if not isinstance(nombre, str):
            raise TypeError("ERROR: El tipo de dato de nombre debe ser un str")
        self.nombre = nombre

        if not isinstance(metros_cuadrados, float):
            raise TypeError("ERROR: El tipo de dato de metros_cuadrados debe ser un float")
        if metros_cuadrados <= 0:
            raise ValueError(f"ERROR: Los metros cuadrados de la habitacion {self.nombre} deben ser mayores a 0")
        self.metros_cuadrados = metros_cuadrados