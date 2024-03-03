def fib(n):
  t1=0
  t2=1
  print(t1," ",t2)
  for i in range(2,n+1):
    t3=t1+t2
    print(t3)
    t2=t3
    t1=t2
n=int(input("Enter a number to print fibonacci series: \n"))
fib(n)
commit1
commit2
commit3