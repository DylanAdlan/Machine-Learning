def keyboardInput(datatype, caption, errorMessage):
    value = None
    isInvalid = True
    while(isInvalid):
        try:
            # take caption as parameter sbb kita ade byk input from user
            value = datatype(input(caption))
        except:
            print(errorMessage)
        else:
            isInvalid = False

    return value


def calculateSimpleInterest():
    principle = keyboardInput(int, "Principle Amount:", "Principle must be in integer" ) #int
    period = keyboardInput(float, "Period in years:", "Period must be in float" ) #float
    rate = keyboardInput(float, "Rate in percentage:", "Rate must be in float") #float
    interest = (principle * period * rate) /100
    print("Interest Amount:", interest)
    print("Total Amount to be paid:", principle + interest)

calculateSimpleInterest()