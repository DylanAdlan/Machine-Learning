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
