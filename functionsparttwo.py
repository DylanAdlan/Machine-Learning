# fx can have inner fx

# Outer function
def authenticate(username, password):
    # inner function 
    def calculateSI(principle, period, rate):
        # def something():
        #     pass
        # something()
        result = (principle * period * rate) /100
        return result
    if username == "admin" and password == "pwd123":
        # since calculateSI fx is inside authenticate fx,
        # then we can call this fx here
        calculateSI(1000, 1, 6)
        # we also can return inner fx here
        return calculateSI


# can call this function
authenticate("admin", "pwd123")

# # cannot call inner fx outside outer function 
# calculateSI(1000, 1, 6) # so cannot do this

# but if the outer fx return inner fx
# then we can call inner fx
func = authenticate("admin", "pwd123")
print("Simple Interest:", func(1000, 1, 6))

# we can also write it like this
print("Simple Interest:", authenticate("admin", "pwd123")(1000, 1, 6))


# Anonymous fx => fx without name
# but how to call fx if no name
# example:
# sum = def (a,b):
#     return a + b
# dia xvalid but this is how python handled every fx
# in python every fx is an annonymous fx

# create fx just in 1 line
# def (a,b): return a+b
# sum = def (a, b): return a + b
# we dont create like this
# instead we use lambda
add = lambda a,b : a+b

fahrenheitvalues = [32,33,34,35]
def fahrenheitToCelcius(fahrenheitvalue):
    return (fahrenheitvalue -32) * 5/9

celciusvalues = map(fahrenheitToCelcius, fahrenheitvalues)
print(list(celciusvalues))

# using lambda fx
# step 1: create annonymous function
# def(fahrenheitvalue) : return (fahrenheit -32) * 5/9
# step 2: ssign it to variable
# fahrenheitToCelcius = def(fahrenheitvalue) : return (fahrenheit -32) * 5/9
# step 3: rename def to lambda
# fahrenheitToCelcius = lambda (fahrenheitvalue) : return (fahrenheit -32) * 5/9
# step 4: remove () at parameter and return keyword
# fahrenheitToCelcius = lambda fahrenheitvalue :  (fahrenheit -32) * 5/9


celciusvalues = map(fahrenheitToCelcius, lambda value: (value-32)* 5/9)
print(list(celciusvalues))