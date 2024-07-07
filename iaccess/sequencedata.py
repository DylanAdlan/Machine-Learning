number1 = input().split(",")
number2 = input().split(",")

num1 = set(map(int, number1))
num2 = set(map(int, number2))

print(num1.issubset(num2))
print(num2.issubset(num1))
print(num1.issuperset(num2))
print(num2.issuperset(num1))
