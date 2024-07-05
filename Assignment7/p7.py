"""
Write a Python class Employee
properties = id, name, salary, and department 
methods = _init_ calculateSalary, assignDepartment and _str_.

"""

class Employee:

    def __init__(self, id, name, salary, department):
        self.id = id
        self.name = name
        self.salary = salary
        self.dept = department

    def calculateSalary(self):
        self.hours = int(input("Number of hours worked: "))
        if self.hours > 50:
            self.hours -= 50
            overtimeAmount = self.hours * (self.salary / 50)
            totalSalary = self.salary + overtimeAmount
            return f"Total salary for {self.name} is RM{totalSalary:.2f}"
        else:
            return f"Total salary for {self.name} is RM{self.salary * self.hours}"


    def assignDepartment(self, department):
        self.dept = department

    def __str__(self):
        return f"{self.id} {self.name} {self.salary} {self.dept}"
    
    
#example usage
adams = Employee("E7876", "ADAMS", 50000, "ACCOUNTING")
jones = Employee("E7499", "JONES", 4500, "RESEARCH")

print(adams)
print(jones)

adams.assignDepartment("RESEARCH")
print(adams)

print(adams.calculateSalary())