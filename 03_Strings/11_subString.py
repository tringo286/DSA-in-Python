# All substrings of a given String

# Given a string s, containing lowercase alphabetical characters. The task is to print all non-empty substrings of the given string.

# Examples : 

# Input :  s = "abc"
# Output :  "a", "ab", "abc", "b", "bc", "c"

# Input :  s = "ab"
# Output :  "a",  "ab",  "b"

# Input :  s = "a"
# Output :  "a"

# 1. [Expected Approach] - Using Iteration

# The idea is to use two nested loops.
# The outer loop picks the starting index (loop for i from 0 to n-1)
# The inner loop picks the ending ending index (loop for j to n-1)

# Function to find all substrings
def find_substrings(s):
    
    # to store all substrings
    res = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            res.append(s[i:j+1])
    return res

s = 'abc'
res = find_substrings(s)
for i in res:
    print(i, end=' ') # a ab abc b bc c 