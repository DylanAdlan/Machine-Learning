import time
from datetime import datetime

def keyboardInput(datatype, caption, errorMessage,defaultValue = None):
    value = None
    isInvalid = True
    while (isInvalid):
        try:
            if defaultValue == None:
                value = datatype(input(caption))
            else:
                value = input(caption)
                if value.strip()=="":
                    value = defaultValue
                else:
                    value = datatype(value)
        except:
            print(errorMessage)
        else:
            isInvalid = False   
    return value

def doMenu (carfile,driverfile,carinsurancefile,driverinsurancefile,bookingfile, claiminsurancefile):
    choice = -1
    
    while choice != 0:
        print("\n    Welcome to AEA Cars!!\n")
        print("*"*34)
        print("          Main Menu              ")
        print("---------------------------------")
        print("|  0 - Exit                     |")
        print("|  1 - Create Car Insurance     |")
        print("|  2 - Create Driver Insurance  |")
        print("|  3 - Claim Insurance          |")
        print("|  4 - Print Receipt            |")
        print("|  5 - Department Report        |")
        print("---------------------------------")
        choice = keyboardInput(int, "Enter your choice: ", "Invalid choice")
        print("")
        if choice==0:
            print("Thank You!!")
        elif choice == 1:
            printCar(carfile, carinsurancefile)
        elif choice == 2:
            printDriver(driverfile, driverinsurancefile)
        elif choice == 3:
            chooseBokingLine(bookingfile,carinsurancefile,driverinsurancefile, claiminsurancefile)            
        elif choice == 4:
            printResit(claiminsurancefile)
        elif choice == 5:
            reportCompany(carinsurancefile, driverinsurancefile, claiminsurancefile)
        
def printCar(carfile, carInsurancefile):
    try:
        lines =None
        with open(carfile, "rt") as filehandler:
            lines = filehandler.readlines()

        for index, line in enumerate(lines):
            
            carPlate, make, model, year, vin, mileage, expiry_date, status = line.strip().split(" | ")# strip method remove the last \n (new line) & remove spaces
            if (index == 0):
                print(f"{"No.":<4}{carPlate:<12}{make:<12}{model:<9}{year:<5}{vin:<19}\
{mileage:<10}{vin:<20}{expiry_date:<25}{status:<10}")
                print("=" * 140)
            else:
                print(f"{index:<4}{carPlate:<12}{make:<12}{model:<9}{year:<5}{vin:<19}\
{mileage:<10}{vin:<20}{expiry_date:<25}{status:<10}")


        datas = []
        for line in lines:
            # print(line)
            datas.append(line.strip().split(" | "))

        
        index = keyboardInput(int, "Enter a number:", "Number must be in integer")
        while index==0:
            print("Invalid")
            index = keyboardInput(int, "Enter a number:", "Number must be in integer")

        else:
            carPlate, make, model, year, vin, mileage, expiry_date, status = datas[index]

            print(f"\nCar plate number: {carPlate}\nMake: {make}\nModel: {model}\nYear: {year}\nVIN: {vin}\
    \nMileage: {mileage}\nInsurance expiry date: {expiry_date}\nStatus: {status}")
            if status.strip() == "Active":
                print("\nThe insurance has been active")
            else:
                print("\nThe insurance has been expired")
                confirm = keyboardInput(str, "\nDo you want to renew this car insurance (y/n) ?", "Confirm must be in String")
                if confirm == "y":
                    findCarInsurance(carInsurancefile, carPlate, carfile)

    except Exception as e: 
        print("Something went wrong when we print the products:", e)

