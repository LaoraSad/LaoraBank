saldo_disponible = 9000 #con lo que inicio
print(f"su saldo disponible es: {saldo_disponible}")

lu= "0"

while(lu != "3"):
    print(""" queremos darte la bienvenida a jochis, para continuar dijite la opción que deseas realizar:
              1. Retirar saldo
              2. depositar saldo
              3. salir""")
    lu= input()
    
    lud_valid = int(lu)
    
    if lud_valid == 1:
        try: 
            
            retiro= float(input("cuanto saldo deseas retirar: ").replace(",","."))
    
            if retiro <= 0:
                print("ingrese un numero mayor a 0")
            
            elif retiro <= saldo_disponible:
                saldo_disponible -= retiro   
                print(f"Tu saldo actual es: {saldo_disponible}")
        
            else:
                print("No tienes suficiente saldo")
        except ValueError:
            print("debes ingresar un numero")

    elif lud_valid == 2:
        depositar_saldo= float(input("cuanto saldo deseas depositar"))
        saldo_disponible += depositar_saldo
        print(f"tu nuevo saldo de jochis es: {saldo_disponible}")
        
    elif lud_valid == 3:
        print("gracias por visitar jochis, la operación se ha realizado con exito")
    else:
        print("Por favor ingresa una opción valida")
        
