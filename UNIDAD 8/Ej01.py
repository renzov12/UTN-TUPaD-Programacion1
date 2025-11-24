def mostrar_Productos():
    productos = []
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            partes = linea.split(",")
            if len(partes) == 3:     
                diccionario = {
                    "nombre": (partes[0]),
                    "precio": (partes[1]),
                   "cantidad": (partes[2])
                }
            productos.append(diccionario)
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")

    return productos 

def buscar_producto(busqueda, Diccionario_de_productos):
    continuar = True
    busqueda = busqueda.lower()  
    while continuar:
        encontrado = False
        for producto in Diccionario_de_productos:
            if busqueda == producto["nombre"].lower():
                print(f"Nombre: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
                encontrado = True
                break
        if encontrado == False:
            print("Ese producto no está")

        respuesta = input("Desea continuar buscando un producto 1-Si 2-No: ")
        if respuesta != "1":
            continuar = False
            print("Guardo los productos actualizados correctamente")
        else:
            busqueda = input("Ingrese otro producto para buscar: ").lower()

archivo = open("Productos.txt", "a")
with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,300.0,15\n")
    archivo.write("Goma,80.0,50\n")
    
with open("productos.txt", "r") as archivo:
    productos_existente = archivo.readlines()
nombres = []
for p in productos_existente:
    nombre = p.strip().split(",")[0].lower()
    nombres.append(nombre)
productos_existente = nombres

seguir = True
while seguir:
    with open("productos.txt", "a") as archivo:
        agregar = int(input("Cuantos productos quiere ingresar "))
        for i in range(agregar):
            producto_nuevo = input(f"Ingrese el producto {i+1} (nombre,precio,cantidad): ")
            Nombre_del_producto = producto_nuevo.split(",")[0].lower() 
            if Nombre_del_producto in productos_existente:
                print("Ese producto ya esta agregado")
                break
            else:
                archivo.write(f"{producto_nuevo}\n")
                productos_existente.append(Nombre_del_producto)  
        else:
                seguir = False

Diccionario_de_productos = mostrar_Productos()

print("\nLista completa de diccionarios:" )
print(Diccionario_de_productos)         
busqueda = input("Ingresar un producto para buscar ")
buscar_producto(busqueda, Diccionario_de_productos)

with open("productos.txt", "w") as archivo:
    for p in Diccionario_de_productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")