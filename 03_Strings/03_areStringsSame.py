# Check if two strings are same or not
# Given two strings, the task is to check if these two strings are identical(same) or not. Consider case sensitivity.

# Examples:

# Input: s1 = "abc", s2 = "abc" 
# Output: Yes 

# Input: s1 = "", s2 = "" 
# Output: Yes 

# Input: s1 = "GeeksforGeeks", s2 = "Geeks" 
# Output: No 

# 1. Approach - By Using (==)

# Function to compare both strings directly

def areStringsSame(s1, s2):
    return s1 == s2

s1 = "abc"
s2 = "abcd"

# Call the areStringsSame function to compare strings
if areStringsSame(s1, s2):
    print("Yes")
else:
    print("No")

# 2. Approach - By Writing your Own Method

def are_strings_equal(s1, s2):
    # Compare lengths first
    if len(s1) != len(s2):
        return False

    # Compare character by character
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True

s1 = "hello"
s2 = "hello"

if are_strings_equal(s1, s2):
    print("Yes")
else:
    print("No")