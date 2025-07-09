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

# 2. By Reversing String - O(n) time and O(n) space

# According to the definition of a palindrome, a string reads the same both forwards and backwards. So, we can use this idea and compare the reversed string with the original one.

# If they are the same, the string is a palindrome, and then returns 1.
# If they are different, then returns 0, meaning it's not a palindrome.

def is_palindrome(s):
  
    #If reverse string is equal to given string,
    # then it is palindrome.
    return 1 if s == s[::-1] else 0

# Driver code
s = "abba"
print(is_palindrome(s)) # 1