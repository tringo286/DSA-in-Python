# Remove all occurrences of a character in a string
# Given a string and a character, remove all the occurrences of the character in the string.

# Examples: 

# Input : s = "geeksforgeeks"
#         c = 'e'
# Output : s = "gksforgks"

# Input : s = "geeksforgeeks"
#         c = 'g'
# Output : s = "eeksforeeks"

# Input : s = "geeksforgeeks"
#         c = 'k'
# Output : s = "geesforgees"

# 1. Using Built-In Methods
s = "ababca"
c = 'a'

# Remove all occurrences of 'c' from 's'
s = s.replace(c, '')

print(s) # bbc