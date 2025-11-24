from ejercicio_2.notas import Nota 
class Alumno():
    def __init__(self, nombre_completo: str, legajo: int, notas: list):
        if not isinstance(nombre_completo, str):
            raise TypeError("ERROR: El tipo de dato nombre_completo debe ser un str")
        self.nombre_completo = nombre_completo

        if not isinstance(legajo, int):
            raise TypeError("ERROR: El tipo de dato de legajo debe ser un int")
        self.legajo = legajo

        if not isinstance(notas, list): raise TypeError("ERROR: El tipo de datos de notas debe ser una list")
        for nota in notas:
            if not isinstance(nota, Nota): raise TypeError("ERROR: Los valores en la lista notas deben ser de tipo Nota")
        self.notas = notas

    def calcular_promedio(self):
        cantidad_notas = len(self.notas)
        sumatoria_notas = sum([notas.nota for notas in self.notas])
        promedio = sumatoria_notas / cantidad_notas
        return promedio