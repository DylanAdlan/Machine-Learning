"""
Input Format Specifications:

The first line of input consists of several sets you required. # N
The second-line consists of entering the inputs to the sets.# set_numbers
Note that print the elements in sorted order. # using sort function

Output Format Specifications:

The first line of output contains the Union of all sets. # set.union
The second line of output contains the Second largest Number of Union sets.
Sample Input 1:
3
1,1
2,1
4,5
Sample Output 1:
set([1, 2, 4, 5])
4
"""

N = int(input())

set_numbers = []
for value in range(N):
    value = input().split(',') # input the numbers and split them by comma
    numbers = map(int, value) # convert them from string into int
    set_numbers.append(set(numbers)) # set the value

# print(set_numbers)

combined_set = set.union(*set_numbers)
# print(combined_set)

# sorted them and store in a list (from set)
sorted_set_number = sorted(combined_set)
print(f"set({sorted_set_number})")

# make them in descending order
reverse = sorted_set_number[::-1]
# print(reverse)

# to take the second highest
print(reverse[1])
