"""
Input and Output Format:
1st input is a number indicates a total number of elements in the list.
2nd input is a String contains a list of numbers.
3rd input is number indicates K (number of elements need to sum every time)
The output contains a set of elements after summing. ( Refer to sample output format).
 
Note: All text in bold corresponds to the input and the rest corresponds to output.
 
Sample Input and Output 1:
9
1 3 2 4 5 1 6 31 15
[1, 2, 3, 4, 5, 6, 15, 31]
3
[6, 15, 31]

"""

array = int(input("enter size of number:"))

numbers = input().split()

set_numbers = set(numbers)

list_number = []
for i in set_numbers:
    list_number.append(i)

print(list_number)

size = int(input())

for length in len(list_number):
    


