l=[5,4,6,7,2]
#lambda
res=lambda x:x**2
print(res(7))
#map
map1=list(map(res,l))
print(map1)
#filter
filter1=list(filter(lambda x : x%2 == 0,l))
print(filter1)
#reduce
from functools import reduce
reduce1=reduce(lambda x,y : x+y, l)
print(reduce1)