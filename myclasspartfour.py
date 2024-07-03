# Has_A relationship
# Customer has a passport


class Passport:

    def __init__(self, country, passportnumber):
        self.country = country
        self.passportnumber = passportnumber


    def __str__(self):
        return f"Country: {self.country} \nPassport NUmber: {self.passportnumber}"

class Customer:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = "" # number only
        self.passport = None # string + number

    def __str__(self):
        message = f"First name: {self.firstname} \n"
        message = message + f"LastName: {self.lastname} \n"
        message = message + f"LastName: {self.lastname} \n"
        message = message + f"IC Number: {self.icnumber} \n"
        if (self.passport != None):
            message = message + self.passport.__str__()

        return message
    


adnin = Customer("Adnin", "Adlan")
passport = Passport("UK", "E02343")
adnin.passport = passport  # passport dalam customer("adnin")
print(adnin)
print(passport)

# convert python object to dictionary
print(adnin.__dict__)
# print(adnin.passport())