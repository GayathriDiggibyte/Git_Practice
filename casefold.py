str="MY NAME is GAYATHRI"
strele=str.split(" ")
casefold=[]
res=""
for x in strele:
    casefold.append(x.casefold())
for x in casefold:
    res=res+x+" "
print(res)