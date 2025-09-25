contactos = {}
for i in range(0,5):
    nombre = input("Ingrese el nombre del contacto ")
    numero = int(input("Ingrese el numero de telefono del contacto "))
  #DICCIONARIO
    contactos[nombre] = numero
print(contactos)