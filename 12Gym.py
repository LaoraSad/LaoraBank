print("----BIENVENIDO A LAORA GYM----\n")

bajo = 0
medio = 0
alto = 0

for i in range(1,5,1):
    
    nombre=input("\nCual es tu nombre?: ")
    dias_asistidos= int(input("cuantos dias asististes en la semana?: "))
    promedio=int(input("cuantos minutus entrenas por dia?: "))

    if dias_asistidos < 3:
        print("Compromiso bajo\n")
        bajo += 1
    elif dias_asistidos >= 3 and dias_asistidos <= 4:
        print("Compromiso medio\n")
        medio += 1
    else:
        print("Compromiso alto\n")
        alto += 1

print("\n----- RESULTADOS -----")
print("Personas con compromiso bajo:", bajo)
print("Personas con compromiso medio:", medio)
print("Personas con compromiso alto:", alto)
    

