"""
Concatenation of Strings
Fun with “Strings” at Chicago technologies.
The official heads of chicago technologies thought only working would tire the employees 
so they arranged some game for relaxation.
Game 1:
Rules were as follows:
• String 1 should define the person and the first letter of the string 1 
should be same as the first letter of String 2
• String 2 should be the person’s name.
• Output String should be the concatenation of both the input strings."""

name = input("Enter the first string:")
word = input("Enter the second string:")

# make them into list datatype
list_name = list(name) 
list_word = list(word)


if list_name[0] == list_word[0]:
    print(f"{name} {word}")
else:
    print("Invalid input")







