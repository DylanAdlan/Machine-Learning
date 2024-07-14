'''"""
video 1 filter() function
"""
def starts_with_r(friends):
    return friends.startswith("R")

friends = ["Rolf", "Jose", "Randy", "Anna", "Mary", "maRy"]
starts_with_r = filter(starts_with_r, friends) # arg 1 : function that return True/False
# start_with_r = filter(lambda friend : friend.startswith("R"), friends)
starts_with_r = (f for f in friends if f.startswith("R"))
print(list(starts_with_r))
print(next(starts_with_r))
# print(next(starts_with_r))
# print(next(starts_with_r))
# print(next(starts_with_r))

'''

"""
to work with Regular expression -> use built in package "re" atau module re
import re

 ======== 
.search() function, utk return yg ada Match object in the string

.span() returns a tuple containing the start-, and end positions of the match.

eg:
import re

#Search for an upper case "S" character in the beginning of a word, and print its position:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

output: (12, 17)

============

.string returns the string passed into the function (return whole string)

eg:
import re

#The string property returns the search string: 

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

output: The rain in Spain

=============

.group() returns the part of the string where there was a match

eg:
import re

#Search for an upper case "S" character in the beginning of a word, and print the word:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

output: Spain

==============
using findall = macam nk check match tak
metacharacters
[] = set of characters
\ = utk signal special sequence/ to escape character
. = any character
^ = start with
$ = end with


[] = return set of characters

eg:
import re

txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt) # nk lower case alphabet a sampai m
print(x)

output: ['h', 'e', 'a', 'i', 'i', 'a', 'i']

====================

\d = return all digit characters

eg:
import re

txt = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)

output: ['5', '9']

======================

import re

txt = "hello planet"

#Check if the string ends with 'planet':

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")










#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

iexplore

1. 
We can handle Unpredictable Output using doctest 
- True

2.
What does the function re.search do?
- Matches a pattern at any position in the string

3.
________ matches the start of the string.
________ matches the end of the string.

- ‘^’, ‘$’

4.
Which of the following functions results in case insensitive matching?
- re.I

5.
What does the function re.match do?
- Matches a pattern at the start of the string

6.
What will be the output of the following Python code?
import re
re.ASCII 
- 256

7.
Which module in Python supports regular expressions?
- re

8.
import re
sentence = 'we are humans'
matched = re.match(r'(.*) (.*?) (.*)', sentence)
print(matched.groups())

- (‘we’, ‘are’, ‘humans’)

9.
import re
sentence = 'horses are fast'
regex = re.compile('(?P<animal>\w+) (?P<verb>\w+) (?P<adjective>\w+)')
matched = re.search(regex, sentence)
print(matched.groupdict())

- {‘animal’: ‘horses’, ‘verb’: ‘are’, ‘adjective’: ‘fast’}

10.
import re
print(re.split('\W+', 'Hello, hello, hello.'))
- [‘Hello’, ‘hello’, ‘hello’, ”]

ianalyse

1.
sys.path.append('/root/mods') 
- used for adds a new directory to seach for python modules that are imported

2.
The name of the script is stored in
- sys.argv[0]

3.
The pattern ^$ will match
- Any empty line

4.
Direct a stderr object to be written to a standard output object in python module
- sys.stderr=sys.stdout

5.
What does re.match() do?
- searches for Regular expression at the Start of string only

6. 
Function allows to run test cases in python
- unittest.main()

7.
time.clock() has a granularity of
- 1/100 th of a second

8.
In Python Regular expressions,Which character implies beginning of a string?
- ^

9.
matches a blank line
- ^ $

10.
import /tmp/mymod.py
- Add and export /tmp to PYTHONPATH and then import mymod


#----------------------------------------------------------------

idesign

1.
create pattern utk offer code
condition - contains all vowels (aeiou)

import re

def checkPatternOffercode(input_user):

    vowels = set(aeiou) # {'a', 'e', 'i', 'o', 'u'}

    words = re.findall(r"\b\w+\b", string)

    # r => akn treat baclashes as ada meaning and bukan hnya escape character
    # \b => at first utk match dgn begin ayat tu, xspecify kna start dgn apa, tpi blh smua(letter, digit, underscore only)
    # \w+ => \w utk [a-zA-z0-9_], ada "+" utk more that one
    # \b => at the end utk match jgk dkat end of word 

    for word in words:
        set_word = set(word)

        if vowels.issubset(set_word):
            print("Accepted")

        else:
            print("Not Accepted")

input_user = input().strip().lower().replace(" ","")
# .strip() => remove trailing whitespace
# .lower() => convert to lowercase
# .replace(" ","") => remove all spaces antra string, bukan hnya yg trailing

checkPatternOffercode(input_user)

#---------------------------------------------------------------------------------------------

3.
Valid phone detect, to avoid spam call
valid(condition) - start "+91", followed by 10 digits

^ => menunjukkan start of ayat
\+91 => utk match string +91, and escape meaning sign of +
- => match the hypen("-")
\d => mkna utk digit [0-9]
{10} => specifiy \d kna appear 10 kali
$ => represent end of line (ayat)

import re

def checkValidcall(input_user):
    
    pattern = r"^\+91-\d{10}$"

    if re.match(pattern, input_user): # kalau input user match dgn pattern
      return "Not a Spam Call"
    
    else:
      return "Spam Call"
    
# example usage
# input must in string
input_user = input().strip()  # ada .strip() = utk remove extra spaces

print(checkValidcall(input_user))

#----------------------------------------------------------------------
"""
#4.

