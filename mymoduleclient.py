# First method

# import mymodule # look at same folder and find for "mymodule" file
# # can access mymodule file and its code

# print("Interest:", mymodule.simpleInterest(1000, 1, 6))

# second method
# this method better bcs no need to type module name everytime
# also drawback if want to import > 1 fx
# we have to explicitly say it
from mymodule import simpleInterest, add
print("Interest:", simpleInterest(1000, 1,6))
print("Result:", add(3,4))


# third method
from mymodule import * # utk take all fx
# this way, all functions available
print("Interest:", simpleInterest(1000, 1,6))
print("Result:", add(3,4))
