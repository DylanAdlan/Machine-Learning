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

# EDIT PRODUCT
def createCarInsurance(carinsurancefile):
    try:
        lines = None
        with open(carinsurancefile, "rt") as filehandler:
            lines = filehandler.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        index = keyboardInput(int, "Please key in index of the Car: ", "Index must be Integer")
        if(index >= len(data)):
            print("Sorry product is not available")
        else:
            car_plate_no, make, model, year, insurance_company, policy_number, vin,coverage_type, premium_amount, status, expiry_date, claim_amount = data[index]
            print(f"Car Plate No: {car_plate_no}\nMake:{make}\nModel:{model}\nYear:{year}\nInsurance company:{insurance_company}\
\nPolicy number:{policy_number}\nVIN:{vin}\nCoverage type:{coverage_type}\nPremium Amount:{premium_amount}\nStatus:{status}\nExpiry date:{expiry_date}\nClaim amount:{claim_amount}")
            if status.strip() == "Active":
                print("The insurance has been active")
            else:
                print("The insurance has been expired")
                confirm = keyboardInput(str, "Do you want to renew this car insurance (y/n) ?", "Confirm must be in String")
                if confirm == "y":
                    newcompany = keyboardInput(str, f"Company[{insurance_company}]: ", "Company must be in string ", insurance_company)
                    newpolicynumber = keyboardInput(str, f"Policy number[{policy_number}]:", "Policy number must be in string", policy_number)
                    newcoverage_type = keyboardInput(str, f"Coverage Type[{coverage_type}]:", "Coverage type must be in string" , coverage_type)
                    newpremiumAmount = keyboardInput(str, f"Premium amount[{premium_amount}]:", "Premium amount must be in integer", premium_amount)
                    newstatus = keyboardInput(str, f"Status[{status}]:", "Status must be in string", status)
                    newexpirydate = keyboardInput(str, f"Expiry date[{expiry_date}]:", "Expiry date must be in string", expiry_date)
                    newclaimAmount = keyboardInput(int, f"Claim amount[{claim_amount}]:", "Claim amount must be in integer", claim_amount)
                    data[index] = [car_plate_no, make, model, year, newcompany, newpolicynumber, vin, newcoverage_type, newpremiumAmount, newstatus, newexpirydate, newclaimAmount]
                    # print(data)
                    newlines = []
                    for product in data:
                        line = "|".join(map(str, product)) + "\n"
                        newlines.append(line)
                    newlines[-1] = newlines[-1].strip()
                    with open(carinsurancefile, "wt") as filehandler:
                        filehandler.writelines(newlines)
    except Exception as e:
        print("Something went wrong when we edit the product:", e)

file = "CarInsurance.txt"
printProduct(file)
createCarInsurance(file)
