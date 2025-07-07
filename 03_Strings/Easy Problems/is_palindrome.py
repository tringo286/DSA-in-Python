# Palindrome String

# Given a string s, the task is to check if it is palindrome or not.

# Example:

# Input: s = "abba"
# Output: 1
# Explanation: s is a palindrome

# Input: s = "abc" 
# Output: 0
# Explanation: s is not a palindrome

# 1. Using Two-Pointers - O(n) time and O(1) space
# The idea is to keep two pointers, one at the beginning (left) and the other at the end (right) of the string.

# Then compare the characters at these positions. If they don't match, the string is not a palindrome, and return 0.
# If they match, the pointers move towards each other (left pointer moves right, right pointer moves left) and continue checking.
# If the pointers cross each other without finding a mismatch, the string is confirmed to be a palindrome, and returns 1.

def is_palindrome(s):
    left = 0
    right = len(s) - 1

    # Continue looping while the two pointers
    # have not crossed
    while left < right:
      
        # If the characters at the current positions
        # are not equal
        if s[left] != s[right]:
            return 0

        # Move the left pointer to the right and
        # the right pointer to the left
        left += 1
        right -= 1

    # If no mismatch is found, return 1 (palindrome)
    return 1

# Driver code
s = "abba"
print(is_palindrome(s)) # 1