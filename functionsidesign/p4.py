def add(num1, num2):
    print(f"{num1} + {num2} = {num1 + num2}")

def subtract(num1, num2):
    print(f"{num1} - {num2} = {num1 - num2}")

def multiply(num1, num2):
    print(f"{num1} * {num2} = {num1 * num2}")

def division(num1, num2):
    print(f"{num1} / {num2} = {num1 // num2}")

def modulus(num1, num2):
    print(f"{num1} % {num2} = {num1 % num2}")


def main():
    print("Select the operation\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Modulus")
    print("Enter the choice(1/2/3/4/5):")
    n = int(input())
    if n < 1 or n > 5:
        print("Invalid Input")
    else:
        print("Enter the first number")
        num1 = int(input())
        print("Enter the second number")
        num2 = int(input())

        if n == 1:
            add(num1, num2)
        elif n == 2:
            subtract(num1, num2)
        elif n == 3:
            multiply(num1, num2)
        elif n == 4:
            division(num1, num2)
        elif n == 5:
            modulus(num1, num2)
        else:
            pass


# example usage
main()

    
