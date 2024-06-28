# principle = 1000
# period = 1
# rate = 6
# simpleInterest = (principle * period * rate) /100
# print(simpleInterest)

# def calculateSi(principle, period, rate):
#     simpleInterest = (principle * period * rate) /100
#     return simpleInterest

# # create a function that call another fx
# def calculateTotalAmountTobePrinted(principle, simpleInterest):
#     total = principle + simpleInterest
#     return total


# principle = 1000
# period = 1
# rate = 6
# result = calculateSi(principle, period, rate)
# newresult = calculateTotalAmountTobePrinted(principle, result)

# print("Simple interest:", result)
# print("Total to be paid:", newresult)

class Student:
    # bcs we cannot declare a property(variable) withpout value
    # kita create special method(function) called "Constructor" 
    # so kita bila call/execute  that method
    # bilamana nk create object
    # method = function inside a class
    # method will atleast 1 parameter
    # no need to pass argumrnt for 1st parameter
    def __init__(self):
        print("Object is created") # zul is the 1st object of student class 

    # create our 1st method/function 
    # method must have atleast 1 paramater
    # but no need to pass argument for first parameter
    def attendClass(self):
        print("Object is attending a class")

    # create 2nd method with 2 parameters
    def doProject(self, projectname):
        print("Object started doing the project:", projectname)

    # create 3rd method
    def attendExam(self, exam):
        grade = "A"
        print(f"Object has attended the exam: {exam} and obtained the score {grade}")


    # create our 1st object
zul = Student()
zul.attendClass()

# since this method have 2 parameters, then we need to pass argument for 2nd paramater
zul.doProject("Pokemon") # 1st parameter dont need argument # the 2nd argument = "Pokemon" 

zul.attendExam("Python") # pass argument "Python" to exam parameter 


