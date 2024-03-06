l=[3,4,5,3,4,4,5,5,6,6,0,0,20,14,5,1,20]
unique=[]
duplicates=set()
for x in l:
    if x in unique:
        duplicates.add(x)
    else:
        unique.append(x)

print(list(duplicates))