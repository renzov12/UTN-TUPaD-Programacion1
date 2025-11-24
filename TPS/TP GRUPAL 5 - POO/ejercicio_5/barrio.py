from ejercicio_5.vivienda import Vivienda

class Barrio():
    def __init__(self, nombre: str, empresa_constructora: str, viviendas: list):
        if not isinstance(nombre, str):
            raise TypeError("ERROR: El tipo de dato de nombre debe ser un str")
        self.nombre = nombre

        if not isinstance(empresa_constructora, str):
            raise TypeError("ERROR: El tipo de dato de empresa_constructora debe ser un str")
        self.empresa_constructora = empresa_constructora

        if not isinstance(viviendas, list):
            raise TypeError("ERROR: El tipo de dato viviendas debe ser un list")
        for vivienda in viviendas:
            if not isinstance(vivienda, Vivienda):
                raise TypeError(f"ERROR: Las viviendas deben ser de tipo vivienda")
        self.viviendas = viviendas

    def get_superficie_total_terreno(self):
        return sum([vivienda.superficie_terreno for vivienda in self.viviendas])
    
    def get_superficie_total_terreno_x_manzana(self, manzana: str):
        return sum([vivienda.superficie_terreno for vivienda in self.viviendas if vivienda.manzana == manzana])
    
    def get_superficie_total_cubierta(self):
        return sum([vivienda.get_metros_cuadrados_cubiertos() for vivienda in self.viviendas])