# Reverse a String 

# Given a string s, the task is to reverse the string. Reversing a string means rearranging the characters such that the first character becomes the last, the second character becomes second last and so on.

# Examples:

# Input: s = "GeeksforGeeks"
# Output: "skeeGrofskeeG"
# Explanation : The first character G moves to last position, the second character e moves to second-last and so on.

# Input: s = "abdcfe"
# Output: "efcdba"
# Explanation: The first character a moves to last position, the second character b moves to second-last and so on. 

# 1. Using backward traversal – O(n) Time and O(n) Space

# The idea is to start at the last character of the string and move backward, appending each character to a new string res. This new string res will contain the characters of the original string in reverse order.

def reverseString(s):
    res = []
  
    # Traverse on s in backward direction
    # and add each character to the list
    for i in range(len(s) - 1, -1, -1):
        res.append(s[i])

    # Convert list back to string
    return ''.join(res)

s = "abdcfe"
print(reverseString(s)) # efcdba
   