l=[3,4,5,3,4,4,5,5,6,6,0,0,20,14,5,1,20]
unique=[]
duplicates=[]
for x in l:
    if x in unique:
        duplicates.append(x)
    else:
        unique.append(x)
for y in unique:
    count=1
    for i in range(len(duplicates)):
        if(y == duplicates[i]):
            count+=1
    if(count == 2):
        print(y)
