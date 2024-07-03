
# RUNTIME ERROR
# bila user key in wrongly (salah datatype)
# atau data from system
# kna bgi mesej to user utuk input specified datatype
principle = int(input())
period = int(input())
rate = int(input())
interest = (principle * period * rate) /100
print("Interest amount:", interest)

# create this code untuk throw mesj to user whenver dia salah enter input in string
try:
    principle = int(input("Principle: "))

except:
    # when the error occur we must do
    print("Principle amount must be in Integer")