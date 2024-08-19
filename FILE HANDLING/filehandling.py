
# input/output data xsimpan dlm hard disk so everytime kita
# execute code, dia akn keep on sruh kita input and output data baru but xsave dlm hard disk
# so kita msti create data and save them kita inside the program
# mestila kna ade code utk read that file
# by creating a txt file / csv file / excel file

# nk create file
# use open keyword
# open('fruits.txt')

# kalau file belum exist, then kita give instruction to python
# extra instruction as mode
# Mode
# 1. x akn create the file if file belum exist lagi
# 2. t = represent text file
# 3. b = represent binary file yg hnya computer blh read
# 4. w = write inside the file.tpi akn clear the existing content in 
#        that file and write a new content # not necessary use this !
# 5. 
############################################################################################################
# CREATE NEW FILE

# (x) create fruits file in text file (t)
# open('fruits.txt', 'xt')
#
#################################################
# import os module (utk file)
# import os # xyah guna cara ini
from os.path import exists

def keyboardInput(datatype, caption, errorMessage, defaultValue = None):
    value = None
    isInvalid = True
    while(isInvalid):
        try:
            if defaultValue == None:
                # take caption as parameter sbb kita ade byk input from user
                value = datatype(input(caption))
            else:
                value = input(caption)
                if(value.strip() == ""):
                    value = defaultValue
                else:
                    value = datatype(value)
        except:
            print(errorMessage)
        else:
            isInvalid = False

    return value

def doMenu(filename):
    choice = -1
    while (choice!=0):
        print("--------------")
        print("| 0 - Exit   |")
        print("| 1 - List   |")
        print("| 2 - Add    |")
        print("| 3 - Edit   |")
        print("| 4 - Delete |")
        print("--------------")
        choice = keyboardInput(int, "Choice [0,1,2,3]: ", "Choice Must be Integer")
        if (choice == 0):
            print("Thank you for using this system")
            break
        elif(choice == 1 ):
            printProduct(filename)
        elif(choice == 2):
            addProduct(filename)
        elif(choice == 3):
            editProduct(filename)
        elif(choice == 4):
            deleteProduct(filename)
# kalau file x exist
# then kita create new file

# nk check if that file is exist or not

# create a fx by passing a filename
def createFile(filename): 

    # kalau file x exist
    if not exists(filename):
        try:
            # the open built in fx open the file and return the handler
            # which we can read/write inseide the file
            # filehandler is an object/ instance of File class

            # dia akn create file in text file by "filename" name
            filehandler = open(filename, 'xt')
        except Exception as f: 
            print("Something went wrong when we create the file", f)
        else:
            createTitle(filename)
        finally:
            # filehandler is an object 
            filehandler.close()
            # open(filename, 'xt').close()


def createTitle(filename):
    try:
        with open(filename, 'wt') as filehandler:
            # here | (pipe) is used as delimiter
            # delimiter = split the line into multiple data
            filehandler.write("Product| Quantity|Price")
    except Exception as e:
        print("Something went wrong when we create the header:", e)

# ADD PRODUCT
def addProduct(filename):
    try:
        product = keyboardInput(str, "Product: ", "Product must be in string")
        quantity = keyboardInput(int, "Quantity:", "Quantity must be in integer" ) #int
        price = keyboardInput(float, "Price:", "Price must be in float" ) #float
        with open(filename, "at") as filehandler:
            filehandler.write(f"\n{product}|{quantity}|{price}")

            # filehandler.write(f"\n{product:40}{quantity:20}{price:20}")
    except Exception as e:
        print("Something went wrong when we append the product")

# PRINT PRODUCT
def printProduct(filename):
    try:
        lines =None
        with open(filename, "rt") as filehandler:
            # read all lines 
            lines = filehandler.readlines()
        for index, line in enumerate(lines):
            product, quantity, price = line.strip().split("|")# strip method remove the last \n (new line) & remove spaces
            if (index == 0):
                print(f"{"No.":5}{product:40} {quantity:>20} {price:>20}")
                print("=" * 80)
            else:
                print(f"{index:<5}{product:40}{int(quantity):>20}{float(price):>20.2f}")
    except Exception as e: 
        print("Something went wrong when we print the products:", e)


# EDIT PRODUCT
def editProduct(filename):
    try:
        lines = None
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        index = keyboardInput(int, "Please key in index of the Product: ", "Index must be Integer")
        if(index >= len(data)):
            print("Sorry product is not available")
        else:
            product, quantity, price = data[index]
            print(f"Product: {product}\nQuantity:{quantity}\nPrice:{price}")
            confirm = keyboardInput(str, "Are you sure you want to edit this product (y/n) ?", "Confirm must be in String")
            if confirm == "y":
                newproduct = keyboardInput(str, f"Product[{product}]: ", "Product must be ", product)
                newquantity = keyboardInput(int, f"Quantity[{quantity}]:", "Quantity must be in integer", quantity) #int
                newprice = keyboardInput(float, f"Price[{price}]:", "Price must be in float" , price) #float
                data[index] = [newproduct, newquantity, newprice]
                # print(data)
                newlines = []
                for product in data:
                    line = "|".join(map(str, product)) + "\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()
                with open(filename, "wt") as filehandler:
                    filehandler.writelines(newlines)
    except Exception as e:
        print("Something went wrong when we edit the product:", e)

# DELETE PRODUCT
def deleteProduct(filename):
    try:
        lines = None
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        index = keyboardInput(int, "Please key in index of the Product: ", "Index must be Integer")
        if(index >= len(data)):
            print("Sorry product is not available")
        else:
            product, quantity, price = data[index]
            print(f"Product: {product}\nQuantity:{quantity}\nPrice:{price}")
            confirm = keyboardInput(str, "Are you sure you want to delete this product (y/n) ?", "Confirm must be in String")
            if confirm == "y":
                # delete the product by index
                del data[index]
                newlines = []
                for product in data:
                    line = "|".join(map(str, product)) + "\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()
                with open(filename, "wt") as filehandler:
                    filehandler.writelines(newlines)
    except Exception as e:
        print("Something went wrong when we edit the product:", e)


# nama file
filename = "fruits.txt"
createFile(filename)

# call doMenu after create File fx
doMenu(filename)
# addProduct(filename)
# printProduct(filename)





# to write the file, kita xleh guna "xt"
# content = input("Fruit name: ")
# filehandler = open(filename, '')


# open = built in fx
# close = method inside file handler, not built in fx

