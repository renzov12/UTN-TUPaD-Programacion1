print("Escribiendo Archivo")
productos_archivos = open("productos.txt",'w')
productos_archivos.write("Lapicera,120,5\n")
productos_archivos.write("Lapiz,90,5\n")
productos_archivos.write("Cuaderno,250,5\n")

productos_archivos.close()
#2-----------------------------------------------------------------------------------------------------------------------
print("Leyendo y Mostrando Productos")

producto_archivo = open("productos.txt" , 'r')

for linea in producto_archivo:
    
    nombre , precio , cantidad = linea.strip().split(",")
    print(f"Producto : {nombre} | Precio : ${precio} , | Cantidad{cantidad}" )


    producto_archivo.close()

#3-----------------------------------------------------------------------------------------------------------------------
print("Agregar productos desde teclado: ")
nombre = input("Ingrese el nombre del producto: ")
precio = input("Ingrese el precio: ")
cantidad = input("Ingrese la cantidad: ")

productos_archivos = open("productos.txt" , 'a')

productos_archivos.write(f"{nombre} , {precio} , {cantidad} \n")

productos_archivos.close()
#4-----------------------------------------------------------------------------------------------------------------------

def mostar_productos():

    productos=[]
    with open("productos.txt" , 'r') as archivo :
        for linea in archivo:
            linea = linea.strip()
            partes = linea.split(" , ")
            if len(partes) == 3:
                diccionario = {

                    "nombre": (partes[0]),
                    "precio": (partes[1]),
                    "cantidad": (partes[2])
                    }
                
            productos.append(diccionario)
        for p in productos: 
         print(f"producto: {p['nombre']} | precio: {p['nombre']} | cantidad: {p['nombre']}")

    return productos 




#5-----------------------------------------------------------------------------------------------------------------------

