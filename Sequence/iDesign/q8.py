"""
Sample Input and Output:
Enter total Number of sheets: 
6
1
2 3 1
4 5 6
2 3 4 5 6 7
2
3 4
Attendance Sheets with Register Number: ((1,), (2, 3, 1), (4, 5, 6), (2, 3, 4, 5, 6, 7), (2,), (3, 4))
Final sheet: (1, 2, 3, 4, 5, 6, 7)

# """

# number = int(input("how many? "))

# students = [] 
# for i in range(number):
#     num_students = input() 
#     tuple_students = tuple(num_students.split()) # split by space each number masuk then tuplekan diorang
#     students.append(tuple_students) # store dalam list

# # print set in a list
# # print(students)

# #convert from list to tuple 
# tuple_students = tuple(students)
# # print(tuple_students)


# # bundle multiple tuples in list into a single tuple
# result = () # initialize an empty tuple and store values from (hasil tambah)
# for i in tuple_students:
#     result = result + i

# # nk convert string in tuple into int and store them into tuple
# # numbers = tuple([int(x) for x in result])

# # another method using map and kna tuplekan balik
# numbers = tuple(map(int, result))
# print(numbers)



# unique_values = []  # Initialize an empty list to store unique values
# seen = set()        # Initialize an empty set to keep track of seen values

# for value in numbers:
#     if value not in seen:  # Check if the value is not in the set 'seen'
#         unique_values.append(value)  # Add the value to the list of unique values
#         seen.add(value)  # Add the value to the set 'seen'

# unique_tuple = tuple(unique_values)  # Convert the list of unique values back to a tuple
# print(unique_tuple)  # Output: (1, 2, 3, 4)

############################################################################################################
# SYU METHOD
numSheet = int(input("Enter total Number of sheets:"))

attendance_sheets = []
for i in range(numSheet):
    registerNum = tuple(map(int, input().split(" ")))
    attendance_sheets.append(registerNum)

print("Attendance Sheets with Register Number: ",tuple(attendance_sheets))

unique_registers = set()
for sheet in attendance_sheets:
    for register in sheet:
        unique_registers.add(register)

print("Final sheet:", tuple(unique_registers))
