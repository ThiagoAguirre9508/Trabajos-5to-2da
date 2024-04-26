n = int(input("ingrese un número: "))

if n >= 1 and n <= 9:
    print("el número tiene un dígito")
elif n <= 99 and n >= 10:
    print("el número tiene dos dígitos")