print("---- REGISTRO DEL CLUB LAORA----\n")

total = 0

basico = 0
premium = 0
familiar = 0

seguir = "si"

while seguir == "si":

    nombre = input("\nNombre: ")
    edad = int(input("Edad: "))

    print("\nPlanes")
    print("1. Básico: 50000")
    print("2. Premium: 90000")
    print("3. Familiar: 130000")

    plan = int(input("Seleccione plan: "))

    if plan == 1:
        precio = 50000
        basico += 1
    elif plan == 2:
        precio = 90000
        premium += 1
    elif plan == 3:
        precio = 130000
        familiar += 1
    else:
        print("Plan no válido")
        continue

    total += precio

    if edad < 18:
        print("Registro juvenil")
    elif edad >= 60:
        print("Beneficio senior")

    seguir = input("\n¿Desea registrar otra persona? (si/no): ").lower()


# determinar plan más vendido
if basico > premium and basico > familiar:
    mas_vendido = "Básico"
elif premium > basico and premium > familiar:
    mas_vendido = "Premium"
else:
    mas_vendido = "Familiar"


print("\n---- RESULTADOS ----")
print("Total recaudado:", total)

print("Personas plan básico:", basico)
print("Personas plan premium:", premium)
print("Personas plan familiar:", familiar)

print("Plan más vendido:", mas_vendido)