# Example list with pairs of data (in tuple)
my_list = [("a", 1), ("b", 2), ("c", 3)]

# Convert list to dictionary
my_dict = dict(my_list)

# Print the resulting dictionary
print("Resulting Dictionary:", my_dict)

################################################################################################################
# LIST IN LIST

# Example list with lists [key, value]
my_list = [["a", 1], ["b", 2], ["c", 3]]

# Convert list to dictionary using dictionary comprehension
my_dict = {item[0]: item[1] for item in my_list}

# Print the resulting dictionary
print("Resulting Dictionary:", my_dict)

###################################################################################################################

# Example list where first element is key and rest are values

my_list = ["a", 1, 2, 3]

# Extract key and values
key = my_list[0]
values = my_list[1:]

# Create dictionary
my_dict = {key: values}

# Print the resulting dictionary
print("Resulting Dictionary:", my_dict)
