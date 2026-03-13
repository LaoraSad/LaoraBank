print("---- BIENVENIDOS AL CURSO DE INGLÉS DE LAORA----\n")

total_promedios = 0
cantidad_estudiantes = 0

bajo = 0
medio = 0
alto = 0

mejor_promedio = 0
mejor_estudiante = ""

seguir = "si"

while seguir == "si":

    nombre = input("\nNombre del estudiante: ")

    speaking = float(input("Nota speaking: "))
    listening = float(input("Nota listening: "))
    reading = float(input("Nota reading: "))

    promedio = (speaking + listening + reading) / 3

    print("Promedio:", promedio)

    total_promedios += promedio
    cantidad_estudiantes += 1

    if promedio < 60:
        nivel = "Bajo"
        bajo += 1
    elif promedio <= 79:
        nivel = "Medio"
        medio += 1
    else:
        nivel = "Alto"
        alto += 1

    print("Nivel:", nivel)

    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_estudiante = nombre

    seguir = input("\n¿Desea registrar otro estudiante? (si/no): ").lower()


promedio_general = total_promedios / cantidad_estudiantes

print("\n---- RESULTADOS ----")
print("Promedio general del grupo:", promedio_general)
print("Mejor estudiante:", mejor_estudiante, "-", mejor_promedio)

print("Estudiantes nivel bajo:", bajo)
print("Estudiantes nivel medio:", medio)
print("Estudiantes nivel alto:", alto)