# Print all possible strings that can be made by placing space

# Given a string you need to print all possible strings that can be made by placing spaces (zero or one) in between them. 

# Input:  str[] = "ABC"
# Output: ABC
#         AB C
#         A BC
#         A B C


# 1. Recursion

# The idea is to use recursion and create a buffer that one by one contains all output strings having spaces. We keep updating the buffer in every recursive call. If the length of the given string is ‘n’ our updated string can have a maximum length of n + (n-1) i.e. 2n-1. So we create a buffer size of 2n (one extra character for string termination). 
# We leave 1st character as it is, starting from the 2nd character, we can either fill a space or a character. Thus, one can write a recursive function like below.

# Python program to print permutations 
# of a given string with
# spaces.

# Utility function
def toString(List):
    s = ""
    for x in List:
        if x == '&# 092;&# 048;':
            break
        s += x
    return s

# Function recursively prints the 
# strings having space pattern.
# i and j are indices in 'str[]' 
# and 'buff[]' respectively
def printPatternUtil(string, buff, i, j, n):
    
    if i == n:
        buff[j] = '&# 092;&# 048;'
        print(toString(buff))
        return

    # Either put the character
    buff[j] = string[i]
    printPatternUtil(string, buff, i + 1, 
                                 j + 1, n)

    # Or put a space followed by next character
    buff[j] = ' '
    buff[j + 1] = string[i]

    printPatternUtil(string, buff, i + 1, 
                                 j + 2, n)

# This function creates buf[] to 
# store individual output string
# and uses printPatternUtil() to 
# print all permutations.
def printPattern(string):
    n = len(string)

    # Buffer to hold the string 
    # containing spaces
    
    # 2n - 1 characters and 1 string terminator
    buff = [0] * (2 * n)

    # Copy the first character as it is, 
    # since it will be always
    # at first position
    buff[0] = string[0]

    printPatternUtil(string, buff, 1, 1, n)

# Driver program
string = "ABCD"
printPattern(string)

# ABCD
# ABC D
# AB CD
# AB C D
# A BCD
# A BC D
# A B CD
# A B C D