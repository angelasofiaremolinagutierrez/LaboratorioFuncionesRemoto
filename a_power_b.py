a=int(input("Ingrese el número base: "))
b=int(input("Ingrese el número exponente: "))
def a_power_b():
    prod_acum = 1
    for x in range (1,b+1):
        prod_acum = prod_acum * a
    print(prod_acum)

a_power_b()