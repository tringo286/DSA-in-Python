# Frequency of Characters in Alphabetical Order

# Given a string s, the task is to print the frequency of each of the characters of s in alphabetical order.
# Example: 

# Input: s = "aabccccddd" 
# Output: a2b1c4d3 
# Since it is already in alphabetical order, the frequency 
# of the characters is returned for each character. 

# Input: s = "geeksforgeeks" 
# Output: e4f1g2k2o1r1s2 

# 1. Expected Approach 1 - Using Hash Map or Dictionary - O(n) Time and O(CHAR_SIZE) Space

# Create a Hash Map and store the frequency of each of the characters of the given string.
# Finally, print the frequency of each of the character in alphabetical order.
# Note the CHAR_SIZE is alphabet size of input characters which is typically a constant. If we have only lower case characters, then CHAR_SIZE is 26 only. If we consider all ASCII characters, then CHAR_SIZE is 256.

# Python3 implementation of the approach 
MAX = 26; 

# Function to print the frequency 
# of each of the characters of 
# s in alphabetical order 
def compressString(s, n) :

    # To store the frequency 
    # of the characters 
    freq = [ 0 ] * MAX; 

    # Update the frequency array 
    for i in range(n) :
        freq[ord(s[i]) - ord('a')] += 1; 

    # Print the frequency in alphatecial order 
    for i in range(MAX) : 

        # If the current alphabet doesn't 
        # appear in the string 
        if (freq[i] == 0) :
            continue; 

        print((chr)(i + ord('a')),freq[i],end = " "); 

# Driver code 
if __name__ == "__main__" : 

    s = "geeksforgeeks"; 
    n = len(s); 

    compressString(s, n); 

# e 4 f 1 g 2 k 2 o 1 r 1 s 2 