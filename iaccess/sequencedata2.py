print("Enter the number of clients")
num_client = int(input())

clientsDetails = []
for i in range(1, num_client +1):
    info = []
    print(f"Enter the details of the client {i}")
    for j in range(3):
        detail = input()
        info.append(detail)

    clientsDetails.append(info)

print("Enter the passport number of the client to be searched")
passport = input()

passports = []
for line in clientsDetails:
    passports.append(line[2])
    if line[2] == passport:
        print(f"Client Details\n{line[0]}--{line[1]}--{line[2]}")

if passport not in passports : print("Client not found")

