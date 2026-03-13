print("----BIENVENIDO A LA ACADEMIA DE BAILE LAORA ----\n")

clases = int(input("¿Cuántas clases asististe este mes?: "))

if clases < 5:
    print("Asistencia baja")
elif clases >= 5 and clases <= 8:
    print("Asistencia media")
else:
    print("Asistencia alta")