Nombre = str(input("Ingrese su nombre: "))
Clave = int(input("Ingrese su número de clave: "))
Antiguedad = int(input("Ingrese sus años de servivcio: "))

if Clave == 1:
    if Antiguedad == 1:
        print(Nombre, "tiene clave 1, tiene", Antiguedad, "años de antiguedad.")
        print("Merece 6 días de vacaciones")
    elif Antiguedad >= 2 and Antiguedad <= 6:
        print(Nombre, "tiene clave 1, tiene", Antiguedad, "años de antiguedad.")
        print("Merece 14 días de vacaciones")
    elif Antiguedad > 6:
        print(Nombre, "tiene clave 1, tiene", Antiguedad, "años de antiguedad.")
        print("Merece 20 días de vacaciones")
elif Clave == 2:
    if Antiguedad == 1:
        print(Nombre, "tiene clave 2, tiene", Antiguedad, "años de antiguedad.")
        print("Merece 7 días de vacaciones")
    elif Antiguedad >= 2 and Antiguedad <= 6:
        print(Nombre, "tiene clave 2, tiene", Antiguedad, "años de antiguedad.")
        print("Merece 15 días de vacaciones")
    elif Antiguedad > 6:
        print(Nombre, "tiene clave 2, tiene", Antiguedad, "años de antiguedad.")
        print("Merece 22 días de vacaciones")
elif Clave == 3:
    if Antiguedad == 1:
        print(Nombre, "tiene clave 3, tiene", Antiguedad, "años de antiguedad.")
        print("Merece 10 días de vacaciones")
    elif Antiguedad >= 2 and Antiguedad <= 6:
        print(Nombre, "tiene clave 3, tiene", Antiguedad, "años de antiguedad.")
        print("Merece 20 días de vacaciones")
    elif Antiguedad > 6:
        print(Nombre, "tiene clave 3, tiene", Antiguedad, "años de antiguedad.")
        print("Merece 30 días de vacaciones")
else:
    print("Los datos son incorrectos")