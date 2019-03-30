def perfect_number():
    sum_div = 0
    for x in range(1,n): #El rango va hasta n y no n+1, ya que no se debe tener en cuenta al número mismo en la suma :)
        if n%x == 0:
            sum_div = sum_div + x
    if sum_div == n:
        print(n, "es un número perfecto!")
    else:
        print(n, "no es perfecto :(")

n=int(input("Ingrese el número: "))
perfect_number()