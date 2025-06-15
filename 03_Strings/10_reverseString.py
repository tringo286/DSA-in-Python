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

# 2. Using Two Pointers - O(n) Time and O(1) Space

# The idea is to maintain two pointers: left and right, such that left points to the beginning of the string and right points to the end of the string. 

# While left pointer is less than the right pointer, swap the characters at these two positions. After each swap, increment the left pointer and decrement the right pointer to move towards the center of the string. This will swap all the characters in the first half with their corresponding character in the second half.

# Python program to reverse a string using two pointers

# Function to reverse a string using two pointers

def reverseString(s):
    left = 0
    right = len(s) - 1
    
    # Convert string to a list for mutability
    s = list(s)  
    
    # Swap characters from both ends till we reach
    # the middle of the string
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
    # Convert list back to string
    return ''.join(s)  

s = "abdcfe"
print(reverseString(s))
    
# 3. Using Stack - O(n) Time and O(n) Space

# The idea is to use stack for reversing a string because Stack follows Last In First Out (LIFO) principle. This means the last character you add is the first one you'll take out. So, when we push all the characters of a string into the stack, the last character becomes the first one to pop. 

def reverseString(s):
    stack = []
    
    # Push the characters into stack
    for char in s:
        stack.append(char)

    # Prepare a list to hold the reversed characters
    rev = [''] * len(s)

    # Pop the characters from stack into the reversed list
    for i in range(len(s)):
        rev[i] = stack.pop()

    # Join the list to form the reversed string
    return ''.join(rev)

s = "abdcfe"
print(reverseString(s))