# create this code untuk throw mesj to user whenver dia salah enter input in string
try:
    # user input data (MUST BE INTEGER!)
    # another example put the file open code here
    principle = int(input("Principle: "))

except ValueError:
    # executed bila ade error, eg: (USER ENTER STRING)
    # another eg throw errors like file corrupted/ file missing
    print("Principle amount must be in Integer")
    principle = 1000

# except Exception as e:
#     # executed bila ade error, eg: user enter string
#     print("Something went wrong:", e)

else:
    # akan executed bila xde error 

    print("All is well")

finally:
    # executed regardless error occur or not
    # another eg Close the file
    print("Thank you!")


# RUNTIME ERROR
# bila user key in wrongly (salah datatype)
# atau data from system
# kna bgi mesej to user utuk input specified datatype
# principle = int(input())
period = int(input("Period: "))
rate = int(input("Rate: "))
interest = (principle * period * rate) /100
print("Interest amount:", interest)



# response system error must be friendly so user know what is wrong

