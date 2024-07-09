# def divisible13():

#     size = int(input("Enter size of list\n"))
#     if size>0:
#         divisible = []
#         print("Enter the elements in list")
#         for i in range(size):
#             number = int(input())
#             divisble = for number % 13 == 0:
#                 divisible.append(number)
#             else:
#                 continue

#         for no in divisible:
#             print(no, end=" ")

#     else:
#         print("Invalid input")
    

# # example usage
# divisible13()

n = int(input("Enter size of list\n"))

if n <= 0:
    print("Invalid input")
else:
    numbers = []
    print("Enter the elements in list")
    for i in range(n):
        number = int(input())
        numbers.append(number)
    
    divisible13 = list(filter(lambda x : x % 13 == 0, numbers))
    print(' '.join(map(str, divisible13)))
