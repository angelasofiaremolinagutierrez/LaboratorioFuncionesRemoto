def almost_perfect_number():
    sum_div = 0
    for x in range(1,n): #El rango va hasta n (y no n+1), ya que no se debe tener en cuenta al número mismo en la suma :)
        if n%x == 0:
            sum_div = sum_div + x

    if (sum_div-n) <= 3 and (sum_div-n) > 0 : #La diferencia debe ser mayor que cero (y no mayor o igual), ya que un número no puede ser perfecto y casi perfecto a la vez
        print(n, "es un número casi perfecto! :D")
    else:
        print(n, "no es ni casi perfecto D:")

n=int(input("Ingrese el número: "))
almost_perfect_number()