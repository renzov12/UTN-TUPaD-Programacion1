class persona():
    def __init__(self , nombre ,apellido , edad , nacionalidad ):
        self.nombre = nombre 
        self.apellido = apellido
        self.edad = edad 
        self.nacionalidad = nacionalidad


nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
nacionalidad = input("Ingrese su nacionalidad: ")

class empleado(persona):
    def __init__(self, nombre, apellido, edad, nacionalidad , trabajo , salario):
        super().__init__(nombre, apellido, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario


trabajo = input("Ingrese cual es su trabajo: ")
salario =  input("Ingrese cuanto es su salario: ")

trabajador = empleado(nombre , apellido , edad , nacionalidad , trabajo , salario)

print(f"""
      -DATOS DEL EMPLEADO-

      NOMBRE: {trabajador.nombre} \n
      APELLIDO: {trabajador.apellido}\n
      EDAD: {trabajador.edad}\n
      NACIONALIDAD: {trabajador.nacionalidad}\n
      TRABAJO: {trabajador.trabajo}\n
      SALARIO: {trabajador.salario}


""")


if (edad >= 40):
    print("USTED NO PUEDE TRABAJAR EN NUESTRA EMPRESA.")

else:
    print("BIENVENIDO A NUESTRA EMPRESA")

