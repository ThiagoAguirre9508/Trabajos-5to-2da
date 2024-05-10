edad = int(input("Ingrese su edad: "))
impuestos = int(input("Ingrese sus ingresos mensuales: "))

if edad >= 18 and impuestos >= 1000:
    print("Usted puede tributar")
else:
    print("Usted no puede tributar")
