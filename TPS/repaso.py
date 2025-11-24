class Animal():

    def __init__(self, categoria , dieta):
        self.categoria = categoria
        self.dieta = dieta


    def comer(self):
        print(f"El perro va a comer {self.dieta}")
    







class Perro(Animal):
    def __init__(self , categoria , dieta , raza):
        super().__init__(categoria , dieta)
        
        self.raza = raza


class Gato(Animal):
    def __init__(self, categoria, dieta, color):
        super().__init__(categoria, dieta)

        self.color = color


    def comer(self):
        print(f"yo soy {self.categoria}")
        print(f"pero me gusta el pescado")


Animal1 = Perro("mamifero " ,"carnivoro " , "caniche ")
Animal2 = Gato("mamifero " ," vegetaliano" , "Negro ")




Animal1.comer()
print("")
Animal2.comer()