def findCarInsurance(carinsurancefile, carplate, carfile):
    carPlate = carplate.replace(" ","")
    try:
        with open(carinsurancefile, "rt") as file:
            lines = file.readlines()

        datas = []
        for line in lines:
            datas.append(line.strip().split(" | "))
        

        for i, data in enumerate(datas): # i for row
            if data[0].replace(" ","") == carPlate:
                
                carPlate, make, model, year, insurance_company, policy_number, vin,coverage_type, premium_amount, status, expiry_date, claim_amount = data
                newcompany = keyboardInput(str, f"Company[{insurance_company}]: ", "Company must be in string ", insurance_company)
                newpolicynumber = keyboardInput(str, f"Policy number[{policy_number}]: ", "Policy number must be in string", policy_number)
                newcoverage_type = keyboardInput(str, f"Coverage Type[{coverage_type}]: ", "Coverage type must be in string" , coverage_type)
                newpremiumAmount = keyboardInput(str, f"Premium amount[{premium_amount}]: ", "Premium amount must be in integer", premium_amount)
                newstatus = keyboardInput(str, f"Status[{status}]: ", "Status must be in string", status)
                newexpirydate = keyboardInput(str, f"Expiry date[{expiry_date}]: ", "Expiry date must be in string", expiry_date)
                newclaimAmount = keyboardInput(int, f"Claim amount[{claim_amount}]: ", "Claim amount must be in integer", claim_amount)
                datas[i] = [carPlate, make, model, year, newcompany, newpolicynumber, vin, newcoverage_type, newpremiumAmount, newstatus, newexpirydate, newclaimAmount]
                break

        newlines = []
        for product in datas:
            line = " | ".join(map(str, product)) + "\n"
            newlines.append(line)
        newlines[-1] = newlines[-1].strip()
        with open(carinsurancefile, "wt") as filehandler:
            filehandler.writelines(newlines)

        updateCarfile(carfile, carinsurancefile, carplate)
        
        
    except Exception as e:
        print("Something went wrong when we edit the product:", e)

def updateCarfile(carfile, carinsurancefile, carplate):
    carPlate = carplate.replace(" ","")

    try:
        with open(carfile, "rt") as filecar:
            linecar = filecar.readlines()

        with open(carinsurancefile, "rt") as fileinsurance:
            lineinsurance = fileinsurance.readlines()

        datacars = []
        for line in linecar:
            datacars.append(line.strip().split(" | "))

        datacarinsurances = []
        for line in lineinsurance:
            datacarinsurances.append(line.strip().split(" | "))


        for i, datacar in enumerate(datacars): # i for row
            for j, datacarinsurance in enumerate(datacarinsurances):
                if datacar[0].replace(" ","") == carPlate and datacarinsurance[0].replace(" ","") == carPlate:
                
                    Carplate, carmake, carmodel, caryear, carvin, mileage, carexpiry_date, carstatus = datacar
                    carPlate, make, model, year, insurance_company, policy_number, vin,coverage_type, premium_amount, status, expiry_date, claim_amount = datacarinsurance
                    carexpiry_date = expiry_date
                    carstatus = status
                    datacars[i] = [Carplate, carmake, carmodel, caryear, carvin, mileage, carexpiry_date, carstatus]
        
        newlines = []
        for product in datacars:
            line = " | ".join(map(str, product)) + "\n"
            newlines.append(line)
        newlines[-1] = newlines[-1].strip()
        with open(carfile, "wt") as filehandler:
            filehandler.writelines(newlines)



    except Exception as e:
        print("Something went wrong when we edit the product:", e)

def printDriver(driverfile, driverInsurancefile):
    try:
        lines =None
        with open(driverfile, "rt") as filehandler:
            lines = filehandler.readlines()
        for index, line in enumerate(lines):

            driverId, drivername, driverAge, gender, license, driverExpiredate, driverstatus = line.strip().split(" | ")# strip method remove the last \n (new line) & remove spaces
            if (index == 0):
                print(f"{"No.":<4}{driverId:<8}{drivername:<15}{driverAge:<4}{gender:<8}{license:<19}\
{driverExpiredate:<15}{driverstatus:<10}")
                print("=" * 100)
            else:
                print(f"{index:<4}{driverId:<8}{drivername:<15}{driverAge:<4}{gender:<8}{license:<19}\
{driverExpiredate:<15}{driverstatus:<10}")


        datas = []
        for line in lines:
            # print(line)
            datas.append(line.strip().split(" | "))
        
        index = keyboardInput(int, "Enter a number: ", "Number must be in integer")
        while index==0:
            print("Invalid")
            index  =keyboardInput(int, "Enter a number:", "Number must be in integer")
        driverId, drivername, driverAge, gender, license, driverExpiredate, driverstatus = datas[index]

        print(f"\nDriver ID: {driverId}\nName: {drivername}\nAge: {driverAge}\nGender: {gender}\niLicense number: {license}\nInsurance expired date: {driverExpiredate}\
\nInsurance status: {driverstatus}")
        
        if driverstatus.strip() == "Active":
            print("\nThe insurance has been active")
        else:
            print("\nThe insurance has been expired")
            confirm = keyboardInput(str, "\nDo you want to renew this driver insurance (y/n) ?", "Confirm must be in String")
            if confirm == "y":
                findDriverInsurance(driverInsurancefile, driverId, driverfile)

    except Exception as e: 
        print("Something went wrong when we print the products:", e)



