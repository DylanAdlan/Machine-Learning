"""
Input Format:
First line of the input is an integer, which corresponds to the total number of school, 'n'.
Next 'n' line of inputs are integers, which corresponds to the total number of students in each school.
Last line of input is an integer indicates the price of a book.

Output Format:
The output consists of a total number of books required and total cost.

Sample Input:
# number of schools
5 
# no of students for each school
20 
50
60
45
25
# price of each book
20 
Sample Output:
Total number of books required : 200
Total cost: 4000
"""

schools = int(input())

student= []
for i in range(schools):
    number = int(input())
    student.append(number)
    
price = int(input())

sum  = 0
for i in student:
    sum = sum + i

# total price = sum of all students x price
sum_price = sum*price

print(f"Total number of books required: {sum}")
print(f"Total cost: {sum_price}")