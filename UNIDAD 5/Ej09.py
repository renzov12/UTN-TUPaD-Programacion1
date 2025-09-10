# 9) Dada la lista “compras”, realizar las siguientes modificaciones: agregar, reemplazar y eliminar elementos, luego imprimir la lista
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 


compras[2].append("jugo")
compras[1][1] =("tallarines")
compras[0].remove("pan")


print(compras)