def findDriverInsurance(driverInsurancefile, driverId, driverfile):
    driverID = driverId.replace(" ","")
    try:
        with open(driverInsurancefile, "rt") as file:
            lines = file.readlines()

        datas = []
        for line in lines:
            datas.append(line.strip().split(" | "))
        

        for i, data in enumerate(datas): # i for row
            if data[0].replace(" ","") == driverID:
                
                driverID, DriverName, DriverAge, DriverContact, DriverLicense, DriverCompanyInsurance, DriverPolicy, DriverCoverage, DriverPremium, DriverStatus, DriverExpiryDate, driverClaim = data
                newcompany = keyboardInput(str, f"Company[{DriverCompanyInsurance}]: ", "Company must be in string ", DriverCompanyInsurance)
                newpolicynumber = keyboardInput(str, f"Policy number[{DriverPolicy}]: ", "Policy number must be in string", DriverPolicy)
                newcoverage_type = keyboardInput(str, f"Coverage Type[{DriverCoverage}]: ", "Coverage type must be in string" , DriverCoverage)
                newpremiumAmount = keyboardInput(str, f"Premium amount[{DriverPremium}]: ", "Premium amount must be in integer", DriverPremium)
                newstatus = keyboardInput(str, f"Status[{DriverStatus}]: ", "Status must be in string", DriverStatus)
                newexpirydate = keyboardInput(str, f"Expiry date[{DriverExpiryDate}]: ", "Expiry date must be in string", DriverExpiryDate)
                newclaimAmount = keyboardInput(int, f"Claim amount[{driverClaim}]: ", "Claim amount must be in integer", driverClaim)
                datas[i] = [driverID, DriverName, DriverAge, DriverContact, DriverLicense, newcompany, newpolicynumber, newcoverage_type, newpremiumAmount, newstatus, newexpirydate, newclaimAmount]
                break
                
        newlines = []
        for product in datas:
            line = " | ".join(map(str, product)) + "\n"
            newlines.append(line)
        newlines[-1] = newlines[-1].strip()
        with open(driverInsurancefile, "wt") as filehandler:
            filehandler.writelines(newlines)

        updateDriverfile(driverfile, driverInsurancefile, driverID)
        
        
    except Exception as e:
        print("Something went wrong when we edit the product:", e)

def updateDriverfile(driverfile, driverInsurancefile, driverID):
    driverID = driverID.replace(" ","")

    try:
        with open(driverfile, "rt") as filedriver:
            linedriver = filedriver.readlines()

        with open(driverInsurancefile, "rt") as fileinsurance:
            lineinsurance = fileinsurance.readlines()

        datadrivers = []
        for line in linedriver:
            datadrivers.append(line.strip().split(" | "))

        datadriverinsurances = []
        for line in lineinsurance:
            datadriverinsurances.append(line.strip().split(" | "))


        for i, datadriver in enumerate(datadrivers): # i for row
            for j, datadriverinsurance in enumerate(datadriverinsurances):
                if datadriver[0].replace(" ","") == driverID and datadriverinsurance[0].replace(" ","") == driverID:
                
                    driverId, drivername, driverAge, gender, license, driverExpiredate, driverstatus = datadriver
                    DriverID, DriverName, DriverAge, DriverContact, DriverLicense, DriverCompanyInsurance, DriverPolicy, DriverCoverage, DriverPremium, DriverStatus, DriverExpiryDate, driverClaim = datadriverinsurance
                    driverstatus = DriverStatus
                    driverExpiredate = DriverExpiryDate
                    datadrivers[i] = [driverId, drivername, driverAge, gender, license, driverExpiredate, driverstatus]
        
        newlines = []
        for product in datadrivers:
            line = " | ".join(map(str, product)) + "\n"
            newlines.append(line)
        newlines[-1] = newlines[-1].strip()
        with open(driverfile, "wt") as filehandler:
            filehandler.writelines(newlines)



    except Exception as e:
        print("Something went wrong when we edit the product:", e)

