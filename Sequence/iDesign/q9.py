# Create an empty dictionary
# my_dict = {}


number = int(input("Num of students: "))

# create empty list to store each student and their marks
students_marks = []
for i in range(number):
    # input many values in a variable
    student_mark = input() 
    # need to separate them by space and tuple them together
    student_mark = student_mark.split()
    # insert the value into list
    students_marks.append(student_mark)

# input nama student yg nk tgk secong highest result
name = input()

# print(students_marks)

student_dict = {}
for i in range(len(students_marks)):
    key = students_marks[i][0]
    values = students_marks[i][1:]
    my_dict = {key: values}
    print(my_dict)
    # store the key and values inside dictionary
    student_dict.update(my_dict) 

print(student_dict)

for key in student_dict.keys():
    if key == name:
        # get the values of specified key 
        marks = student_dict.get(name)
        int_mark = list(map(int, marks))
        print(int_mark)

        
        # for mark in marks:
        #     if 








