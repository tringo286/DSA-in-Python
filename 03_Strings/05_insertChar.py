# Insert a character in String at a Given Position

# Given a string s, a character c and an integer position pos, the task is to insert the character c into the string s at the specified position pos.

# Examples:

# Input: s = "Geeks", c = 'A', pos = 3
# Output: GeeAks

# Input: s = "HelloWorld", c = '!', pos = 5
# Output: Hello!World

# 1. Using Built-In Methods - O(n)

def insertChar(s, c, pos):
  
    # Insert character at specified position
    return s[:pos] + c + s[pos:]

s = "Geeks"
print(insertChar(s, 'A', 3)) # GeeAks

# 2.  Using Custom Method - O(n)    

# First, iterate through the given string, inserting all the characters into a new string until we reach the position where the given character needs to be inserted. At that position, insert the character, and then append the remaining characters from the input string to the new string.

def insertChar(string, char, position):
    newString = ""

    for i in range(len(string)):
        if  i == position:
            newString += char

        newString += string[i]

    if position >= len(string):
        newString += char   

    return newString

s = "Geeks"
print(insertChar(s, 'A', 3)) # GeeAks
print(insertChar(s, 'A', 10)) # GeeksA