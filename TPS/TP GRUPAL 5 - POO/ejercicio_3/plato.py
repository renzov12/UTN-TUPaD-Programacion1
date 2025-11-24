from ejercicio_3.ingrediente import Ingrediente
class Plato():
    def __init__(self, nombre_completo: str, precio: float, esBebida: bool, ingredientes: list):
        if not isinstance(nombre_completo, str):
            raise TypeError("ERROR: El tipo de dato nombre_completo debe ser un str")
        self.nombre_completo = nombre_completo

        if not isinstance(precio, float):
            raise TypeError("ERROR: El tipo de dato precio debe ser un float")
        if precio < 0: 
            raise ValueError(f"ERROR: El precio de {self.nombre_completo} debe ser mayor a 0")
        self.precio = precio

        if not isinstance(esBebida, bool):
            raise TypeError("ERROR: El tipo de dato esBebida debe ser un bool")
        self.esBebida = esBebida

        if not isinstance(ingredientes, list):
            raise TypeError("ERROR: El tipo de dato ingredientes debe ser un list")
        for ingrediente in ingredientes:
            if not isinstance(ingrediente, Ingrediente):
                raise TypeError(f"ERROR: Los ingredientes de {self.nombre_completo} deben ser de tipo Ingrediente")
        self.ingredientes = ingredientes