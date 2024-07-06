# carfile,driverfile,carinsurancefile,driverinsurancefile,bookingfile, claiminsurancefile
from printCarInsurance import printProduct

import time

def keyboardInput(datatype, caption, errorMessage, defaultValue = None):
    value = None
    isInvalid = True
    while(isInvalid):
        try:
            if defaultValue == None:
                value = datatype(input(caption))
            else:
                value = input(caption)
                if value.strip() == "":
                    value = defaultValue
                else:
                    value = datatype(value)
        except:
            print(errorMessage)
        else:
            isInvalid = False
        return value


# edit driver insurance 
def createDriverInsurance(driverinsurancefile): # 
    try:
        lines = None
        with open(driverinsurancefile, "rt") as filehandler:
            lines = filehandler.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        index = keyboardInput(int, "Please key in index of the Driver Insurance: ", "Index must be Integer")
        if(index >= len(data)):
            print("Sorry product is not available")
        else:
            DriverID, DriverName, DriverAge, DriverContact, DriverLicense, DriverCompanyInsurance, DriverPolicy, DriverCoverage, DriverPremium, DriverStatus, DriverExpiryDate, driverClaim = data[index]
            print(f"ID:{DriverID}\nName:{DriverName}\nAge:{DriverAge}\nContact:{DriverContact}\nLicense number:{DriverLicense}\
\nInsurance company:{DriverCompanyInsurance}\nPolicy number:{DriverPolicy}\nCoverage type:{DriverCoverage}\
\nPremium amount:{DriverPremium}\nStatus:{DriverStatus}\nExpiry date:{DriverExpiryDate}\nClaim amount:{driverClaim}")
            if DriverStatus.strip() == "Active":
                print("The insurance has been active")
            else:
                print("The insurance has been expired")
                confirm = keyboardInput(str, "Do you want to renew the insurance (y/n) ?", "Confirm must be in String")
                if confirm == "y":
                    newcompany = keyboardInput(str, f"Company[{DriverCompanyInsurance}]: ", "Company must be in string ", DriverCompanyInsurance)
                    newpolicynumber = keyboardInput(str, f"Policy number[{DriverPolicy}]:", "Policy number must be in string", DriverPolicy)
                    newcoverage_type = keyboardInput(str, f"Coverage Type[{DriverCoverage}]:", "Coverage type must be in string" , DriverCoverage)
                    newpremiumAmount = keyboardInput(str, f"Premium amount[{DriverPremium}]:", "Premium amount must be in integer", DriverPremium)
                    newstatus = keyboardInput(str, f"Status[{DriverStatus}]:", "Status must be in string", DriverStatus)
                    newexpirydate = keyboardInput(str, f"Expiry date[{DriverExpiryDate}]:", "Expiry date must be in string", DriverExpiryDate)
                    newclaimAmount = keyboardInput(int, f"Claim amount[{driverClaim}]:", "Claim amount must be in integer", driverClaim)
                    data[index] = [DriverID, DriverName, DriverAge, DriverContact, DriverLicense, newcompany, newpolicynumber, newcoverage_type, newpremiumAmount, newstatus, newexpirydate, newclaimAmount]
                    # print(data)
                    newlines = []
                    for product in data:
                        line = "|".join(map(str, product)) + "\n"
                        newlines.append(line)
                    newlines[-1] = newlines[-1].strip()
                    with open(driverinsurancefile, "wt") as filehandler:
                        filehandler.writelines(newlines)
    except Exception as e:
        print("Something went wrong when we edit the product:", e)

file = "DriverInsurance.txt"
printProduct(file)
createDriverInsurance(file)