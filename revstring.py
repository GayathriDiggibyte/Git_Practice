def rev(s):
  rev1=""
  for i in range(len(s)-1,-1,-1):
    rev1=rev1+s[i]
  print(rev1)
s="gaythri"
rev(s)