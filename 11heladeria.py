print("----BIENVENIDO A HELADERIA LAORA----\n")

cono=0
vaso=0
banana_split=0

total_venta= 0
cliente= 0

continuar= "si"

while continuar =="si":
    print(
        "\nproductos  disponibles:\n"
          "1.Cono:3000\n"
          "2.Vaso:4000\n"
          "3.banana split:9000\n"
          "4.salir\n"
          )

    producto=int(input("Selecione el producto deseado: "))
    cantidad=int(input("cuantos deseas: "))
    
    if producto== 1:
        total= cantidad*3000
        cono += cantidad
    elif producto== 2:
        total= cantidad*4000
        vaso += cantidad
    elif producto== 3:
        total= cantidad*9000
        banana_split += cantidad
    else:
        print("\ningrese un producto valido\n")
        continue
    total_venta += total
    

    print("Total a pagar:", total)
    total_venta += total
    cliente += 1

    continuar = input("\n¿Hay otro cliente? (si/no): ").lower()

if cono > vaso and cono > banana_split:
    mas_vendido = "cono"
elif vaso > cono and vaso > banana_split:
    mas_vendido = "vaso"
else:
    mas_vendido = "banana split"

print("\n----- RESUMEN DEL DIA -----")
print("Total vendido:", total_venta)
print("Clientes atendidos:", cliente)
print("Producto más pedido:", mas_vendido)