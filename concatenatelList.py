str1=input("Enter a list separated by spaces ")
strele1=str1.split(" ")
str2=input("Enter a list separated by spaces ")
strele2=str2.split(" ")
l1=[]
l2=[]
l3=[]
for x in strele1:
    l1.append(int(x))
for y in strele2:
    l2.append(int(y))
l3=l1+l2
print(l3)