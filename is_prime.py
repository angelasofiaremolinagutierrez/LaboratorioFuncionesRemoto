def is_prime():
    div = 0
    for x in range (1,n+1):
        if (n%x) == 0:
          div = div + 1

    primo = 1
    no_primo = 0
    otro = -1
    if div<=2 and div>0:
        print(primo)
    elif div>2:
        print(no_primo)
    else:
        print(otro)

try:
    n = int(input("Ingresa un número: "))
    is_prime()
except ValueError:
    print ("Carácter no válido. Intenta otra vez")