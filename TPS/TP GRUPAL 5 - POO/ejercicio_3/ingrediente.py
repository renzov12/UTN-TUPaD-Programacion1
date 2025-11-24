class Ingrediente():
    def __init__(self, nombre: str, cantidad: float, unidad_de_medida: str):
        if not isinstance(nombre, str):
            raise TypeError("ERROR: El tipo de dato nombre debe ser un str")
        self.nombre = nombre

        if not isinstance(cantidad, float):
            raise TypeError("ERROR: El tipo de dato cantidad debe ser un float")
        if cantidad <= 0:
            raise ValueError(f"ERROR: La cantidad del ingrediente {self.nombre} debe ser mayor a 0")
        self.cantidad = cantidad

        if not isinstance(unidad_de_medida, str):
            raise TypeError("ERROR: El tipo de dato unidad_de_medida debe ser un str")
        self.unidad_de_medida = unidad_de_medida