"""
Input and Output Format:
1st input is a number indicates a total number of elements in the list.
2nd input is a String contains a list of numbers.
3rd input is number indicates K (number of elements need to sum every time)
The output contains a set of elements after summing. ( Refer to sample output format).
 
Note: All text in bold corresponds to the input and the rest corresponds to output.
 
Sample Input and Output 1:
9
1 3 2 4 5 1 6 31 15
[1, 2, 3, 4, 5, 6, 15, 31]
3
[6, 15, 31]

"""

""" 
1. input berapa element, list of numbers and position 
4. list of number convert to int 
5. set and sort them out in ascending order (sort jdi list balik)
6. nk calculate sum of numbers ikut position then append in a new list
7. 
"""

def generate_pin_number(num_elements, elements_str, k):

    elements = list(map(int, elements_str.split()))
    #print(elements)
    
    unique_element = sorted(set(elements))

    # print(unique_element)

    pin_number = []
    length = len(unique_element)
    i = 0

    while i < length:
        totalnum = sum(unique_element[i:i+k])

    

num_elements = 9
elements_str = input()
k = int(input())
generate_pin_number(num_elements, elements_str, k)
