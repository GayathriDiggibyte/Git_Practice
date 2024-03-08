str="my name is gayathri"
strele=str.split(" ")
capitalized_string=[]
res=""
for x in strele:
    capitalized_string.append(x.capitalize())
for x in capitalized_string:
    res=res+x+" "
print(res)