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
