# Check for Binary String

# Given a string s, the task is to check if it is a binary string or not. A binary string is a string which only contains the characters '0' and '1'.

# Examples:

# Input: s = "01010101010"
# Output: true

# Input: s = "geeks101"
# Output: false 

# Approach:
# The idea is to iterate over all the characters of the string and if we encounter a character other than '0' or '1', then the input string is not a binary string. Otherwise, if all the characters are either '0' or '1', then the input string is a binary string.

def isBinary(s):
    for i in range(len(s)):
      
        # Check if the character is neither 
        # '0' nor '1'
        if s[i] != '0' and s[i] != '1':
            return False
    return True

s = "01010101010"
print("true" if isBinary(s) else "false") # trues