
# create a fx to pass a string and calculate count
def char_counts(s):

    # susun dlm ascending order
    s = sorted(s)
    # print(s)

    # create an empty dictionary to store our characters and its count
    char_count_dict = {}

    for char in s: # string is iterable object
        if char in char_count_dict: # kalau character dh ade dlm dict, then dia akn tmbh 1
            char_count_dict[char] +=1
        else:
            char_count_dict[char] = 1 # kalau belum ada, dia akn start with 1

    print(f"Dictionary of string:{char_count_dict}")

    for key, value in char_count_dict.items():
        print(f"{key}--{value}")


# example usage
string = input()
char_counts(string)