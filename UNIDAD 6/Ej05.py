#FUNCIONES

def segundo_a_horas(segundos):
    horas = segundos/3600

    return horas     




#PROGRAMA 

segundos_ingresados = int(input("Ingrese la cantidad de SEGUNDOS "))

ressultado = segundo_a_horas(segundos_ingresados)

print(f"{segundos_ingresados}) segundos equivalentes a {ressultado} horas")
