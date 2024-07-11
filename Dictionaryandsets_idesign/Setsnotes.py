"""
video 1 - set introduction

sets = -{1,2,3,4,5}
unordered - hashing
unindexed

- no duplicate elements
- eements should be immutable

hash function - key 

"""
'''
s = set() # datatype = class set
print(type(s))
s1 = {'orange', 'apple', 'mango', 'grapes', 'apple'} # no duplicate values
print(s1)
print(type(s1))

'''

'''
l = [1,2,3,4,7,1,2,3,4]
s = set(l)
print("In a list:", l)
print("After convert to set:", s) # remove duplicate values


print("s set values in sorted")
for i in sorted(s): # set boleh sorted
    print(i, end=" ")
    
'''

'''

s = {12, 23, 43, 13, 34}
print("\nOriginal set s", s)
s.add(123) # add new value in a set
print("After adding 123:",s)

'''
'''
s1 = {234, 345, 567}
s.update(s1) # joining two sets together in a first set
print("After update s + s1: s", s)
print("After update s + s1: s1", s1)

'''
'''
s = {12, 23, 43}
print("Original s values:",s)
s.remove(12) # remove specific value in a set
print("After remove 12:", s)
# s.remove(56) # remove non exist value # error
# print(s)
'''

'''
s = {12, 23, 43}
s.discard(56) # remove non exist value but no error raise
print(s)
s.discard(23) # remove 23
print(s)
s.pop() # pop takes no argument, random remove one value
print(s)
s = {12, 23, 43}
# s.clear() # remove all, leave empty set
del(s) # totally remove that variable, so keluar error undefined name 's'
print(s)

'''
'''
video 2 - set operation

- union
- intersection
- difference
- symmetric difference

'''

S1 = {1,2,3,4,5,6,7,8,9,10}
S2 = {2,4,6,8,10,12,14,16,18,20}
print("Union between S1 and S2:", S1.union(S2)) # just union time nih, but dont effect original set
print("S1 after union:",S1) # still the same value at original one
print("S2 after union:",S2) 


print("Intersection between S1 and S2:", S1.intersection(S2)) # ambik yg sama antra S1 and S2
# print("Intersection update between S1 and S2:", S1.intersection_update(S2)) # ambik yg sama antra S1 and S2 and update yg baru into S1
# print("S1 after intersection update:",S1) 
print(S2) # does not effct


print("Apa yg ada kat S1 xde kat S2:", S1.difference(S2))
print("Apa yg ada kat S2 xde kat S1:", S2.difference(S1))

print("Gabungan difference S1 and S2:", S1.symmetric_difference(S2)) # gabungan difference S1 and S2

S1 = {1,2,3,4,5,6,7,8,9,10}
S2 = {2,4,6,8,10}

print(S1.issuperset(S2))
print(S2.issuperset(S1))
print(S1.issubset(S2))
print(S1.issubset(S2))

S1 = {1,2,3,4,5}
S2 = {6,7,8,9,10}
print(S1.isdisjoint(S2)) # xde common elements in 2 sets











