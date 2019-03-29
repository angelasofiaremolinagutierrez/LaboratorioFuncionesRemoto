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

nveces = 0
while True:
    try:
        n = int(input("Ingresa un número: "))
        if n <= 0 :
            break
        else:
            is_prime()
            nveces = nveces + 1
    except ValueError:
        print ("Carácter no válido. Intenta otra vez")

print("Se comprobó", nveces,"veces si un número era primo")

nv_div = 0
for y in range (1,nveces+1):
    if (nveces%y) == 0:
      nv_div = nv_div + 1
if nv_div<=2 and nv_div>0:
    print("Y está cantidad fue prima")
else:
    print("Y está cantidad no fue prima")