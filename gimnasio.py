print("----BIENVENIDO A LAORA GYM----\n")

def edades(edad):

    if edad <13:
        return "NO PUEDE INGRESAR"
    elif 13 <= edad <= 17: 
        return "clase juvenil"
    elif 18 <= edad <= 59: 
        return "clase general"
    else:
        return "clase senior"

edad_usuario= int(input("por favor digite su edad: "))
print(edades(edad_usuario))
