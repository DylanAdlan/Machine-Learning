with open("input.txt", "rt") as file:
    lines = file.readlines()
    count = 0
    for line in lines:
        count +=1
    
    print(f"The file has {count} lines")