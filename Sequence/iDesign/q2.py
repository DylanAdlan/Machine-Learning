# def make_palindrome(s):
#     # for even length
#     if len(s) % 2 == 0:
#         return s[:3] + s[::-1][3:]
#     else:
#     #     # for odd length
#         return s[:2] + s[::-1][2:]


# testing
def make_palindrome(s):
    # for even length
    if len(s) % 2 == 0:
        number = int(len(s) /2)
        return s[:number] + s[:number][::-1]
    else:
    #     # for odd length
        number = int(len(s) / 2) + 1
        return s[:number] + s[:number -1][::-1]

# example usage
s = input()
print(make_palindrome(s))

# # blackbox
# def make_palindrome(s):
#     # for even length
#     if len(s) % 2 == 0:
#     #     return s[:3] + s[::-1][3:]
#     # else:
#     #     # for odd length
#     #     return s[:2] + s[::-1][2:]
#         return s + s[::-1]
#     else:
#         return s + s[::-1][1:]
