class Estudiante:
    def __init__(self , nombre , edad , grado):
        self.nombre = nombre 
        self.edad = edad 
        self.grado = grado 

    def estudiar(self):
        print(f"El estudiante {self.nombre} esta estudiando...... ")

    def NoEstudiar(self):
        print(f"El estudiante {self.nombre} no va a estudiar........")


nombre=input("Ingrese el nombre del alumno: ")
edad=input("Ingrese la edad del alumno: ")
grado=input("Ingrese el grado del alumno: ")
        
        
alumno1 = Estudiante(nombre , edad , grado)

print(f"""
        ----------DATOS DEL ESTUDIANTE:---------- \n\n
        Nombre: {alumno1.nombre} 
        Edad: {alumno1.edad} 
        Grado: {alumno1.grado} 

""")



while True:


    
    print("¿El estudiante debe de estudiar?")
    estudiar = input("Ingrese ESTUDIA si desea que el estudiante estudie ingrese NO si no quiere: ")
    if(estudiar.lower() == "estudia"):
        alumno1.estudiar()
        break

    else:
        if(estudiar.lower() == "no"):
            alumno1.NoEstudiar()
            break
        else:
            print("Ingrese una opcion valida")
