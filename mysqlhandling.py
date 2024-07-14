import mysql.connector as mysql

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

def doMenu(connection):
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
            printProduct(connection)
        elif(choice == 2):
            addProduct(connection)
        elif(choice == 3):
            editProduct(connection)
        elif(choice == 4):
            deleteProduct(connection)
# kalau file x exist
# then kita create new file

# nk check if that file is exist or not

# create a fx by passing a filename
def dbConnect(): 
    connection = mysql.connect(
        host="localhost", user="root", password="", database="peneraju")
    return connection

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


# PRINT PRODUCT
def printProduct(connection):
    SQL = f"SELECT id, name, description, quantity, price FROM products"
    cursor = connection.cursor()
    cursor.execute(SQL)
    print("="*110)
    print(f"{'Id':6s}|{'Name':20s}|{'Description':40s}|{'Quantity':20s}|{'Price':20s}")
    for id, name, description, quantity, price in cursor:
        print(f"{id:<6d}|{name:20s}|{description:40s}|{quantity:20d}|{price:20.2f}")
    print("="*110)

# ADD PRODUCT
def addProduct(connection):
    try:
        name = keyboardInput(str, "Product: ", "Product must be in string")
        description = keyboardInput(str, "Decsription:", "Description must be in string") 
        quantity = keyboardInput(int, "Quantity:", "Quantity must be in integer") 
        price = keyboardInput(float, "Price:", "Price must be in float") 
        SQL = F"INSERT INTO products (name, description, quantity, price) VALUES ('{name}','{description}',{quantity},{price})"""
        cursor = connection.cursor()
        cursor.execute(SQL)
        connection.commit()
    except Exception as e:
        print("Something went wrong when we append the product")
'hgfarah cantik'

# EDIT PRODUCT
def editProduct(connection):
    try:
        id = keyboardInput(int, "Please key in index of the Product: ", "Index must be Integer\n")
        SQL = f"SELECT id, name, description, quantity, price FROM products WHERE id = {id}"
        cursor = connection.cursor()
        cursor.execute(SQL)
        id, name, description, quantity, price = cursor.fetchone()
    except:
        print("Product for this ID does not exists")
    else:
        print(f"Product:{name}\nDescription:{description}\nQuantity:{quantity}\nPrice:{price}")
        confirm = keyboardInput(str, "Are you sure you want to edit this product (y/n): ", "Confirmation must be String\n")
        if confirm == "y":
            # print("Let us edit")
            newname = keyboardInput(str, f"Product [{name}]:","Product must be String", name)
            newdescription = keyboardInput(str, f"Product [{description}]:","Product must be String", description)
            newquantity = keyboardInput(int, f"Quantity [{quantity}]: ", "Quantity must be Integer", quantity)
            newprice = keyboardInput(float, f"Price [{price}]: ","Price must be float",price)
            SQL= f"""UPDATE products SET name='{newname}',description='{newdescription}',quantity={newquantity}, price={newprice} WHERE id = {id}"""
            cursor = connection.cursor()
            cursor.execute(SQL)
            connection.commit()
     

def deleteProduct(connection):
    try:
        id = keyboardInput(int, "Please key in index of the Product: ", "Index must be Integer\n")
        SQL = f"SELECT id, name, description, quantity, price FROM products WHERE id = {id}"
        cursor = connection.cursor()
        cursor.execute(SQL)
        id, name, description, quantity, price = cursor.fetchone()
    except:
        print("Product for this ID does not exists")
    else:
        print(f"Product:{name}\nDescription:{description}\nQuantity:{quantity}\nPrice:{price}")
        confirm = keyboardInput(str, "Are you sure you want to edit this product (y/n): ", "Confirmation must be String\n")
        if confirm == "y":
            SQL= f"""DELETE from products WHERE id = {id}"""
            cursor = connection.cursor()
            cursor.execute(SQL)
            connection.commit()
     
    # except Exception as e:
    #     print("Something went wrong when we edit the product:", e)


# example usage
connection = dbConnect()
doMenu(connection)
