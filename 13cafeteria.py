print("----BIENVENIDO A LA CAFETERIA LAORA----\n")

total_dia = 0
continuar = "si"

while continuar == "si":

    print(
        "--------Menu-------\n"
        "1.café = 4000\n"
        "2.capuchino = 7000\n"
        "3.pastel = 6000\n"
    )

    opcion = int(input("¿Qué deseas comprar? "))
    cantidad = int(input("¿Cuántos deseas?: "))

    if opcion == 1:
        total = cantidad * 4000
    elif opcion == 2:
        total = cantidad * 7000
    elif opcion == 3:
        total = cantidad * 6000
    else:
        print("Producto no válido")
        continue

    if total > 20000:
        descuento = total * 0.10
        total -= descuento
        print("Se aplicó 10% de descuento")

    print("Total a pagar:", total)

    total_dia += total

    continuar = input("¿Quieres seguir comprando? (si/no): ").lower()


print("\n----- RESUMEN DEL DÍA -----")
print("Total vendido:", total_dia)