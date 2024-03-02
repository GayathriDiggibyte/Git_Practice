def palin(n):
  rev=0
  t=n
  while(t>0):
    rem=t%10
    rev=(rev*10)+rem
    t=t//10
  print(rev)
n=int(input("Enter a number: "))
palin(n)
