print("----BIENVENIDO AL PARQUEADERO LAORA ----\n")
hora=int(input("¿cuántas horas estuvo en el parqueadero?: " ))

precio1=5000
adicional=3000
if hora==1:
    print("total a pagar", precio1)
else:
    total_pagar=precio1*adicional
    print("total a pagar:", total_pagar)