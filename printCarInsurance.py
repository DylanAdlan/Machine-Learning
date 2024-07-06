# filename = CarInsurance.txt

def printProduct(carinsurancefile):
    try:
        lines =None
        with open(carinsurancefile, "rt") as filehandler:
            # read all lines 
            lines = filehandler.readlines()
        for index, line in enumerate(lines):
            car_plate_no, make, model, year, insurance_company, policy_number, vin, coverage_type, premium_amount, status, expiry_date, claim_amount = line.strip().split("|")# strip method remove the last \n (new line) & remove spaces
            if (index == 0):
                print(f"{"No.":<4}{car_plate_no:<12}{make:<12}{model:<9}{year:<5}{insurance_company:<19}\
{policy_number:<14}{vin:<20}{coverage_type:<15}{premium_amount:<16}{status:<10}\
{expiry_date:<13}{claim_amount:<10}")
                print("=" * 165)
            else:
                print(f"{index:<4}{car_plate_no:<12}{make:<12}{model:<10}{year:<5}{insurance_company:<19}\
{policy_number:<14}{vin:<20}{coverage_type:<15}{premium_amount:<16}{status:<10}\
{expiry_date:<13}{claim_amount:<10}")

            #     print(f"{index:<5}{product:40}{int(quantity):>20}{float(price):>20.2f}")
    except Exception as e: 
        print("Something went wrong when we print the products:", e)

file = "CarInsurance.txt"
printProduct(file)
