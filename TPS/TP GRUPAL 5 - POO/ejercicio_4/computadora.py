from ejercicio_4.componente_cpu import Componente_cpu
class Computadora():
    def __init__(self, marca: str, modelo: str, componentes: list):
        if not isinstance(marca, str):
            raise TypeError("ERROR: El tipo de dato marca debe ser un str")
        self.marca = marca

        if not isinstance(modelo, str):
            raise TypeError("ERROR: El tipo de dato modelo debe ser un str")
        self.modelo = modelo

        if not isinstance(componentes, list):
            raise TypeError("ERROR: El tipo de dato componentes debe ser un list")
        for componente in componentes:
            if not isinstance(componente, Componente_cpu):
                raise TypeError(f"ERROR: Los componentes de {self.marca} {self.modelo} deben ser de tipo Componente_cpu")
        self.componentes = componentes