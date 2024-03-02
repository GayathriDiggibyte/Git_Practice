def primeNo(n):
  count=0
  for i in range(1,n+1):
    if(n%i == 0):
      count++
  if(count == 2):
    print(n,"is a prime Number")
  else:
    print(n, "is not a prime Number")

n=int(input("Enter a number : "))
primeNo(n)