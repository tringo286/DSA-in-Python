# Search a Character in a String
# Given a character ch and a string s, the task is to find the index of the first occurrence of the character in the string. If the character is not present in the string, return -1.

# Examples:

# Input: s = "geeksforgeeks", ch = 'k'
# Output: 3
# Explanation: The character 'k' is present at index 3 and 11 in "geeksforgeeks", but it first appears at index 3.

# Input: s = "geeksforgeeks", ch = 'z'
# Output: -1
# Explanation: The character 'z' is not present in "geeksforgeeks".

# 1. Approach - By traversing the string - O(n) Time and O(1) Space

def findChar(s, ch):
    n = len(s)
    for i in range(n):
      
        # If the current character is equal to ch, 
        # return the current index
        if s[i] == ch:
            return i

    # If we did not find any occurrence of ch,
    # return -1
    return -1

s = "geeksforgeeks"
ch = 'k'

print(findChar(s, ch)) # 3

# 2. Approach - By Using in-built library functions - O(n) Time and O(1) Space

def find_character_index(s, ch):
    idx = s.find(ch)
    return idx 

s = "geeksforgeeks"
ch = 'k'

index = find_character_index(s, ch)
print(index) # 3
   