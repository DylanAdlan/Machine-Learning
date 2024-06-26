# when we can access this variable?
def add (a,b):
    # result is local variable => created inside a function
    # result cannot be access outside of the function
    result = a + b
    return result

#print(result) # cannot access

# the above discussion is called scope of variable

######################################################################################################################################

# now we are at main context called as global context
x = 10
# variable x is cretaed at the main context
def printX():
    # blh access x variable
    print("Inside the function(printX):", x)

printX() # call the printX function
print(x)

def modifyX():
    # we want to modify the value of variable x
    # the moment we try to modify a variable inside the fx
    # the variable created immediately at the localcontext(inside the modifyX function)
    # does not refer to global context
    x = 15
    print("Inside the function(modifyX):", x)

modifyX()  # call modifyX function
print(x)

# if nk create fx yg bh modify variable at global context
# then the fx must return the value
def traditionalModifyX():
    x= 15
    return x

x = traditionalModifyX()
print(x)
# proper programming recommendation

# however this way, we can only return single value
# then we also have shortcut for this to return more values
def pythonModifyX():
    global x  # telling python create variable globally
    x = 25
    print("Inside the function(pythonModifyX):", x)

pythonModifyX()
print(x) # this x variable changed 


#################################################################################################################################

def simpleInterest(principle, period, rate): # outer fx
    result = 0
    def printSimpleInterest(): # inner fx
        nonlocal result
        # dont create local variable when modifying the value of outer variable
        # in other words, we can modify the variable that in outer fx
        temp = 0 # variable created inside inner fx
        print("Simple Interest:", result) # however inner fx can access the
        # variable which is in the outer fx
        print("Principle:", principle) # inner fx can access parameter of outer fx
        print("Rate:", rate)
        # can i modify the variable result
        result = result + 50
    #print(temp) # this is not allowed
    result = (principle * period * rate) / 100
    printSimpleInterest()
    print(result)


simpleInterest(1000, 1,6)
# Summary
# global keyword allows the fx to modify the variable which is 
# in the global context
# local keyword allows the fx to modify the variable which is
# in the outer function context

fruit = "apple" 
def myfunction():
    fruit = ""
    print(fruit) # this refer to local variable, so error bcs we initialize after the print
    fruit = "orange"

myfunction()