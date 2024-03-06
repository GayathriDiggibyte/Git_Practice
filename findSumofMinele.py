l=[[1,5,6],[6,5,4],[3,2,4]]
sum=0
minele=[]
for list1 in l:
    list1=sorted(list1)
    print(list1)
    minele.append(list1[0])
print("The minimum elements in each list are: ",minele)
for x in minele:
    sum=sum+x
print(sum)