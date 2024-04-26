n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese un número: "))
n3 = int(input("Ingrese un número: "))

if n1 < 10 and n2 < 10 and n3 < 10:
    print("Todos los números son menores a diez")
elif n1 > 10 and n2 > 10 and n3 < 10:
    print("Alguno de los números es menor a diez")
elif n1 > 10 and n2 < 10 and n3 > 10:
    print("Alguno de los números es menor a diez")
elif n1 < 10 and n2 > 10 and n3 > 10:
    print("Alguno de los números es menor a diez")
elif n1 > 10 and n2 > 10 and n3 > 10:
    print("Todos los números son mayores a diez")
else:
    print("Fin.")