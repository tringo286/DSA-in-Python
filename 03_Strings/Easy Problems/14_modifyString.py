# Find Character Frequencies in Order of Occurrence

# Given string s containing only lowercase characters, the task is to print the characters along with their frequency in the order of their occurrence and in the given format explained in the examples below.

# Examples: 

# Input: s = "geeksforgeeks"
# Output: g2 e4 k2 s2 f1 o1 r1

# Input: str = "elephant"
# Output: e2 l1 p1 h1 a1 n1 t1

# 1. [Naive Approach] Using Nested Loops - O(n^2) Time and O(1) Space

# Traverse through every character and count frequency of it using one more loop inside the main traversal loop. To ensure that we do not have repeated characters in output, check if the character is already seen. If already seen, then ignore the character.

# Python Code to find character frequencies in order of
# occurrence using Nested Loops

# function to modify the string by appending 
# character with its frequency in order of occurrence
def modifyString(s):
    
    res = ""
    n = len(s)
    
    # loop through the string
    for i in range(n):
        
        # count the occurrence of s[i]
        count = 1  
        
        # check if the character has been 
        # processed already
        seen = False
        for j in range(i):
            if s[j] == s[i]:
                seen = True
                break
        
        if seen: continue; 
        
        # count frequency of s[i]
        for j in range(i + 1, n):
            if s[j] == s[i]:
                count += 1
        
        # append character and its frequency 
        # to the result
        res += s[i] + str(count) + " "
    
    return res

s = "geeksforgeeks"
print(modifyString(s)) # g2 e4 k2 s2 f1 o1 r1 

# 2. [Expected Approach 1] Use Hash Map or Dictionary - O(n) Time and O(MAX_CHAR) Space

# 1) Store Frequencies of all characters in a map.
# 2) Traverse through the string, append the character and its frequency to the result and make frequency as 0 to avoid repetition.

# Note the MAX_CHAR is alphabet size of input characters which is typically a constant. If we have only lower case characters, then MAX_CHAR is 26 only. If we consider all ASCII characters, then MAX_CHAR is 256.

# Python Code to find character frequencies in order of
# occurrence using Hash Map
def modifyString(str):

    # Store all characters and their frequencies
    # in dictionary
    d = {}
    for i in str:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    # Print characters and their frequencies in
    # same order of their appearance
    for i in str:

        # Print only if this character is not printed
        # before.  
        if d[i] != 0:
            print("{}{}".format(i,d[i]), end =" ")
            d[i] = 0
     
if __name__ == "__main__" :
    
    str = "geeksforgeeks"
    modifyString(str)

# g2 e4 k2 s2 f1 o1 r1 
