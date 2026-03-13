print("---- BIENVENIDO A PARQUEADERO LAORA ----\n")

total_recaudado = 0
carros = 0
motos = 0

mayor_pago = 0
placa_mayor = ""

for i in range(1,9,1):

    placa = input(f"\nPlaca del vehículo numero {i}: ")

    print("Tipo de vehículo")
    print("1. Carro")
    print("2. Moto")

    tipo = int(input("Seleccione el tipo: "))
    horas = int(input("Horas parqueado: "))

    if tipo == 1:
        pago = horas * 4000
        carros += 1
    elif tipo == 2:
        pago = horas * 2000
        motos += 1
    else:
        print("Tipo inválido")
        continue

    print("Total a pagar:", pago)

    total_recaudado += pago

    if pago > mayor_pago:
        mayor_pago = pago
        placa_mayor = placa


print("\n----- RESUMEN DEL DÍA -----")
print("Total recaudado:", total_recaudado)
print("Carros ingresados:", carros)
print("Motos ingresadas:", motos)
print("Vehículo que pagó más:", placa_mayor, "-", mayor_pago)