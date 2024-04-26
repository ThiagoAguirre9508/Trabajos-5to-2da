n = int(input("Ingrese un número: "))
n2 = int(input("Ingrese otro número: "))

if n > n2:
    r = n+n2
    r2 = n-n2
    print("La suma de los números es: ", r)
    print("La resta de los números es: ", r2)
elif n < n2:
    r = n*n2
    r2 = n/n2
    print("La multiplicación de los números es: ", r)
    print("La división de los números (del primero respecto al segundo) es : ", r2)