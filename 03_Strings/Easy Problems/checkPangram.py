# Check if given String is Pangram or not

# Given a string s, the task is to check if it is Pangram or not. 
# A pangram is a sentence containing all letters of the English Alphabet.

# Examples: 

# Input: s = "The quick brown fox jumps over the lazy dog" 
# Output: true
# Explanation: The input string contains all characters from ‘a’ to ‘z’.

# Input: s = "The quick brown fox jumps over the dog"
# Output: false
# Explanation: The input string does not contain all characters from ‘a’ to ‘z’, as ‘l’, ‘z’, ‘y’ are missing

# 1. [Naive Approach] By Searching for each Character - O(MAX_CHAR* n) Time and O(1) Space

# The idea is to iterate over all characters from 'a' to 'z' and for each character, check if it is present in the input string or not. If any character is not present in the input string, return false. Otherwise, return true. Also, we need to ignore the case while searching for a character('a' and 'A' are considered same).

from string import ascii_lowercase

def checkPangram(s):

   
    for ch in ascii_lowercase:
        found = False
        
        for i in range(len(s)):
            if ch == (s[i].lower()):
                found = True
                break
        
        if found == False:
            return False
    return True

s = "The quick brown fox jumps over the lazy dog"
if checkPangram(s) == True:
    print("true")
else:
    print("false")
# true