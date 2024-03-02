def palin(n):
  rev=0
  t=n
  while(t>0):
    rem=t%10
    rev=(rev*10)+rem
    t=t//10
  if(rev==n):
    print(n, " is a palindrome number")
  else:
    print(n, " is not a palindrome number")
n=int(input("Enter a number: "))
palin(n)
print("Program Ended")
