set1={3,5,6,8,9,7}
set2=set((6,8,1,2,5))
print(len(set1))
set1.update(set2)
print("update method",set1)
set1={3,5,6,8,9,7}
set2=set((6,8,1,2,5))
set1.union(set2)
print("union method",set1)
set1={3,5,6,8,9,7}
set2=set((6,8,1,2,5))
set1.intersection_update(set2)
print("intersection update method",set1)
set1={3,5,6,8,9,7}
set2=set((6,8,1,2,5))
set1.symmetric_difference_update(set2)
print("symmetric difference update method",set1)
set1={3,5,6,8,9,7}
set2=set((6,8,1,2,5))
set3=set1.intersection(set2)
print("intersection method",set3)
set1={3,5,6,8,9,7}
set2=set((6,8,1,2,5))
set3=set1.symmetric_difference(set2)
print("symmetric difference method",set3)

