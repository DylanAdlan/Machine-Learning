# Polymorphism

class Gender:
    def __init__(self):
        pass
    def doCarryObjects(self):
        pass

class Male(Gender):
    def __init__(self):
        pass
    def doCarryObjects(self):
        print("Carry Heavy Objects")


class Female(Gender):
    def __init__(self):
        pass
    def doCarryObjects(self):
        print("Carry Light Objects")

def getGender(name):
    if "A/L" in name: # in operator can be used in string instead of just list
        return Male()
    else:
        return Female()
    
# for gender to hold Male() bcs at getGender fx pass condition A/L
gender = getGender("Khairi A/L Abu Bakar")
gender.doCarryObjects()

# for gender to hold Female() bcs xpass condition
gender = getGender("Aida A/P Abu Bakar")
gender.doCarryObjects()
print(type(gender))

#########################################################################################################################################
# TEST HOW FUNCTION CALL METHOD USING DOT OPERATOR
getGender("Farah A/P Fauzi").doCarryObjects()
Female().doCarryObjects()
Male().doCarryObjects()
