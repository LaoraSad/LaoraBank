print("---- BIENVENIDO AL CINE LAORA ----\n")

capacidad = int(input("Capacidad total de la sala: "))

total_personas = 0
niños = 0
adultos = 0
adultos_mayores = 0

continuar = "si"

while continuar == "si" and total_personas < capacidad:

    print("\nClasificación de edad")
    print("1. Niño (0-12)")
    print("2. Adulto (13-59)")
    print("3. Adulto mayor (60+)")

    opcion = int(input("Seleccione la categoría: "))

    if opcion == 1:
        niños += 1
    elif opcion == 2:
        adultos += 1
    elif opcion == 3:
        adultos_mayores += 1
    else:
        print("Opción no válida")
        continue

    total_personas += 1

    if total_personas < capacidad:
        continuar = input("¿Desea registrar otra persona? (si/no): ").lower()
    else:
        print("La sala se ha llenado")


print("\n----- RESUMEN -----")
print("Total de personas:", total_personas)
print("Niños:", niños)
print("Adultos:", adultos)
print("Adultos mayores:", adultos_mayores)

if total_personas == capacidad:
    print("La sala se llenó")
else:
    print("La sala no se llenó")