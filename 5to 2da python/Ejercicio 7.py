renta = int(input("Ingrese su renta anual: "))

if renta < 10000:
    print("Su tipo impositivo es 5%")
elif renta >= 10000 and renta <= 20000:
    print("Su tipo impositivo es 15%")
elif renta >= 20000 and renta <= 35000:
    print("Su tipo impositivo es 20%")
elif renta >= 35000 and renta <= 60000:
    print("Su tipo impositivo es 30%")
elif renta > 60000:
    print("Su tipo impositivo es 45%")