def createDriverInsurance(driverfile, driverinsurancefile):
#     try:
#         lines =None
#         with open(driverfile, "rt") as filehandler:
#             # read all lines 
#             lines = filehandler.readlines()
#         for index, line in enumerate(lines):
#             driver_id, driver_name, driver_age, driver_gender, license, insurance_company, policy_number,\
#             coverage_type, premium_amount, status, expiry_date, claim_amount = line.strip().split("|")# strip method remove the last \n (new line) & remove spaces
#             if (index == 0):
#                 print(f"{"No.":<4}{driver_id:<6}{driver_name:<16}{driver_age:<5}{driver_gender:<8}{license:<18}{insurance_company:<19}\
# {policy_number:<14}{coverage_type:<15}{premium_amount:<16}{status:<10}\
# {expiry_date:<13}{claim_amount:<10}")
#                 print("=" * 159)
#             else:
#                 print(f"{index:<4}{driver_id:<6}{driver_name:<16}{driver_age:<5}{driver_gender:<8}{license:<18}{insurance_company:<19}\
# {policy_number:<14}{coverage_type:<15}{premium_amount:<16}{status:<10}\
# {expiry_date:<13}{claim_amount:<10}")
#     except Exception as e: 
#         print("Something went wrong when we print the products:", e)
    pass

def chooseBokingLine(bookingfile,carinsurancefile,driverinsurancefile, claiminsurancefile):
    verify = True
    while verify:
        # with open(bookingfile, "rt") as file:
        #     display = file.read()
        #     print("\nBooking Detail:")
        #     print(display)
        print("\nBooking Detail:\n")
        readbookingfile(bookingfile)

        try:
            lines = None
            with open(bookingfile, "rt") as file:
                lines = file.readlines()
                #print(lines)
            data = []
            for line in lines:
                data.append(line.strip().split("|"))
            #print(data)

            index = keyboardInput(int,"Plesase insert line number: ", "Number must be integer")
            while index==0:
                print("Invalid!")
                index = keyboardInput(int,"Plesase insert line number: ", "Number must be in integer")
            print("\nPlese check the detail carefully...")
            BookingID, CustomerID, CarPlate, DriverID, DriverName, BookingDate = data[index]
            print(f"\nBooking ID: {BookingID}\nCustomer ID: {CustomerID}\nPlate No: {CarPlate}\nDriver ID: {DriverID}\nName: {DriverName}\nBooking Date: {BookingDate}")
            confirm = keyboardInput(str, "\nDetails is true?  (y/n): ", "Please insert y or n")
            if confirm == "y":
                print("\nDetail Claim Amont:")
                carClaim = claimfindCarInsurance(carinsurancefile, CarPlate)
                driverClaim = claimfindDriverInsurance(driverinsurancefile, DriverID)
                totalClaim = carClaim + driverClaim
                print(f"Total Claim: {totalClaim}\n")
            
                totalClaimInsurance(claiminsurancefile,BookingDate, CarPlate, carClaim, DriverID, driverClaim, totalClaim)
                verify = False
            #BookingID | CustomerID | CarPlate | DriverID | DriverName | BookingDate

        except Exception as e:
            print("Error edit product:", e)

def readbookingfile(bookingfile):
    with open (bookingfile, "r") as file:
        booking = file.readlines()
    
    for index, line in enumerate(booking):
        bookingID, custID, carPlate, driverID, driverName, bookingDate = line.strip().split(" | ")
        if (index == 0):
            print(f"{"No.":<4}{bookingID:<12}{custID:<13}{carPlate:<15}{driverID:<12}{driverName:<18}{bookingDate:<15}")
            print("=" * 85)
        else:
            print(f"{index:<4}{bookingID:<12}{custID:<13}{carPlate:<15}{driverID:<12}{driverName:<18}{bookingDate:<15}")
    print("-" * 90)
    print()

