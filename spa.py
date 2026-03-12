print("----BIENVENIDO A SPA LAORA----\n"
      "servicios disponibles")

servicios = ["1.masaje", "2.facial", "3.manicura"]

for i in servicios:
    print(i)

opcion = input("escoge el servicio que deseas: ")

if opcion == "1":
    print("servicio disponible: masaje")
elif opcion == "2":
    print("servicio disponible: facial")
elif opcion == "3":
    print("servicio disponible: manicura")
else:
    print("servicio no disponible")





