#listas , diccionarios

lista_de_alumnos = {60902 : "Rodolfo Fernandez", 61654 : "Luis Gomez", 61852: "Andrea Pereira", 61754 : "Juan Cruz Gonzales"}
materias = [["Ciencias", 0, 0, 0 ],["Historia",0 ,0 ,0],["Geografia",0 ,0 ,0 ],["Matematica",0 ,0 ,0 ],["Fisica",0 ,0 ,0 ]]
notasFinales = [["Rodolfo Fernandez",0],["Luis Gomez",0],["Andrea Pereira",0],["Juan Cruz Gonzales",0]]
"""materiasCargadas = []"""

#FUNCIONES

def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("ERROR: Debe ingresar un número.")

def pedir_notas(materias):   
    for materia in materias:
        while True:
                nota1 = pedir_entero(f"Ingrese el valor de nota 1 para la materia {materia[0]}\n")
                if 0 <= nota1 <= 10:
                    break
                else:
                    print(" La nota debe estar entre 0 y 10.")
        materia[1] = nota1
        while True:
                nota2 = pedir_entero(f"Ingrese el valor de nota 2 para la materia {materia[0]}\n")
                if 0 <= nota2 <= 10:
                    break
                else:
                    print(" La nota debe estar entre 0 y 10.")
        materia[2] = nota2
        promedio = (nota1+nota2)/2 
        materia[3] = promedio

def mostrar_notas(materias):
    for materia in materias:
        print(f"Materia: {materia[0]}\nNota 1: {materia[1]}\nNota 2: {materia[2]}\nPromedio: {materia[3]}")

def mostrar_mayor_promedio(materias):
    materia_mas_alta = ""
    nota_mas_alta = 0


    for i in (materias):
        if i[3] > nota_mas_alta:
            nota_mas_alta = i[3]
            materia_mas_alta = i[0]
    
    print(f"El promedio mas alto es de la materia {materia_mas_alta} con un promedio de {nota_mas_alta}")

def asignar_notas_finales(materias,notasFinales, nro_alumno):
    suma = 0

    for i in (materias):
        suma += i[3]
        
    promedio = suma / len(materias)
    notasFinales[nro_alumno][1] = promedio
    print(f"Alumno: {notasFinales[nro_alumno][0]} Nota Final: {notasFinales[nro_alumno][1]}")



#menu   



nro_alumno = -1
for i in lista_de_alumnos.items():
    nro_alumno +=1
    print(f"Legajo = {i[0]} Nombre = {i[1]}")
    pedir_notas(materias)
    mostrar_notas(materias)
    mostrar_mayor_promedio(materias)
    asignar_notas_finales(materias,notasFinales, nro_alumno)
        



