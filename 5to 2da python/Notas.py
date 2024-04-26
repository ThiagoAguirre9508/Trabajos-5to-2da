N1=int(input("Ingrese la nota 1:"))
N2=int(input("Ingrese la nota 2:"))
N3=int(input("Ingrese la nota 3:"))

prom=(N1+N2+N3)/3

if prom >= 7:
    print("Promocionado")
elif prom>=4:
        print ("Regular")
else:
        print ("Reprobado")