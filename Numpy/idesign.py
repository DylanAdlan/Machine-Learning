# idesign

# 1.
import numpy as np
import csv

with open("sample_data.csv", "r") as file:
    line = csv.reader(file)
    data = list(line)
    array = np.array(data)

print(array)

#------------------------------------------------------------------------------------------------#
# 1.

file_path = "sample_data.csv"

# Read data from CSV into Numpy array
data = np.genfromtext(file_path, delimiter=",", dtype=str)

print(data)

#-------------------------------------------------------------------------------------------------#

#2. 

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])


print("Array\n", arr)
print("Array type\n", str(type(arr)).replace("<","").replace(">",""))

#---------------------------------------------------------------------------------------------------#

# 3 .
import numpy as np

size = int(input("Enter the size of the list\n"))

listnum = []
print("Enter the elements in the list")
for _ in range(size):
    number = int(input())
    listnum.append(number)


a = np.array(listnum)
print(str(type(a)).replace("<","").replace(">",""))
print(a)

#----------------------------------------------------------------------------------------------------#

# 4.

# from sklearn.datasets module import load_iris function
from sklearn.datasets import load_iris

# load the iris dataset into dictionary-like object 
iris = load_iris()

# separate out the data part
data = iris.data

# print the top 3 rows from the data part
print(data[:3])

#------------------------------------------------------------------------------------------------------#

# 5.

import numpy as np

a = int(input("Enter the limit\n"))
b = int(input("Enter the number of points\n"))

arr = np.linspace(0, a, b)
print(arr)

#--------------------------------------------------------------------------------------------------------#

# 6. 

import numpy as np

num_rolls = int(input("Enter the number of dice rolls\n"))

listnum = []
print("Enter the value of each dice roll")
for _ in range(num_rolls):
    number = int(input())
    listnum.append(number)

dice_roll = np.array(listnum)

count_number_greater_than_2 = np.sum(dice_roll > 2)
print("Dice rolls greater than 2")
print(count_number_greater_than_2)   


#---------------------------------------------------------------------------------------------------------------#

# 6.

import numpy as np

size = int(input("Enter the size of 1-D array\n")) #6

# create a 1-D array using the range fx and convert to numpy array
one_d_array = np.array(range(size)) #[0,1,2,3,4,5]

print("1-D Array")
print(one_d_array)

m = int(input("Enter m value\n"))
n = int(input("Enter n value\n"))

two_d_array = one_d_array.reshape(m,n)
print("2-D Array")
print(two_d_array)

#--------------------------------------------------------------------------------------------------------------------#

# 7.

import numpy as np

first_array = int(input("Enter the size of 1st array\n"))

listnum1 = []
print("Enter the elements of first array")
for _ in range(first_array):
    number = float(input())
    listnum1.append(number)

second_array = int(input("Enter the size of 2nd array\n"))

listnum2 = []
print("Enter the elements of second array")
for _ in range(second_array):
    number = float(input())
    listnum2.append(number)

arr1 = np.array(listnum1)
arr2 = np.array(listnum2)

union_array = np.union1d(arr1, arr2)
intersection_array = np.intersect1d(arr1, arr2)
difference_array = np.setdiff1d(arr1, arr2)

print("Union Array")
print(union_array)
print("Intersection Array")
print(intersection_array)
print("Difference Array")
print(difference_array)

#--------------------------------------------------------------------------------------------------------------------------------------------------#

# iaccess
# 1.

import numpy as np

hundred_array = np.array(range(100)) 
print("Array 1")
print(hundred_array)

multiples_100 = np.arange(2000, 10000, 100)
print("Array 2")
print(multiples_100)

#---------------------------------------------------------------------------------------------------------------------------------------------------#

# 2.

from sklearn.datasets import load_iris

# load iris dataset
iris = load_iris()

# get feature names
feature_name = iris.feature_names

# get target names
target_name = iris.target_names

# get the first 5 rows of the iris data
first_five_data = iris.data[:5]

# get the first 5 rows of the iris target vector
first_five_target = iris.target[:5]

# print the result
print("Iris Feature Names")
print(feature_name)
print("Iris Target Names")
print(target_name)
print("Iris Feature Matrix")
print(first_five_data)
print("Iris Target Vector")
print(first_five_target)
print("Type of Iris Feature Matrix")
print(str(type(first_five_data)).replace("<","").replace(">",""))
print("Type of Iris Target Vector")
print(str(type(first_five_target)).replace("<","").replace(">",""))





































