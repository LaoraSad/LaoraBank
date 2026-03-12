print("----BIENVENIDO A AL CINE LAORA ----\n")

edad=int(input("¿Cual es tu edad?: "))

if edad <12 and edad >=0:
    print("Tu entrada vale $8.000")
elif  12<= edad <=59:
    print("Tu entrada vale $12.000")
elif edad >60:
    print("Tu entrada vale $9.000")
else: 
    print("digite una edad valida")