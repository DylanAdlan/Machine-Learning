def printProduct(driverinsurancefile):
    try:
        lines =None
        with open(driverinsurancefile, "rt") as filehandler:
            # read all lines 
            lines = filehandler.readlines()
        for index, line in enumerate(lines):
            driver_id, driver_name, driver_age, driver_gender, license, insurance_company, policy_number,\
            coverage_type, premium_amount, status, expiry_date, claim_amount = line.strip().split("|")# strip method remove the last \n (new line) & remove spaces
            if (index == 0):
                print(f"{"No.":<4}{driver_id:<6}{driver_name:<16}{driver_age:<5}{driver_gender:<8}{license:<18}{insurance_company:<19}\
{policy_number:<14}{coverage_type:<15}{premium_amount:<16}{status:<10}\
{expiry_date:<13}{claim_amount:<10}")
                print("=" * 159)
            else:
                print(f"{index:<4}{driver_id:<6}{driver_name:<16}{driver_age:<5}{driver_gender:<8}{license:<18}{insurance_company:<19}\
{policy_number:<14}{coverage_type:<15}{premium_amount:<16}{status:<10}\
{expiry_date:<13}{claim_amount:<10}")
    except Exception as e: 
        print("Something went wrong when we print the products:", e)

printProduct("DriverInsurance.txt")
