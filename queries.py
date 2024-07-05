# any / all => built in fx
# take boolean list as parameter
# [True, False, False, True]

#Any fx take above list as parameter will return True
#(any == or)

# all fx take above list as parametr will return False
# (all == and)

# example
# to check the number is prime number or not
givenNumber = 11
divisors = range(2, givenNumber)

if len([mynumber for mynumber in divisors if (givenNumber % mynumber == 0)]) == 0:
    print("Prime Number")
else:
    print("Not Prime Number")

# return True/ False
if any ([givenNumber % mynumber == 0 for mynumber in divisors]):
    print("Not Prime Number")
else:
    print("Prime Number")


# CONTOH SOALAN RELATE TO PRIME NUMBER
# check whether givennumber is prime number
# check whether the input is prime number or not
# generate 10 first prime number
# generate prime numbers between 10 to 100
