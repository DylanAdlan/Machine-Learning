"""
Problem 1:
A pangram is a sentence using every letter of the alphabet at least once. It is case insensitive, so it doesn't matter if a letter is lower-case (e.g. k) or upper-case (e.g. K).
For this exercise, a sentence is a pangram if it contains each of the 26 letters in the English alphabet.
Example: The quick brown fox jumps over the lazy dog.

Your task is to figure out if a sentence is a pangram.

"""


# set yang contains all alphabets
alphabets = {'a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

sentences = input("Enter a sentence: ")

# to get unique values using set
set_sentences = set(sentences)
print(set_sentences)

# intersect values dlm set_sentences dengan alphabets 
# utk buang spaces and other characters selain alphabets
common_chars = set_sentences & alphabets  
# atau guna set_sentences.intersection(alphabets)

print("Common characters:", common_chars)



# print(set_sentences)

# comparekan length sentences set dengan length alphabets set
# kalau sama, meaning sentences enteres contains all alphabets
if len(common_chars) == len(alphabets):
  print("The sentence is a pangram")
else:
  print("The sentence is not a pangram")



#CHATGPT method

import string

# create isParagram and pass sentence value to check whether 
# that sentence paragram or not
def isParagram(sentence):

  # convert the sentence to lowercase
  sentence = sentence.lower()

  # convert string sentence to set to remove duplicate values
  set_sentence = set(sentence)
  # create a variable to store all English alphabet
  # string.ascii_lowercase is "abcdefghijklmnopqrstuvwxyz"
  # make them into set to avoid duplicate values
  alphabet = string.ascii_lowercase
  alphabet_set = set(alphabet)

  return alphabet_set.issubset(set_sentence)


# example usage
sentence = "The quick brown fox jumps over the lazy dog"
print(isParagram(sentence)) # output :TRUE

sentence = "Adnin Adlan"
print(isParagram(sentence)) # output :FALSE







