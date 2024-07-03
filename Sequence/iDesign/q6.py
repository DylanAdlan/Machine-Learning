"""
Input Format Specifications:

Firstline contains to enter the elements to set1(integers).
Second-line contains to enter the elements to set2(integers).
Note that print the elements in sorted order.
Output Format Specifications:

Output Consists of Symmetric_difference between set1 and set2 (Integers)
If both set elements are equal to print ‘invalid set’.
 

Sample Input1:
1,2,3,4,5,6
2,3,5,7,8,9
Sample Output1:
{1, 4, 6, 7, 8, 9}

Sample input2:
1,2,3
1,2,3
Sample Output2:
invalid set
"""

number1 = input()
number2 = input()

# # split them into list (string) ordered
# list_number1 = number1.split(",")
# print(list_number1)

# # convert list to set (string) # unordered
# set_number1 = set(number1.split(","))
# print(set_number1)

# set them from string to integer # unordered
int_set_number1 = set(map(int, number1.split(",")))
int_set_number2 = set(map(int, number2.split(",")))

# print(int_set_number1)
# print(int_set_number2)

# number in num1 and not in number2
num1_not_num2 = int_set_number1.difference(int_set_number2)

# number in num2 and not in number1
num2_not_num1 = int_set_number2.difference(int_set_number1)

# combine them toggther using union
differ = num1_not_num2.union(num2_not_num1)

# print the difference if exists otherwise print invalid
if differ:
    print(differ)    
else:
    print("invalid set")
