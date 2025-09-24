#FUNCION 

def informacion_personal(nombre , apellido , edad , residencia):
     return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."

#PROGRAMA PRINCIPAL

nombre_ingresado = input("Ingrese su Nombre ")
apellido_ingresado = input("Ingrese su Apellido ")
edad_ingresado = input("Ingrese su Edad ")
residencia_ingresado = input("Ingrese su Residencia ")

presentacion = informacion_personal(nombre_ingresado , apellido_ingresado , edad_ingresado , residencia_ingresado)

print(presentacion)