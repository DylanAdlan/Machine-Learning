"""
video1 - modules

1) python program
2) functions, other objects, variables, classes
3) can be accessed by multiple programs by importing the module


import iClientmodules

print("Inside main")
a = b
b = 10
c = iClientmodules.sum_of_two_numbers(a,b)
print("sum =", c)

print(iClientmodules.person["address"])
print(iClientmodules.JKconstant)

====

# using mm as alias
import iClientmodules as mm

print("Inside main")
a = b
b = 10
c = mm.sum_of_two_numbers(a,b)
print("sum = ", c)

print(mm.person["address"])
print(mm.JKconstant)

=====

from iClientmodules import sum_of_two_numbers, person
from iClientmodules import * # import all functions, variables, and classes
print("Inside main")
a = b
b = 10

c = sum_of_two_numbers(a,b)

print("sum = ", c)

print(person["name"])

=====

from iClientmodules import *

radius = 5
area = area_of_circle(radius)
print(area)

video 2 - packages

1) collection of modules

package//mypackage//all files
package//mypackage & main file


__init__.py -> must put this file on the my package
---------------------------------------------------

inside my __init__.py

print("Inside MyPackage \n importing the modules")
import MyPackage.MyModule
import MyPackage.MultipleModule
import MyPackage.AreaCalculationModule
import MyPackage.PerimeterPackage
print("modules imported successfully")
 -----------------------------------------------------

inside Main.py

import MyPackage
import MyPackage.perimetercalculationmodule as per

print("Inside main program")
l = 10
b = 10
area = MyPackage.AreaCalculationModule.area_of_rectangle(l,b)
print("area = ", area)

peri = MyPackage.PerimeterPackage.rectPerimeterModule.perimeter_of_rect(l,b)
print("perimeter = ", peri)

if we add another package in mypackage. in the another package, we must add __init__.py
----------------------------------------------------------------

cd packages
inside __init__.py
print("importing perimeter package")
import MyPackage.PerimeterPackage.circlePerimeterModule
import MyPackage.perimeterPackage.rectPerimeterModule
print("perimeter package imported successfully")


=====
"""
# idesign
# 1. 

""" ---in mymodule file--
def fibonacci(x,y):
    xtemp = x+y
    x = y
    y = xtemp
    return xtemp

"""

from mymodule import fibonacci

size = int(input())
x = 0
y = 1
listnum = [0, 1]
for i in range(size-2):
    # fibonacci()
    # xtemp = x + y
    # x = y
    # y = xtemp
    listnum.append(fibonacci(x,y))

for i in listnum:
    print(i, end=" ")

#----------------------------------------------------------------------------------------------------------
# 2. 

from math import factorial

number = int(input())

factorial_num = factorial(number)
print(factorial_num)

#------------------------------------------------------------------------------------------------------------
# 3. 

size = int(input())

list_num = []
for i in range(size):
    number = int(input())
    list_num.append(number)

choose = int(input())

if choose in list_num:
    print("Got It!")
else:
    print("Sorry!")

#------------------------------------------------------
# 4

def count_string(string):
    words = string.lower().split()

    count_word = {}
    

    for i in sorted(words):
        if i in count_word:
            count_word[i] += 1
        else:
            count_word[i] = 1

    print("Enter the String")
    for word, count in count_word.items():
        print(f"{word}-{count}")

string = input()
# string = "mother father mother GST father GST facebook facebook GST"
count_string(string)   

#------------------------------------------------------------------------------------------------------------------
# 5

def gcd(a,b):

    while b!=0:
        a, b = b, a% b
    return a

print("Enter the two positive numbers")
num1 = int(input())
num2 = int(input())
print("GCD:",gcd(num1, num2))

#----------------------------------------------------------------------------------------------------------------------
# 6.

def findRepeat(string):

    count_word = {}
    for i in string:
        if i in count_word:
            count_word[i] +=1
        else:
            count_word[i] = 1

    for i in count_word:
        if count_word[i] == 1:
            # return first character yg xde repeating char
            return i
    
    # if non-repeating character, return #
    return "#"

string = input()
print(findRepeat(string))

#----------------------------------------------------------------------------------------------------------------------------------
#6 

def findMaxMin(number):
    number = list(map(int, number.split()))

    max_num = max(number)
    min_num = min(number)
    print("The maximum value is :",max_num)
    print("The minimum value is :",min_num)

number = input("Enter the values:\n")
findMaxMin(number)

#-----------------------------------------------------------------------------------------------------------
# 7
def convertnumtoAscii():
    value = int(input("Enter the value :\n"))

    ascii_value = chr(value)
    print(f"Character of ASCII value {value} is  {ascii_value}")


# example usage
convertnumtoAscii()


#--------------------------------------------------------------------------------------------------------------

# iaccess 1

def decodeString(string, wordsplit):
    sentence = string.split(wordsplit)

    print("Strings after splitting")
    for word in sentence:
        # using capitalize function to capital first char
        print(word.capitalize())


sentence = input()
wordsplit = input()
decodeString(sentence, wordsplit)

#------------------------------------------------------------------------------------------------------------------

# iaccess 2
import math

def PrimeNum(number):

    prime = []
    
    for i in range(2, number + 1):
        isPrime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                isPrime = False
                break
        
        if isPrime:
            prime.append(i)

    return prime

def SumNum(number, times):

    primes = PrimeNum(number)
    sum_num = sum(primes)

    for i in range(times -1):
        primes = PrimeNum(sum_num)
        sum_num = sum(primes)
    
    print("Sum:", sum_num)

# example usage
max_num = int(input())
times = int(input())
SumNum(max_num, times)



            
            

