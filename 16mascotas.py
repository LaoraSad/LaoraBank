print("---- BIENVENIDA A TIENDA DE MASCOTAS LAORA ----\n")

alimento = 0
juguete = 0
accesorio = 0

for i in range(1,11,1):

    print("\nCategorías")
    print("1. Alimento")
    print("2. Juguete")
    print("3. Accesorio")

    categoria = int(input("Seleccione la categoría: "))
    valor = int(input("Valor de la compra: "))

    if categoria == 1:
        alimento += valor
    elif categoria == 2:
        juguete += valor
    elif categoria == 3:
        accesorio += valor
    else:
        print("Categoría no válida")
        continue


# determinar cuál vendió más
if alimento > juguete and alimento > accesorio:
    mayor = "Alimento"
elif juguete > alimento and juguete > accesorio:
    mayor = "Juguete"
else:
    mayor = "Accesorio"


print("\n----- RESULTADOS -----")
print("Total vendido en alimento:", alimento)
print("Total vendido en juguete:", juguete)
print("Total vendido en accesorio:", accesorio)
print("Categoría que generó más dinero:", mayor)