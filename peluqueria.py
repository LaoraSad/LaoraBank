print("----BIENVENIDO A LA PELUQUERIA LAORA ----\n")

hora_llegada=int(input("ingrese su hora de llegada(Formato:0-22)"))

if hora_llegada >=6 and hora_llegada <=11:
    print("Turno de mañana")
elif hora_llegada >=12 and hora_llegada <=17:
    print("Turno de tarde")
elif hora_llegada >=18 and hora_llegada <=22:
    print("Turno de noche")
else:
    print("fuera de horario ")