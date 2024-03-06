l=[3,4,5,3,4,4,5,5,6,0,0,14,5,1,20]
unique_list=[]
for e in l:
    if e not in unique_list:
        unique_list.append(e)

print(unique_list)