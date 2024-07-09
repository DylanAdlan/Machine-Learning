def sumNumber(filename):
    with open(filename, "rt") as file:
        line = file.read().split()
        line = list(map(int, line))
        total = sum(line)
        print(f"The sum of the integers in the file {filename} is:{total}")
    
# example usage
file = "sample.txt"
sumNumber(file)