alumnos = {}


for i in range(3):
    nombre = (input(f"Ingrese el nombre del alumno{i+1}:"))

    notas = []

    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
        alumnos[nombre] = tuple(notas)

print("Promedios")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")