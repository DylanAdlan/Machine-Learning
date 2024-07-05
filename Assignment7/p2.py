"""
Problem 2:
An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.
Examples of isograms:
lumberjacks background downstream six-year-old

The word isograms, however, is not an isogram, because the s repeats.
Your task is to figure out if the user input is isogram
"""

def determineIsogram(word):

    unique_word = []
    duplicate_char = ''

    isIsogram = True
    for char in word:
        if char == " " or char == "-":
            continue
        else:
            if char not in unique_word:
                unique_word.append(char)
            else:
                isIsogram = False
                duplicate_char += char

    duplicate_char = set(duplicate_char)

    if isIsogram == True:
        print(f"The word ({word}) is an isogram")
    else:
        print(f"The word ({word}) is not an isogram because {duplicate_char} is repeating characters")


sentences = input("Give me a sentence: ")
word = sentences.split()

for item in word:
    determineIsogram(item)

determineIsogram(sentences)

