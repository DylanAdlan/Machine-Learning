# in every class there will be many properties
# and very few properties are common to all the objects
# its good to keep these properties at the class level
# rather than keep at the object (instance) level

class Participant:
    # assuming all these participants are going to take 
    # ome particular program "Python Data Science /ML"
    # class variables are inside the class but outside the methods
    # class variable will be destroyed when the class is destroyed
    # to access 
    course = "Python Data Science /Machine Learning "

    def __init__(self, firstname, lastname):
        # the following properties will be created at the 
        # obejct level. in other words every object being
        # cretaed will allocate space to keep these values
        self.firstname = firstname
        self.lastname = lastname
        count = 1
        print(self.firstname, self.lastname, count)
        # inside the methods we can have 2 types of variables
        # 1. Instance variables prefix with the word self
        # instance variable live until thr object is destroyed
        # 2. Local variable not prefixed with the word self
        # local variable will die after the method execution
        # local variable created inside the class but outside the methods

    def getFullName(self):
        print(self.firstname, self.lastname)

khairi = Participant("Khairi", "Abu Bakar")
# when will the firstname, lastname destroy from memory
# when you destro Khairi firstname, lastname will be destroyed
# del khairi

#when u want to access the instance variable u must prefix 
# with object
print(khairi.firstname)

#when u want to access the class variable u must prefix 
# with object
print(Participant.course)