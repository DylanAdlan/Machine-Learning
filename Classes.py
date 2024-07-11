"""
iexplore

1.
class test:
    def __init__(self,a="Hello World"):
        self.a=a
    def display(self):
        print(self.a) 

obj=test("Hello")
obj.display()

output: Hello

2.
getattr() used for 
- To access the attribute of the object

3.
class test:
    def __init__(self):
           self.variable = 'Old'
           self.Change(self.variable)
    def Change(self, var):
          var = 'New'
obj=test()
print(obj.variable)

output = "Old"

4.
setattr() used for
- To set or change the value of an attribute of object

5.
_____ is used to create an object.
- constructor which always named as __init__ method

6.
class change:
    def __init__(self, x, y, z):
    self.a = x + y + z 

x = change(1,2,3) # x.a = 6
y = getattr(x, 'a') # y = x.a = 6
setattr(x, 'a', y+1) # x.a = 6 + 1
print(x.a) # 7

output = 7

7.
class test:
    def __init__(self,a):
        self.a=a
    def display(self):
        print(self.a)

obj=test()
obj.display()

output = test.__init__() missing 1 required positional argument: 'a'

8.
_____ represents an entity in the real world with its identity and behaviour.
- object

9.
What is Instantiation in terms of OOP terminology?
- Creating an instance of class

10.
class fruits:
    def __init__(self, price):
        self.price = price

obj=fruits(50)
obj.quantity=10
obj.bags=2
print(obj.quantity+len(obj.__dict__)) 
# len(obj.__dict__) ->returns the number of attributes in this dictionary. ( price, quantity, bags = 3)

output = 10+3 = 13

ianalyse

1.
 Private members of a class cannot be accessed
- False

2.
class student:
    def __init__(self):
        self.marks = 97
        self.__cgpa = 8.7
    def display(self):
        print(self.marks)

obj=student()
print(obj._student__cgpa)

output = 8.7
(The program runs fine and 8.7 is printed)

3.
Which of these is a private data field?
class Demo:
    def __init__(self):
        __a = 1
        self.__b = 1   <==
        self.__c__ = 1
        __d__= 1

output = __b

4.
definition for encapsulation
- Means of bundling instance variables and methods in order 
to restrict access to certain class members

5.
false about protected class members
- They can be accessed by name mangling method (intended to be a private to the class)

6.
cth soalan:
class MyClass:
    def __init__(self, value):
        self.__value = value  # Name mangling will occur here

    def get_value(self): 
        return self.__value


# Create an instance of MyClass
obj = MyClass(10)

# Accessing the attribute directly will result in an AttributeError
# print(obj.__value)  # This will raise an AttributeError

# Accessing the attribute using the name mangled version
print(obj._MyClass__value)  # Output: 10

# Accessing via a method
print(obj.get_value())  # Output: 10

real question: 

class Demo:
    def __init__(self):
        self.a = 1
        self.__b = 1
    def get(self):
        return self.__b

obj = Demo()
print(obj.get()) <== access method, so blh run

output =  1

7.
class objects:
    def __init__(self):
        self.colour = None
        self._shape = "Circle"  <==
    def display(self, s):
        self._shape = s

obj=objects()
print(obj._objects_shape) # Error because the member shape is a protected member
print(obj.__shape) # Circle

# NAME MANGLING
eg: 

class fruits:
    def __init__(self, price):
        self.__price = price  # Name mangling will occur here

obj = fruits(50)
obj.__quantity = 10  # This will be accessible directly since it's not mangled
obj.__bags = 2  # This will be accessible directly since it's not mangled

# Access the attributes using name mangling
print(obj._fruits__price)  # Output: 50

8.
The purpose of name mangling is to avoid unintentional access of private class members. 
- True

9.
class Demo:
    def __init__(self):
        self.a = 1
        self.__b = 1
    def get(self):
        return self.__b

obj = Demo()
obj.a=45 <== Modify the public attribute 'a'
print(obj.a) # 45

output = 45

10.
Methods of a class that provide access to private members of the class are called as ______ and ______
- getters/setters


"""
# idesign
# 1.

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}\n{self.age}"
    
# from Person import Person

#Fill your code

name = input("Enter name\n")
age = int(input("Enter age\n"))

print("Person Details")
ppl = Person(name, age)
print(ppl)
    

#------------------------------------------------------------------------------------------------------------

# 2.

class Person:
	def __init__(self,name, age):
		self.__name = name
		self.__age = age
		
	@classmethod # decorator
	def from_string(cls, person_str): # class method
		name, age = person_str.split(",")
		return cls(name, int(age))
		
	def __str__(self):
		return f"{self.__name} is {self.__age} years old"

# from Person import Person

print("Creating object using __init__ method")
person_name = input("Enter name\n")
person_age = input("Enter age\n")
person1 = Person(person_name, person_age)
print("Person Details")
print(person1)
print("\n")

print("Creating object using class method")
person_str = input("Enter name and age in comma separated format\n")
person2 = Person.from_string(person_str)
print("Person Details")
print(person2)

#----------------------------------------------------------------------------------------------------------------------

#3.

class Address:
	def __init__(self, street, city, state):
		self.__street = street
		self.__city = city
		self.__state = state
	def __str__(self):
		return f"{self.__street}, {self.__city}, {self.__state}"
	
class Person:
	
    def __init__(self, name, age, address):
        self.__name = name
        self.__age = age
        self.__address = address
	
    def __str__(self):
	    return f"{self.__name} is a person who is {self.__age} years old and lives in the following : {self.__address}"
	
# Input for creating Person and Address objects
name = input("Enter name\n")
age = int(input("Enter age\n"))
print("Enter address")
street = input("Enter street\n")
city = input("Enter city\n")
state = input("Enter state\n")

# Create Address object
address = Address(street, city, state)

# Create Person object
person = Person(name, age, address)

# Print Person details
print("Person Details")
print(person)

		
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#4.

class City:
	
    def __init__(self, name, state):
        self.__name = name
        self.__state = state
		
    def __str__(self):
		return f"{self.__name},{self.__state}"
	
class State:
	def __init__(self, name, city_list):
		self.__name = name
		self.__citylist = city_list
		
    def __str__(self):
        

print("Enter City Details")
city = input("Enter city name\n")
state = input("Enter state name\n")
choice = 
city_detail1 = City(city, state)
state_detail = State(name, city_detail1)

	
		
	


		
		

	
	






