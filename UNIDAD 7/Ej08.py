
stock = {
    "manzanas": 10,
    "peras": 5,
    "naranjas": 8
}


print("Stock inicial:", stock)


producto = input("\nIngrese el nombre de un producto: ").lower()

if producto in stock:
    print(f"El stock de {producto} es: {stock[producto]} unidades")


    agregar = input(f"¿Desea agregar unidades a {producto}? (s/n): ").lower()
    if agregar == "s":
        cantidad = int(input("Ingrese cuántas unidades agregar: "))
        stock[producto] += cantidad
        print(f"Nuevo stock de {producto}: {stock[producto]}")

else:
    print(f"{producto} no existe en el stock.")
  
    agregar_nuevo = input("¿Desea agregarlo como nuevo producto? (s/n): ").lower()
    if agregar_nuevo == "s":
        cantidad = int(input("Ingrese la cantidad inicial: "))
        stock[producto] = cantidad
        print(f"Producto {producto} agregado con stock {cantidad}.")


print("\nStock final:", stock)
