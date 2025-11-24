class Componente_cpu():
    def __init__(self, componente: str, marca: str, cantidad: int, precio: float):
        if not isinstance(componente, str):
            raise TypeError("ERROR: El tipo de dato componente debe ser un str")
        self.componente = componente

        if not isinstance(marca, str):
            raise TypeError("ERROR: El tipo de dato de marca debe ser un str")
        self.marca = marca

        if not isinstance(cantidad, int):
            raise TypeError("ERROR: El tipo de dato cantidad debe ser un int")
        if cantidad < 1: 
            raise ValueError(f"ERROR: La cantidad de {self.componente} debe ser mayor a 1")
        self.cantidad = cantidad

        if not isinstance(precio, float):
            raise TypeError("ERROR: El tipo de dato precio debe ser un float")
        if precio < 0:
            raise ValueError(f"ERROR: El precio de {self.componente} debe ser mayor a 0")
        self.precio = precio