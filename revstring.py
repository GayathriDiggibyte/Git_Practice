def rev(s):
  rev1=""
  for i in range(len(s)-1,-1,-1):
    rev1=rev1+s[i]
  return rev1

def main():
  s=input("Enter a string : \n")
  res=rev(s)
  print("The reversed string ",s," is : ",res)
main()