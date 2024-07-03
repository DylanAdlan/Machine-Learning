number = int(input())

for j in range(4): # 0,1,2,3
    for l in range(2): # 0,1,2,3
        for i in range(number): # 0,1,2
            print("/", end="")
        for i in range(number): # 0,1,2
            print("\\", end="")
    print() # akan ke next line after finish "l" loop