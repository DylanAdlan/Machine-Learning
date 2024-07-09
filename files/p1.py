def averageWordLength(filename):
    with open(filename, "rt") as file:

        text = file.read().split()
        print(text)
        count = 0
        for words in text:
            for char in words:
                count +=1

        averagelength = count // len(text)
        print(averagelength)


file = "averageLength.txt"
averageWordLength(file)

