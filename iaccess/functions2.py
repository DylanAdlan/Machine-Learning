def multiVarFunc():
    dept_name = input("Enter department name:\n")
    total_student = int(input("Enter the number of total students:\n"))
    total_faculty = int(input("Enter the number of total faculties:\n"))

    return dept_name, total_student, total_faculty

# example usage
dept_name, total_student, total_faculty = multiVarFunc()
print(f"Details\nDepartment:{dept_name}\nTotal students:{total_student}\nTotal faculties:{total_faculty}")
