# Creating a frozenset
fs = frozenset([1, 2, 3, 4])

# Accessing elements (similar to set)
for element in fs:
    print(element)

# Operations (similar to set)
fs1 = frozenset([2, 3, 4, 5])
union = fs | fs1
intersection = fs & fs1
difference = fs - fs1
difference2 = fs1 - fs
print("Union:", union)
print("Intersection:", intersection)
print("Difference:", difference)
print("Difference:", difference2)
number = {1,2,3,4}

for i in number:
    print(i)