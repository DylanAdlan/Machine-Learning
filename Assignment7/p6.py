'''
Syahmi solution 
Write a Python class that has two methods: getString and printString , 
The getString accept a string from the user and printString prints the string in upper case.
'''

class String:
    def _init_(self):
        self.input = ""
    
    def getString(self):
        self.input = input("Enter a string: ")
        return self.input
    
    def printString(self):
        return print((self.input).upper())
    
contoh = String()

print(contoh.getString())
contoh.printString()