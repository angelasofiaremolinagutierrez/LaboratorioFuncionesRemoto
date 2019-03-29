def a_power_b():

    prod_acum = 1
    for x in range (1,b+1):
        prod_acum = prod_acum * a
    print(prod_acum)

while True:
        try:
            a=int(input("Ingrese el número base: "))
            if a != 0:
                b=int(input("Ingrese el número exponente: "))
                a_power_b()
            else:
                print("Carácter no válido")
                break

        except ValueError:
            print ("Carácter no válido. Intenta otra vez")