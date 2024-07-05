"""
Write a Python class Inventory 
attributes like id, productName, availableQuantity and price. 
methods like addItem, updateItem, and checkItem_details.

Use a dictionary to store the item details
key = id
value = productName, availableQuantity and price.

"""

class Inventory:

    def __init__(self):
        # create empty dictionary to store data
        self.items = {}

    def addItem(self, id, productName, availableQuantity, price):
        if id in self.items:
            print(f"Item with this id {id} is already exists")
        else:
            self.items[id]:{
                "productName": productName,
                "availableQuantity": availableQuantity,
                "price": price
            }
            print(f"Item {productName} added with id {id}.")
        

    def updateItem(self):
        pass

    def checkItem_details(self):
        pass

    def __str__(self):
        self.dict = {}
        listed = [self.id, self.productname, self.availableQuantity, self.price]
        return listed
        # self.dict[listed[0]] = listed[1:]
        # return self.dict


tv = Inventory("97410", "Televsion", 20, 1455.99)
print(tv)

