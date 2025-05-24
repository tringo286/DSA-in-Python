# Remove a Character from a Given Position

# Given a string and a position (0-based indexing), remove the character at the given position.

# Examples: 

# Input : s = "abcde",  pos = 1
# Output : s = "acde"

# Input : s = "a",  pos = 0
# Output : s = ""

# 1. Approach - By Using Built-In Methods - O(n)

def remove_char_at_position(s, pos):
    if pos < 0 or pos >= len(s):
        return s
    return s[:pos] + s[pos+1:]

s = "abcde"
pos = 1
print("Output:", remove_char_at_position(s, pos)) # acde

# 2. Approach - By Writing Your Own Method - O(n)

# Remove character at specified position using a loop

def remove_char_at_position(s, p):
  
    # Check for valid position
    if p < 0 or p >= len(s): 
        return s

    # Convert string to list for mutable operations
    s_list = list(s)  
    
    # Shift characters to the left from the position
    for i in range(p, len(s) - 1):
        s_list[i] = s_list[i + 1]

    # Remove the last character
    s_list.pop()  
    
    return ''.join(s_list) 
  
s = "abcde" 
p = 1 
s = remove_char_at_position(s, p)  
print(s) # acde

# for i in range(1, 4):  # i = 1, 2, 3
# i = 1: s_list[1] = s_list[2] → s_list = ['a', 'c', 'c', 'd', 'e']

# i = 2: s_list[2] = s_list[3] → s_list = ['a', 'c', 'd', 'd', 'e']

# i = 3: s_list[3] = s_list[4] → s_list = ['a', 'c', 'd', 'e', 'e']
