# multiple inheritance

class Card:
    def __init__(self):
        pass
    def doSomething(self):
        print("Inside Card Class")

class AtmCard(Card):

    def __init__(self):
        pass
    def doSomething(self):
        print("Inside AtmCard Class")

class CreditCard(Card):

    def __init__(self):
        pass
    def doSomething(self):
        print("Inside CreditCard Class")

class DebitCard(Card):

    def __init__(self):
        pass
    def doSomething(self):
        print("Inside DebitCard Class")

class BankCard(AtmCard, CreditCard, DebitCard):

    def __init__(self):
        pass
    def doSomething(self):
        print("Inside BankCard Class")
        super().doSomething() # 

# we have created 5 classes
# and in all 5 classes we have doSomething method
# and it is implemented (got code inside which is "print")

# let us create instance of the last card
bankCard = BankCard()
bankCard.doSomething()
# now remove the print statement from bankcard.doSomthing
# and call the super().doSomething
# this time u will see "Inside AtmCard Class" 
# which is the 1st inherited class

# comment doSomething method AtmCard class

# comment doSomething method CreditCard class

# comment doSomething method DebitCard class

# Conclusion: pyhton scan from left to right and identify
# the base ckasses
# and call the methods according;y
# this process called Method Resolution Order (MRO)
print(BankCard.__mro__)

# <class '__main__.BankCard'>, 
#  <class '__main__.AtmCard'>, 
#  <class '__main__.CreditCard'>, 
#  <class '__main__.DebitCard'>, 
#  <class '__main__.Card'>, 
#  <class 'object'>

# BIGGEST CONCLUSION
# Every class we create in python inherited from a class
# called object
# class object:

#     def __init__(self):
#         pass
#     def __str__():
#         print(memory address)
 

class Student:
    def __str__(self):
        return "Student"

class Alumni(Student):
    def __str__(self):
        return "Alumni"

alumni = Alumni() 
print(alumni)
# just print "Alumni" bcs override

#########################################################################################################################
# PRINT ADDRESS LOCATION

# class Student(object):
#     pass
# print(Student()) 

########################################################################################################################
# PRINT HELLO
class object:

    def __str__(self):
        return ("Hello")
    
print(object())

########################################################################################################################

# iterator object like enumerator, range, map, filter do not override the method __str__
# howver those classes are inherited from default python class
# called object which has the method __str__ which
# returns the address location of the object
# finally that gets printed using the print fx
class object:
    def __str__(self):
        return "address"

##########################################################################################################################

# HAS PARENT
# RANGE CLASS INHERITED FROM OBJECT CLASS
class range(object): #object is the parent class
    pass

myrange = range()
print(myrange)

#############################################################################################################################

# HAS NO PARENT 
class range: # no parent class and no return then it'll print out address location
    pass

myrange = range()
print(myrange)

#############################################################################################################
# what if i dont want my class to inherit from base class called object
# definitely u dont want this bcs
# u will loose all default feature of a class

# class myClass:
#     pass
# student = myClass().__init__

# myClass(). will list more methods
# now we understand those methods are coming the base class called object

# class noObjectClass():
#     pass

# test = noObjectClass()
# print(test)