print("----BIENVENIDO A TIENDA DEPORTIVA GYM----\n")
producto1=[]
for i in range(1,7,1):
    producto = int(input(f"ingrese el precio del producto {i}: "))
    if producto > 100000:
        producto1.append(producto)
if producto1:
    print(f"productos con precio mayor a 100000: {producto1}")
else:
    print("no hay productos mayores a 100000")

       



