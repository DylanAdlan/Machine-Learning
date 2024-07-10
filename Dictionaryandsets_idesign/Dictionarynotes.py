""" NOTES

dictionary { "adnin": 24, "farah": 24}
key - value

key -> unique, immutable, cannot be None
value -> xperlu unique, cannot be None, can be mutable data

format
d = {}
d = dict()

print("--" * 40)

"""

d = {"name": "JK", 
     "age": 25, 
     "rollNo": 12345, 
     "weight":80.5,
     "subjects": ["Maths", "Science"],
     "address": {"Dno": 5213, "SName":"1st Cross", "City":"Cbe", "PinCode":"620014"}}

print(d)
print(d["name"])
print(d["address"]["City"])
print(d["subjects"][1])

print("--" * 40)

d["age"] = 27
print(d) 

# add new key
d["height"] = "5.7"
print(d)

# delete a key
del(d["weight"])
print(d)

print("--" * 40)

d = {1:"int", 
    2.4: "float",
    (21, 23): "tuple",
    "name": "str",
    2 +3j: "complex"}
    # [1,2,3]: "list"} # throw error, bcs list is mutable(unhashable), so we cannot make as key

print(d)

# to print only keys
print("Keys only")
for i in d:
    print(i)

# to print keys and values
print("Keys and values")
for i in d:
    print(i, d[i], sep="--")

print("--" * 40)

d = {12: "two",
    123:"three",
    1234: "four"}

print("Keys in sorted")
# but key must be same datatype, str, int
for i in sorted(d):
    print(i, d[i], sep="--")

print("--" * 40)

"""
# delete key and pass key using pop function 
print("Delete key 12")
d.pop(12)
print(d)

print("--" * 40)

# delete entire items in dict
print("Delete entire item in dict\n")
d.popitem()

# print(d[12]) # throw error

"""

print("--" * 40)

# make value in key 12 in a list
d[12] = [d[12]]
print(d)

# append new value in key 12
d[12].append("abc")
print(d)

#-----------------------------------------------------------------------------------------------------------------------------------------------#
# idesign
# 1.

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

#---------------------------------------------------------------------------------------------------------------------------------------
#2. 

# create a fx to pass a string and calculate count
def char_counts(s):

    # susun dlm ascending order
    s = sorted(s)
    # print(s)

    # create an empty dictionary to store our characters and its count
    char_count_dict = {}

    for char in s: # string is iterable object
        if char in char_count_dict: # kalau character dh ade dlm dict, then dia akn tmbh 1
            char_count_dict[char] +=1
        else:
            char_count_dict[char] = 1 # kalau belum ada, dia akn start with 1

    print(f"Dictionary of string:{char_count_dict}")

    for key, value in char_count_dict.items():
        print(f"{key}--{value}")


# example usage
string = input()
char_counts(string)

#----------------------------------------------------------------------------------------------------------------------------------------
# 3. 

num_of_students = int(input())

students = {}
for student in range(num_of_students):
    # first input masuk students, the rest masuk scores (thats why *)
    student, *scores = input().split()
    students[student] = list(map(int, scores))

# print(students)
chosen = input()

total = 0
count = 0
for key in students:
    if key == chosen:
        marks = students[key]
        for mark in marks:
            total +=mark
            count +=1
        average = total/count
    else:
        continue

print(f"Average Mark of is: {average:.2f}")

#----------------------------------------------------------------------------------------------------------------------------------------
# 4.

num_of_students = int(input("bagi no:"))

students = {}
for student in range(num_of_students):
    # first input masuk students, the rest masuk scores (thats why *)
    student, *scores = input().split()
    students[student] = list(map(int, scores))

chosen = input()

if chosen not in students: print("Student doesn't exist")
for key in students:
    if key == chosen:
        marks = students[key]
        if len(set(marks)) == 1:
            for i in set(marks): mark = i
            print(f"{key} scored same marks in all subjects: {mark}")
        else:
            max_mark = max(marks)
            marks.remove(max_mark)
            print(f"Second Highest mark of {key}:{max(marks)}")
    else:
        continue

#----------------------------------------------------------------------------------------------------------------------------------------------------

# 5.

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

""" 
1. input berapa element, list of numbers and position 
4. list of number convert to int 
5. set and sort them out in ascending order (sort jdi list balik)
6. nk calculate sum of numbers ikut position then append in a new list
7. 
"""

def generate_pin_number(num_elements, elements_str, k):

    elements = list(map(int, elements_str.split()))
    #print(elements)
    
    unique_element = sorted(set(elements))

    # print(unique_element)

    pin_number = []
    length = len(unique_element)
    i = 0

    while i < length:
        totalnum = sum(unique_element[i:i+k])

    

num_elements = 9
elements_str = input()
k = int(input())
generate_pin_number(num_elements, elements_str, k)