def claimfindCarInsurance (carinsurancefile,CarPlate):
    CarPlate = CarPlate.replace(" ","")
    #carinsurancefile = "CarInsurance.txt"
    with open(carinsurancefile, "rt") as file:
        lines = file.readlines()
    
    datas = []
    for line in lines:
        datas.append(line.strip().split(" | "))
    #print(data)
    for data in datas:
        #print(f"{data[0]}:")
        if data[0].replace(" ","") == CarPlate:
            print(f"Car Insurance Claim: {data[-1]}")
            break
            
    else:
        print("Car Insurance not found")
    
    return int(data[-1])

def claimfindDriverInsurance (driverinsurancefile, DriverID):
    DriverID = DriverID.replace(" ","")
    # print(f"{DriverID}:")
    #driverinsurancefile = "DriverInsurance.txt"
    with open(driverinsurancefile, "rt") as file:
        lines = file.readlines()
    
    datas = []
    for line in lines:
        datas.append(line.strip().split(" | "))
    #print(data)
    for data in datas:
        # print(f"{data[0]}:")
        if data[0].replace(" ","") == DriverID:
            print(f"Driver Insurance Claim: {data[-1]}")
            break
    else:
        print("Driver Insurance not found")
    
    return int(data[-1])

def totalClaimInsurance (claimInsurancefile,BookingDate, CarPlate, carClaim, DriverID, driverClaim, totalClaim):
    #claimInsurancefile = "ClaimInsurance.txt"
    try:
        with open(claimInsurancefile, "at") as file:
            total = file.write(f"\n{BookingDate} | {CarPlate} | {carClaim} | {DriverID} | {driverClaim} | {totalClaim}")
            #print(total)

    except Exception as e:
        print("Something went wrong when we write to the file", e)

def printResit (claimInsurancefile):
    lines = None
    print("*"*120)
    net_claimed = 0.0
    #claimInsurancefile = "ClaimInsurance.txt"
    try:
        with open(carinsurancefile,"rt") as file:
            line = file.readlines()

            print(" "*47,"\033[1mSUMMARY INSURANCE CLAIMED\033[0m"," "*47)
            print("\n"," "*45,"AEA CAR RENTAL SERVICE SDN BHD"," "*45)
            print(" "*42,"123,AEA STREET, EFG CITY,45689 HIJL"," "*42)
            print(" "*52,"(123)- 4567 890"," "*52)
            print(" "*51,"\033[94minfo@AEARENTAL.com\033[0m"," "*51)
            print("-"*120)

        with open(claimInsurancefile, 'rt') as filehandler:
            
            lines = filehandler.readlines()
        
        print("\nInvoices Summary:\n")
        for index,line in enumerate(lines):
            parts = line.strip().split("|")
            if len(parts) == 6:
                BookingDate, CarPlate, carClaim, DriverID, driverClaim, totalClaim = parts
                if(index == 0):
                    print(f"{"No:":5}{BookingDate:>11}{CarPlate:>15}{carClaim:>25}{DriverID:>12}{driverClaim:>25}{totalClaim:>2}")
                    print("=" * 116)
                else:
                    CarPlate = CarPlate.strip()
                    print(f"{index:<5}{BookingDate:15}{CarPlate:>10}{carClaim:>25}{DriverID:>14}{driverClaim:>23}{totalClaim:>22}")
                    #print("-"*116)
        
        for line in lines[1:]:
            line = line.strip().split("|")
            net_claimed += float(line[5].strip())
        print(" "*77,f"Net total claimed:     \033[92mRM {net_claimed:,.2f}\033[0m")

        print("")
        time.sleep(2)
    except Exception as e:
        print("Something went wrong when we read from the file", e)
