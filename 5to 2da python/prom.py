n1 = int(input("ingrese la primera nota: "))
n2 = int(input("ingrese la segunda nota: "))
n3 = int(input("ingrese la tercera nota: "))
prom = (n1 + n2 + n3)/3
if prom > 7:
    print("Promocionado")
elif prom < 7:
    print("no fue promocionado")