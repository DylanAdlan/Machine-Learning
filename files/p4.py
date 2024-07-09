def reverseWord(filename):

    with open(filename, "rt") as file:
        lines = file.read()
        print(lines[::-1])

        with open("output.txt", "wt") as filehandler:
            filehandler.write(lines[::-1])


file = "sample.txt"
reverseWord(file)