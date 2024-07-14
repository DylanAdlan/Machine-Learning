def kucing(x,y): # function
    total = x + y
    return total

x = 2
y = 2
kucing0 = x + y # variable
kcg = "wdadadw"

# print(kucing(2,2)) # panggil function
# print(kucing0) # panggil variable

######################################

# x = input("Enter a string")
# print(x)
# #---------------------------------------------
# def cth(y):
#     print(y)

# statement = input("enter something")
# cth(statement)
# #------------------------------------------------
# def cth1():
#     inputstr = input("Enter a string: ")
#     print(inputstr)
# cth1()

#--------------------------------------------------

def tolak():
    i = int(input("Enter i: "))
    j = 2
    return i - j
def tambah(x,y): 
    return x + y

def kira(x,y):
    nilai = tambah(x,2) * tolak()
    return nilai


# a = int(input("Enter value a: "))
# b = int(input("Enter value b: "))
# print(kira(a,b))

#-----------------------------------

class Student:
    def __init__(self,name,tahun):
        self.namastudent = name # self.namastudent pegang value dari luar utk guna dalam kelas
        self.tahunstudent = tahun
    
    def printnama(self): # Method
        # print(self.namastudent)
        return self.namastudent
    
    def kucing(self):
        umur = 2024 - self.tahunstudent
        return umur
    
    def __str__(self):
        return f"IEG Student {self.namastudent}"
    
    
student = Student("Adnin",2000)
print(student.printnama()) # cara panggil method
# print(student.namastudent) # cara panggil properties
# print(student)
# print(student.kucing())












class kirakira:
    def __init__(self,x,y):
        self.nilaix = x
        self.nilaiy = y
    
    def tambah(self):
        return self.nilaix + self.nilaiy
    
    def tolak(self):
        return self.nilaix - self.nilaiy
    
    def special(self):
        return self.tolak() * self.tambah()

answer = kirakira(2,3)