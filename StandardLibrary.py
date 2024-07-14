"""



iexplore

1.
How can we read value for "PI" ?

answer: 
import math
math.pi

2.
We can handle Unpredictable Output using doctest.
- True

3.
standard module for manipulating dates and times, with types such as date and time
- datetime

4.
import re
number = "987654321"
short = re.match( r'\d{3}', number)
if short:
   print (short.group())
else:
   print ("No short!!")

answer: 987

5.
odd statement
- '^ab*c$'

6.
function that allows to run test cases in python
- unittest.main()

7.
read list of all .txt files from a directory called myDir
- Using glob module

8.
matches a blank line
- ^$

9. 
specify character classes in a regular expression?
- []

10.
profile module is the standard Python profiler.
- True

ianalyse

1.
matches a blank line
- ^$

2.
time.clock() has a granularity of
- 1/100 th of a second

3.
re.match() is used for
- searches for Regular expression at the Start of string only

4.
direct a stderr object 
to be written to a standard output object in python module
- sys.stderr=sys.stdout

5.
The name of the script is stored in
- sys.argv[0]

6.
sys.path.append('/root/mods') is for
- Adds a new directory to seach for python modules that are imported

7.
how to import /tmp/mymod.py
- Add and export /tmp to PYTHONPATH and then import mymod

8.
function that allow to run test cases in python
- unittest.main()

9.
In Python Regular expressions,
Which character implies beginning of a string
- ^

10.
The pattern ^$ will match
- an empty line

#-----------------------------------------------------------

#iaccess

# Operating System Interface
import os # provide functions to interact with operating system

print(dir(os))

print(help(os))


#-------------------------------------------------------

import shutil  # provides a higher level interface

print(shutil.copyfile('data.db', 'archieve.db'))

print(shutil.move('/build/executables', 'installdir'))

#--------------------------------------------------------

# File wildcards

import glob # provides a function for making file lists from directory wildcard

print(glob.glob('*.py'))


#---------------------------------------------------

# Command Line Arguments

import sys
print(sys.argv)



import argparse # provides more sophisticated mechanism to process command line arguments

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()

print(args)

#--------------------------------------------------------
# Error Output Redirection and Program Termination

sys.stderr.write('Warning, log file not found starting a new one\n')


#-----------------------------------------------

# String Pattern Matching (Regular expression)

import re

# Date
"""
import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()
print(current_datetime)

# Display current date and time in different formats

print("Current Date and Time (ISO Format):", current_datetime.date())
print("Current Date:", current_datetime.date())
print("Current Time:", current_datetime.time())
print("Formatted Date and Time:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))


# current time only
print(current_datetime.time())

#---------------------------------------------------------
# iaccess

'''1.
Date Decoder I

Madhumitha was working as an Accountant in BINNI mills Pvt Ltd, Coimbatore. She was in charge of crediting salary for all the employees, summarising the current financial status by collecting information, preparing balance sheet, profit, and loss statement, and other reports.

That particular day she was assigned to generate a report that contains the Date of Joining of employees between years 1980 - 2015 in the format (yyyy, MMM,dd). But the date of joining which is available in the present datasheet is in the format DD-MMM-YY. Help her to convert the date of joining of all the employees to (DD, MMM, yyyy) format by writing a program.

Note :
Create a dictionary suitable for decoding month names to numbers.
Months in a dictionary should be in the following format: JAN for January, FEB for February, MAR for March and so on..

Create a  function named date_decoder( ) that takes a date in the "dd-MMM-yy" format as its argument. Translate the month, correct the year to include all of the digits and respond with the format of (yyyy,MMM,dd).

Input format:
Input is a string that contains the date in the format DD-MMM-YY format.

Output format :
The output is the translated form of the input date string in the format (yyyy, MMM, dd) as a tuple.
and display whether the year is a leap year or not

Note: Refer to sample input and output for further formatting specifications.

Sample Input 1 :
85-MAR-19

Sample Output 1 :
 (19, 03, 1985) is not a leap year


Sample Input 2 :
04-DEC-12

Sample Output 2 :
(12, 12, 2004) is a leap year'''
def date_decoder():
    
   months = {"JAN": "01", "FEB": "02", "MAR": "03", "APR": "04", "MAY": "05", "JUN": "06", "JUL": "07", "AUG": "08", "SEP": "09", "OCT": "10", "NOV": "11", "DEC": "12"}

   date = input() # in format [dd-MMM-yy]
   year, month, day = date.split("-")

   # format month
   month = months[month] # JAN => 01

   # format year
   year = int(year) # bcs in string
   if year <=99:  
      if year >= 80:
         year = 1900 + year
      else:
         year = 2000 + year

   # check leap year
   is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

   # format the output
   output_date = (int(day), month, year)

   # display leap year status
   leap_year_status = "is a leap year" if is_leap_year else "is not a leap year"

   return f"({output_date[0]}, {output_date[1]}, {output_date[2]}) {leap_year_status}"

# example usage
print(date_decoder())   

#---------------------------------------------------------------

#2.
'''Suresh playing a numbers game. The game description is  Suresh picks random numbers and calculate the sum of all numbers, and the problem is some times the sum of the numbers will be float value and he wants to modify that sum by using Floor(), Ceil(), Round() functions and finally, he wants to calculate the difference of these 3 functions.



 

Input Format specifications:

Input consists of a list of values separated by space.
Output Format Specifications:

The first line of output should be the difference between floor()sum - ceil()sum.
Secondly of output should be the difference between the ceil()sum - round()sum.
The third line of output should be the difference between floor()sum - round()sum.
Constraints:

Use only floor() and ceil() round() function Python


Sample Input 1:
23.34 12 25

Sample Output 1:
-1.0
1.0
0.0

Sample Input 2:
-21.23 -18.23 -12

Sample Output 2:
-1.0
0.0
-1.0'''

import math

def calculate_sum_differences(numbers):
    numbers = list(map(float, numbers.split()))
    
    total_sum = sum(numbers)
    floor_sum = math.floor(sum(numbers))
    ceil_sum = math.ceil(sum(numbers))
    round_sum = round(total_sum)
    
    diff_floor_ceil = float(floor_sum - ceil_sum)
    diff_ceil_round = float(ceil_sum - round_sum)
    diff_floor_round = float(floor_sum - round_sum)
    
    return diff_floor_ceil, diff_ceil_round, diff_floor_round

# Example usage:
input_data = input()
diff1, diff2, diff3 = calculate_sum_differences(input_data)
print(diff1)
print(diff2)
print(diff3)
