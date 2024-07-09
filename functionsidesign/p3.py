def GCD(n1, n2): # greatest common divisor
    while n2!= 0:
        n1, n2 = n2, n1 % n2
    return n1


def LCM(n1, n2): # lease common multiple
    return (n1 * n2) // GCD(n1, n2)

# example usage
print("Enter two integers:")
n1 = int(input())
n2 = int(input())
print(f"Greatest common divisor of {n1} and {n2} = {GCD(n1, n2)}")
print(f"Least common multiple of {n1} and {n2} = {LCM(n1, n2)}")