
class Student:
  
    # usually init method is used to declare properties
    def __init__(self, firstname, lastname, icnumber): # kita create our properties assigned with empty value

        # condition for properties
        # 1. properties = varaibles but inside a class
        # 2. properties must always prefix with 1st parameter eg:
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = icnumber
        self.program = ""
        self.address = ""
        # if xdeclare prefix, the properties will only become local variable inside method
        # some of these properties are compulsary and we cannot create object tanpa value for these compulsary properties 
        # eg: u cannot create a student without having their firstname, lastnume and icnumber
        # however address and program can be provided late (not compulsary)



    def attendClass(self):
        print(f"{self.firstname} {self.lastname} is attending a class")

    # create 2nd method with 2 parameters
    def doProject(self, projectname):
        print(f"{self.firstname} {self.lastname} started doing the project:", projectname)

    # create 3rd method
    def attendExam(self, exam):
        grade = "A"
        print(f"""{self.firstname} {self.lastname} has attended the exam:\
{exam} and obtained the score {grade}""")
        

    def info(self):
        print("First name:", self.firstname)
        print("Last name:", self.lastname)
        print("Ic number:", self.icnumber)

        # here program is local variable created inside the method
        for program in self.program:
            print("Program:", program)
        print("Address:", self.address)
        print(self.address["Street"])
        print(self.address["Area"])
        print(self.address["State"])
    
    def __str__(self):
        return f"""First name: {self.firstname}\
    Last name: {self.lastname}\
    Ic number: {self.icnumber}"""
        # for program in self.program:
        #     print("Program:", program)
        # print("Address:", self.address)
        # print(self.address["Street"])
        # print(self.address["Area"])
        # print(self.address["State"])



# create our 1st object 
zul = Student("Zul", "Ahmad", "001001830")


# call the object with their methods
zul.attendClass()
zul.doProject("Pokemon")  
zul.attendExam("Python") 


# how can we set value for the properties
# 1. using constructor (__init__ method)
# 2. set directly using dot(.) operator
zul.program = ["Machine Learning", "Data Science", "Python"]
zul.address = {
    "Street": "jalan 41",
    "Area": "Bunga Cempaka",
    "State": "Kelantan"

}

zul.info()
# default bevahoiur is to print address location where the object is
# however if we want to "override" thta behaviour we can do that by
# creating a special method __str__

print(zul)
# when we try to print the object using print function
# if that class has __str__ method it will be executed automatically
