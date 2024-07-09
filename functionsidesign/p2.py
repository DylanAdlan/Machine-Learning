def daysInYear(year, argument2 = False):
    
    if (year % 100 !=0 and year % 4 == 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

#example usage
daysInYear(2000)