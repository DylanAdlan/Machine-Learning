"""
1. read the content from file : open and read the file
2. count the frequency of the characters
3. sort the frequency table, sort by keys
4. print the sorted frequency table
"""

def count_char(file_path):

    # initialize dict to store character count
    chars_count = {}
    
    with open(file_path, 'r') as f:
        word = f.read() # A32dninadlan

    for char in word:
        if char.isalpha():  # if char is  alphabet character. then == True
            char = char.lower()
            if char in chars_count:
                chars_count[char] +=1
            else:
                chars_count[char] = 1

    # chars_count.items = returns a list of tuples [("a": 1), ("b": 3)]
    # sorted function akan return dlm alphabet ascending order
    sorted_char = sorted(chars_count.items())

    # convert back from tuples to dict
    sorted_char = dict(sorted_char)

    for char, count in sorted_char.items():
        print(f"{char}: {count}")

file = "frequencyFile.txt"
count_char(file)

# syu method

def charcount():
    with open("frequencyFile.txt", "rt") as file:
        lines = file.read().lower()
        words = lines.split()

        count = {}
        for i in words:
            if i in count:
                count[i] +=1
            else:
                count[i] = 1

        for i in count:
            print(f"{count[0]}:{count[1]}")


charcount()







        
         

    









       