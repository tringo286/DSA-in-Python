# Check if a string is substring of another

# Given two strings txt and pat, the task is to find if pat is a substring of txt. If yes, return the index of the first occurrence, else return -1.

# Examples : 

# Input: txt = "geeksforgeeks", pat = "eks"
# Output: 2
# Explanation: String "eks" is present at index 2 and 9, so 2 is the smallest index.

# Input: txt = "geeksforgeeks", pat = "xyz"
# Output: -1.
# Explanation: There is no occurrence of "xyz" in "geeksforgeeks"

# 1. Using nested loops - O(m*n) Time and O(1) Space
# The basic idea is to iterate through a loop in the string txt and for every index in the string txt, check whether we can match pat starting from this index. This can be done by running a nested loop for traversing the string pat and checking for each character of pat matches with txt or not. If all character of pat matches then return the starting index of such substring.

# Function to find if pat is a substring of txt
def findSubstring(txt, pat):
    n = len(txt)
    m = len(pat)

    # Iterate through txt
    for i in range(n - m + 1):

        # Check for substring match
        j = 0
        while j < m and txt[i + j] == pat[j]:
            j += 1
        
        # If we completed the inner loop, we found a match
        if j == m:
            return i

    # No match found
    return -1

txt = "geeksforgeeks"
pat = "eks"
print(findSubstring(txt, pat)) # 2
