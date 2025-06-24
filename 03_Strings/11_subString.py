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

# 2. [Interesting Approach] - Using Recursion

# The idea is to recursively generate all possible substrings of the given string s. To do so, create an array of string res[] to store the substrings of string s and an empty string cur to store the current string. Start from the 0th index and for each index ind, add the current character s[ind] in the string cur, and add the string cur in res[]. Then, move to index ind + 1, and recursively generate the all substrings. At each recursive call, check if string cur is empty, if so, skip the current character to start the string from next index ind + 1. At last print all the substrings.

# Python program to find all the
# substrings of given string

# Recursive Function to find all
# substrings of a string
def subString(s, n, index, cur, res):

    # if we have reached the
    # end of the string
    if index == n:
        return

    # add the character s[index]
    # to the current string
    cur += s[index]

    # add the current string in result
    res.append(cur)

    # move to next index
    subString(s, n, index + 1, cur, res)

    # remove the current character
    # from the current string
    cur = cur[:-1]

    # if current string is empty
    # skip the current index to
    # start the new substring
    if not cur:
        subString(s, n, index + 1, cur, res)

# Function to find all substrings
def findSubstrings(s):

    # to store all substrings
    res = []

    # to store current string
    cur = ""
    subString(s, len(s), 0, cur, res)
    return res

s = "abc"
res = findSubstrings(s)
print(" ".join(res)) # a ab abc b bc c 