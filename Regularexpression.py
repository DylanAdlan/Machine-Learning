"""
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




















"""