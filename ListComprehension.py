'''
new_list = [expression for item in iterable if condition]

'''

# simple list comprehension (finding squares number)
numbers = [1,2,3,4,5]
squares = [number**2 for number in numbers]
print(squares)

#list comprehension with condition (find even number)
numbers = [1,2,3,4,5,6,7,8]
even = [n for n in numbers if n%2==0]
print(even)

# nested loops in list comprehension 
nested_list = [[1,2,3], [4,5,6], [7,8,9]]
flat_list = [item for sub_list in nested_list for item in sub_list]
print(flat_list)

# using function in list comprehension
def square(x):
    return x*x

numbers = [1,2,3,4,5,6]
squares = [square(n) for n in numbers]
print(squares)


# iterate through multiple lists
tuple_number = [(x,y) for x in [1,2,3] for y in [2,3,4] if x!=y]
print(tuple_number)

# calculate pi values in differ decimal points
from math import pi

pi_round = [str(round(pi, i)) for i in range(1,6)]
print(pi_round)


def printinfo(name, age= 30):
    print("Name", name)
    print("Age", age)
    return

printinfo(age = 20, name = "Adnin")
printinfo(name = "Adnin") # bcs no value passed for age, it will take defualt value yg dh assigned

def sum (message, *mynumbers):
    total = 0
    for number in mynumbers:
        total +=number

    return message + " " + str(total)

print(sum("Total: ", 10, 20, 30))


def intro(**data):
    for key, value in data.items():
        print(f"{key} is {value}")
        # print("{} is {}".format(key, value)) sama macm atas


intro(Firstname = "Adnin", Lastname = "Adlan", Age = 22)
intro(Firstname = "Farah", Lastname = "Fauzi", Age = 22)

# assign functions to a variable
def greet(name):
    return "Hello " + name

greet_someone = greet # assign function to a variable
print(greet_someone("Adnin"))


#----pass a function--------

def greet(name):
    return "Hello " + name

def call_greet(func):
    other_name = "adnin"
    return func(other_name)

# example usage
print(call_greet(greet)) # calling a function by passing another function

#----------function can be returned----------------\

def compose_greet_func():

    def get_message():
        return "Good Morning!"
    
    return get_message() # retrun a function

#example usage
print(compose_greet_func())

#------another example------------

def compose_greet_func(name):
    name = name
    name1 = "Adnin"

    def get_message():
        return "Good Morning " + name + "!"
    
    return get_message() # return a function

#example usage
print(compose_greet_func("Aida"))

#---------lambda function---------------\

'''
can take any numbers of arguments but only return one value
'''

#--------ex1-------(simple lambda)

double = lambda x: x * 2
print(double(5))

#-----using filter functionin lambda---take what's TRUE!

mylist = [1,2,3,4,5,6,7,8]

'''
filter(function, iterable) # ambik yg True
lambda x: (x%2==0) => function
mylist => iterable
'''
newlist = list(filter(lambda x: (x%2==0), mylist))
'''filter akn ambik value yg blh dibahagi dgn 2'''
print(newlist)

#----------using map function in lambda-----apply the function to every item in iterable and returns an iterator\
newlist = list(map(lambda x: (x%2==0), mylist))
'''filter akn ambik value yg blh dibahagi dgn 2'''
print(newlist)

newlist = list(map(lambda x: x*2, mylist))
'''filter akn ambik value yg blh dibahagi dgn 2'''
print(newlist)

#----------using lambda in function---------

def multiplier(n):
    return lambda x: x * n

mydoubler = multiplier(2)
print(mydoubler(11))

#---------using reduce function in lambda-----\
# kena import library (from functools import reduce)
# module - single file contain pyhton code
# library - collection of modules and packages

#-------------% operator-----------\
''' % operator = format a set of variables in a tuple'''
''' %s = string, %d = integers, %f= float'''

#example usage
name = 'Adnin'
print("Hello, %s" % name)

number = 13
print("The number given is %f" %number)

#------------------------------------------------------

# number after : represent spaces
print("Art:{0:4d}, Price:{1:6.2f}".format(453, 59.058))

# > to left
print("{0:>20s}".format('Spam & Eggs'))

# center
print("{0:^20s}".format('Spam & Eggs'))

print("{0:$^20s}".format('Spam & Eggs'))

#----------------------------------------------

x = -378
print("The value is {:06d}".format(x))

x = -998.8
print("The value is {:,}".format(x))

print("The value is {:6,.3f}".format(x))

print('C:\some\name')

print('''Heloo
      my 
      name
       is
      Adnin''')

names = ['Adnin', 'Farah', 'Asyful', 'Asyful', 'Syahmi']
names2 = names.copy()
print(names2)

asyful = names.count('Asyful')
print(asyful)

names2.insert(2, "Syu") # insert take 2 argument, index n value yg nk tmbh
print(names)
print(names2)

names2.append("Akmal")

names2.remove("Asyful") # remove direct value
print(names2)

names2.pop(1) # delete index
print(names2)

# del names2 # delete the variable
del names2[0]
print(names2)

fruit = {'orange', 'mango'}
fruit.clear()
print(fruit)

# del fruit
# print(fruit)

class Person:
    first_name = ""

    def set_first_name(self):
        self.first_name = "Instance First Name"
    
    def modify_first_name():
        Person.first_name = "Class variable First Name"

print(Person.first_name)

Person.modify_first_name()
print(Person.first_name)

person = Person()
person.set_first_name()
print(person.first_name)


class Product:

    def add_price(self):
        self.price = self.price * 5

# exmple usage
product = Product()
print(product.add_price)


names = ['adnin', 'naqib', 'ain']

name = iter(names)
print(name)