# nk encrypt message
# message kan 2 words only
# to encrypt, first character s1 gabung last character of s2 then second 1st s1 gabung second last character s2 and so on, yg selebih akn go to the end 
# example = hello, hi => hiehllo

import re

def encryptString(word1, word2):
    
    word1 = re.sub(r'[^a-zA-Z]', '', word1) # ['h','e','l','l','o']
    word2 = re.sub(r'[^a-zA-Z]', '', word2) # ['h','i']

    # re.sub() => utk replace 
    # [a-zA-Z] => nk letter shaja, kalau non-letter(digit, underscore)(0-9_) 
    # akan replace by empty string, ''

    len1 = len(word1)  #5
    len2 = len(word2)  #2
    encrypt_str = []

    for i in range(max(len1, len2)): # 5
        if i < len1:
            encrypt_str.append(word1[i])
        if i < len2:
            encrypt_str.append(word2[len2-1-i]) # ambik start dri belakang

    return "".join(encrypt_str) # return in string (from list to string after join)

# example usage
word1 = input().strip()
word2 = input().strip()
print(encryptString(word1, word2))

#----------------------------------------------------------------------------

# 5. Income Tax Validation

# check PAN 
# condition - 10 digits (5 first (letters), next 4 (numerals), last(letter), MUST UPPERCASE)

import re

def checkPAN(input_user):
    
    pattern = r"^[A-Z]{5}\d{4}[A-Z]$"

    if re.match(pattern, input_user):
        return "Valid PAN Number"
    
    else:
        return "Invalid PAN Number"
    
#example usage
input_user = input().strip()
print(checkPAN(input_user))

#---------------------------------------------------------
# iaccess

1.

import re

def findNouns(input_user):
    pattern = r"\b[A-Z][a-zA-Z.]*\b"

    # [] = define character class
    # \b[A-Z] = start with uppercase character
    # [a-zA-Z.]* =  followed by any character (lowercase, uppercase or period(.)) 
    # * = zero or more (ada pun xpe, xde pun xpe)
    # tpi mmg kna start character with uppercase char
    # dia akn cari word by word 


    nouns = re.findall(pattern, input_user)

    for i in nouns:
        print(i)


# example usage
input_user = input()
findNouns(input_user)

#------------------------------------------------------

# 2. Ceaser Cipher Encryption

import re

def shift_char():

    text = input()
    next_shift = int(input())

    # initialize empty string utk store encrypt result
    encrpyt_text = ""

    for char in text:
        # convert to ascii value sbb kita xleh shift to next char guna alphabet 
        shifted_char = ord(char) + next_shift
        if shifted_char > 127:
            return "invalid"
        else:
            encrypt_char = chr(shifted_char)
            # masukkan encrypt_char dlm empty string yg kita initialize
            encrpyt_text += encrypt_char

    return encrpyt_text

# example usage
print(shift_char())













text = "amphisoft"
size = 3

result = re.sub(r"[a-zA-Z]", )





    
    
    
    

    















