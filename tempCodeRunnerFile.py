# raise error
# class Rank:

#     def __init__(self, classroom, rank):
#         self.classroom = classroom
#         self.rank = rank

#     def __repr__(self):
#         return f"<Car {self.classroom} {self.rank}>"


# class Student:

#     def __init__(self):
#         self.name = []
#         pass

#     def __len__(self):
#         return len(self.name)
     
#     def add_name(self, name):
#         if not isinstance(name, Rank):
#             raise TypeError("Tried to to add {name.__class__.__name}")
#         self.name.append(name)

# adnin = Student()
# adnin.add_name("Adnin")
# print(len(adnin))