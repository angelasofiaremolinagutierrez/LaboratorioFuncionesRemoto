def is_prime():
  div = 0
  for x in range (1,n+1):
    if (n%x) == 0:
      div = div + 1

  if div>2:
    print("Is NOT a prime number")
  else:
    print("Is a prime number")
#cero(0) = no primo
#uno(1) = primo
#-uno(-1) = otro
n = int(input("Enter a number: "))
is_prime()