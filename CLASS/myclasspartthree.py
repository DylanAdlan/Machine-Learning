# encapsulation => bundling(gabungan) of data (attributes) and methods (functions) 
# that operate on the data into a single unit, usually a class.

# encapsulate the properties insode the calss
# dalam bahasa lain, keyword used= public / private / protected
# to protect the properties

class circle:

    def __init__(self, radius): # properties
        # self.radius = 
        if (isinstance (radius, int)): # check whether radius is type integer
            self.radius = radius # self.radius(property), radius (parameter)
        else:
            print("Invalid Radius")

    # METHODS

    def getRadius(self, radius): # to get the radius value
        return self.radius
    
    def setRadius(self, radius): # set the radius to the property 
        if (isinstance(radius, int)):
            self.radius = radius 
        else:
            print("Error 404")
    
    # property is a aclass
    # we are calling/ invoking the class by passing the method as argument
    # please notice after getRadius there is no()
    # the property class returns the property object whch is assigned to 
    # a variable radius
    # in other wprds radius is an instance of property class
    # radius = property(getRadius, setRadius)

    # calculate area of circle
    def area(self): #pai * (r^2)
        return 3.14 * (self.radius * self.radius)
    
    # calculate ukur lilit of circle 
    def circumference(self): #2*pai*r
        return 2 * 3.14 * self.radius
    
    def __str__(self):
        return f"Radius of the circle is {self.radius}"
    
    


mycircle = circle(20)
print(mycircle)
print(mycircle.area())
print(mycircle.circumference())

print("="*40)

radius = mycircle.setRadius(50) # kita set kan value untuk radius
print(mycircle)
print(mycircle.getRadius(radius)) # ambil value
print(mycircle.area())
print(mycircle.circumference())

print("="*40)

# mycircle.radius = 30
# print(mycircle)

#print(mycircle.setRadius())

# mycircle.radius = "abc" # to test if condition but cannot do the operation bcs in string
# print(mycircle)

# mycircle = circle("abc") # if user salah input, then we know what is wrong with our code
# print(mycircle)

# print(mycircle.area())

