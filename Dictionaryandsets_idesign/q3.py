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




