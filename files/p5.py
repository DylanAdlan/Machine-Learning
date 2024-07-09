import csv

def printfilecsv():
    with open("SalariesDataSet.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(";".join(row))

printfilecsv()
   