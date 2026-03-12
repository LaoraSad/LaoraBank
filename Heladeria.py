import time

print("----BIENVENIDO A HELADERIA LAORA----\n"
      "\nselecione qué sabor desea\n")
vainilla= 0
chocolate=0
fresa= 0



print(
        "Sabores disponibles:\n"
          "1.vainilla\n"
          "2.chocolate\n"
          "3.fresa\n"
          )


for i in range(5,1,-1):
    pedido= int(input(f"¿Qué sabor deseas elegir?: {i} pedidos disponibles "))

        
    if pedido == 1:
        vainilla += 1
        print(f"has elegido vainilla")
        
            

    elif pedido == 2:
        chocolate += 1 
        print(f"has elegido chocolate")
        

    elif pedido == 3:
        fresa += 1 
        print(f"has elegido fresa")
        

print("\n----TOTAL DEL PEDIDO----\n")
time.sleep(1)

print(
f"vainilla: {vainilla}\n" 
f"chocolate: {chocolate}\n"
f"fresa: {fresa}\n"
        )
time.sleep(1)

print("Gracias por visitar heladerias Laora")