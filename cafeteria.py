print("----BIENVENIDO A LA CAFERERÍA LAORA ----\n")

print(
"--------Menu-------\n" 
"1.café = 4000\n"
"2.té = 3500\n"
"3.jugo = 5000\n"
)

opcion=int(input("¿Qué bebidas deseas comprar? "))
if opcion==1:
    bebida= "café "
    precio= 4000
elif opcion==2:
    bebida= "Té"
    precio= 3500
elif opcion==3:
    bebida="Jugo"
    precio=5000
else:
    print("Escoja una opcion valida")

unidades=int(input("¿Cuántas unidades deseas?"))

total= precio * unidades

print("Bebida:", bebida)
print("Unidades:", unidades)
print("total a pagar:", total)
