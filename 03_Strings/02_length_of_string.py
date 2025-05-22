# Given a string s, the task is to find the length of the string.

# Examples:

# Input: s = "abc"
# Output:  3

# Input: s = "GeeksforGeeks"
# Output: 13

# Input: s = ""
# Output: 0

# 1. Using In-built methods

# Python code to demonstrate string length
# using len

s = "gfg"
print(len(s)) # 3
 
# 2. Traversing method

# Function to calculate length of a string
def get_length(s):
    cnt = 0
    for c in s:
        cnt += 1
    
    return cnt

# Driver code
s = "GeeksforGeeks"
print(get_length(s)) # 13