# methods are nothing but fx inside the class
# methods take atleast 1 parameter (self)
# This parameter is used by python to pass the instance

class Calculator:

    # since this method take self as parameter (instance argument)
    # this method also called as instance method
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def add(self):
        return self.x + self.y
    
    def subtract(self):
        return self.x - self.y
    
mycalculator = Calculator(3,4)
print(mycalculator.add())
print(mycalculator.subtract())

#####################################################################

# there is a class which has many methods but no properties
# why methods take self as a parameter ? bcs we want to access the properties
# # which means the methods no need to take self as parameter anymore
# # since there is no property thwn we cannot create Objects
# these types of methods attached to the class not objects
# they are called class methods

class Utility:

    def addition(x,y):
        return x + y

    def subtraction(x,y):
        return x-y

print(Utility.addition(10, 10)) 

# however this can be done using module in pyhton
# no need to create class

####################################################################################################

# there are some use cases where class has properties
# but ada methods inside class yg xnk access the properties 
# those methods can be created without self parameter
# they called as class methods

class Customer:
    # instance method
    def __init__(self, fn, ln):
        self.fn = fn
        self.ln = ln

    # class method bcs dont take self as parameter
    def getFullname(fn, ln):
        return fn + ln
    
    def __str__(self):
        return Customer.getFullname(self.fn, self.ln)
    
myCustomer = Customer("John", "David")
print(myCustomer)

###################################################################

def Odd(a, b):
    if a & 1 and b &1:
        print("Both are Odd")
    elif(a&1):
        print("%d is Odd"%(a))
    elif(b&1):
        print("%d is Odd"%(b))

Odd(3, 4)