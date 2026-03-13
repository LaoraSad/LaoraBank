print("---- INVENTARIO DE PRODUCTOS LAORA----\n")

agotado = 0
stock_bajo = 0
stock_normal = 0

for i in range(1,11.1):

    nombre = input("\nNombre del producto: ")
    cantidad = int(input("Cantidad disponible: "))

    if cantidad == 0:
        agotado += 1
    elif cantidad <= 5:
        stock_bajo += 1
    else:
        stock_normal += 1


print("\n---- RESULTADOS ----")
print("Productos agotados:", agotado)
print("Productos con stock bajo:", stock_bajo)
print("Productos con stock normal:", stock_normal)