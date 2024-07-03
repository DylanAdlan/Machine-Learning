# Is-A relationship
# Alumni is a student

# parent
class Student:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = ""

# child
# Alumni extends Student class
class Alumni(Student):


    # nk create new properties dlm Alumni class
    def __init__(self, firstname, lastname, alumninumber):
        # to create the parent object inside the child object
        # # you can use super class
        # which will return the object of parent class
        #Student.__init__(self,firstname, lastname, alumninumber) 
        super().__init__(firstname, lastname)       # parents punya attribute
        self.alumninumber = alumninumber
        

    # once created child, child kne follow properties parent

    # akan print out kalau kita print 
    def __str__(self):
        return f"First name: {self.firstname} \
        \nLast Name: {self.lastname} \
        \nIC number: {self.icnumber} \
        \nAlumni Number: {self.alumninumber}"


# we have create an object for alumni class
alumni = Alumni("Peter", "Parker", 6789) 
#alumni = Alumni() # keluar error sbb alumni is anak student and need to pass parameter sama mcm student
print(alumni)
# print(alumni.firstname)


