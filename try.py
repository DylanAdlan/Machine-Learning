# raise error

# USING BUILT IN ERROR
class Rank:

    def __init__(self, classroom, rank):
        self.classroom = classroom
        self.rank = rank

    def __repr__(self):
        return f"<Car {self.classroom} {self.rank}>"


class Student:

    def __init__(self):
        self.name = []
        pass

    def __len__(self):
        return len(self.name)
     
    def add_name(self, name):
        if not isinstance(name, Rank):
            raise TypeError("Tried to to add {name.__class__.__name}")
        self.name.append(name)

adnin = Student()
adnin.add_name("Adnin")
print(len(adnin))

########################################################################################################
 
# CREATE CUSTOM ERROR
# create our our customer error (xleh pakai nama error sama macm built in error) from built in error

class MyCustomError(TypeError): 
    # TypeError is superclass. MyCustomError is subclass
    
    def __init__(self, message, code):
        super().__init__(f"Error code {code}: {message}") # message is parent attribute
        self.code = code # child own attribute

raise MyCustomError("OUCH, Whats happening", 500)

#######################################################################################################

class RunTimeErrorwithcode(TypeError): 
    # TypeError is superclass. MyCustomError is subclass
    """
    Exception is raised 
    
    """
    
    def __init__(self, message, code):
        super().__init__(f"Error code {code}: {message}") # message is parent attribute
        self.code = code # child own attribute

err = RunTimeErrorwithcode("OUCH, Whats happening", 500)
print(err.__doc__) # print out message dalam """ """