#______________________________________________________________________________#
def reportCompany (carinsurancefile, driverinsurancefile, claiminsurancefile):
    print('-'*20, "REPORT ON INSURANCE DEPARTMENT",'-'*20)
    try:
        year = keyboardInput(int,"Report Year: ","Please input Year in YYYY format")
        while len(str(year)) != 4 :
            print("Invalid!")
            year = keyboardInput(int,"Report Year: ","Please input Year in YYYY format")
        #to get the report on the month that user want
        targetDate = datetime(year,1,1)
        totalCarsWithInsurance = 0
        totalActiveCars = 0
        totalInactiveCar = 0
        totalDriverWithInsurance = 0
        totalActiveDriver = 0
        totalInactiveDriver = 0
        totalRenewInsuranceCar = 0
        totalClaims = 0
        while year ==2024:
            with open(carinsurancefile,'rt') as file:
                next(file)
                for line in file:
                    data = line.strip().split("|")
                    if len(data)<12:
                        continue

                    expiry_date_str = data[-2].strip()
                    status = data[-3].strip()

                    try: 
                        expiry_date= datetime.strptime(expiry_date_str, '%Y-%m-%d')

                    except:
                        print(f"Invalid date format encountered:{expiry_date_str}. Skip line")
                        continue
                    if expiry_date.year<=year or expiry_date.year>=year:
                        totalCarsWithInsurance += 1
                        if status == 'Active':
                            totalActiveCars += 1
                        elif status == 'Inactive':
                            totalInactiveCar += 1
                    else:
                        print (f"The report for Year {year} is not available.")
                        break
            
            with open(driverinsurancefile,'rt') as file:
                next(file)
                for line in file:
                    data = line.strip().split("|")
                    if len(data)<12:
                        continue

                    expiry_date_str = data[-2].strip()
                    status = data[-3].strip()
                    try:
                        expiry_date = datetime.strptime(expiry_date_str, '%Y-%m-%d')

                    except:
                        print(f"Invalide date format encountered:{expiry_date_str}. Skip line")
                        continue
                    if expiry_date.year<=year or expiry_date.year>=year:
                        totalDriverWithInsurance += 1
                        if status == 'Active':
                            totalActiveDriver += 1
                        elif status == 'Inactive':
                            totalInactiveDriver += 1
                    else:
                        print(f"The report for year {year} is not available.")
                        break
            totalRenewInsuranceCar = totalInactiveCar + totalInactiveDriver
            with open(claiminsurancefile,'rt') as file:
                next(file)
                for line in file:
                    data = line.strip().split("|")
                    if len(data)<6:
                        continue

                    booking_date_str = data[0].strip()
                    try:
                        booking_date = datetime.strptime(booking_date_str, '%Y-%m-%d')

                    except ValueError:
                        print(f"Invalid date format encountered: {booking_date_str}. Skip line.")
                        continue

                    if booking_date.year==year:
                        totalClaims += 1

            #display
            print("="*72)
            print(f"\nReport for {targetDate.strftime('%B %Y')}")

            print(f"\n1.   Total cars with insurance(car(s)):"," "*31,f"{totalCarsWithInsurance}")
            print(f"     - Cars with Active insurance(car(s)):"," "*28,f"{totalActiveCars}")
            print(f"     - Cars with Inactive insurance(car(s)):"," "*26,f"{totalInactiveCar}")
            print(f"2.   Total drivers with insurance(driver(s)):"," "*25,f"{totalDriverWithInsurance}")
            print(f"     - Drivers with Active insurance(driver(s)):"," "*22,f"{totalActiveDriver}")
            print(f"     - Drivers with Inactive insurance(driver(s)):"," "*20,f"{totalInactiveDriver}")
            print(f"3.   Total insurance that need to renew its insurance(insurance(s)):"," "*2,f"{totalRenewInsuranceCar}")
            print(f"4.   Total claims that has been made(claims):"," "*25,f"{totalClaims}")

            time.sleep(2)
            break
        else:
            print("No record")

    except FileNotFoundError:
        print("Error: One or more insurance file not found")

    except Exception as e:
        print(f"An error occured: {e}")

    except FileNotFoundError:
        print("Error: One or more insurance file not found")

    except Exception as e:
        print(f"An error occured: {e}")


carfile = "Car.txt"
driverfile = "Driver.txt"
carinsurancefile = "CarInsurance.txt"
driverinsurancefile = "DriverInsurance.txt"
bookingfile = "Booking.txt"
claiminsurancefile = "ClaimInsurance.txt"

doMenu(carfile,driverfile,carinsurancefile,driverinsurancefile,bookingfile, claiminsurancefile)