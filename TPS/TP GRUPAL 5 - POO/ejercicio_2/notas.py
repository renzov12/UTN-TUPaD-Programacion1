class Nota():
    def __init__(self, catedra: str, nota: int):
        if not isinstance(catedra, str):
            raise TypeError("ERROR: El tipo de dato catedra debe ser un str")
        self.catedra = catedra

        if not isinstance(nota, float): raise TypeError("ERROR: El tipo de dato nota debe ser un float")
        if not 1<=nota<=10: raise ValueError("ERROR: El valor de nota debe estar entre 1 y 10")
        self.nota = nota
