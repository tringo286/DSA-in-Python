# Count number of equal pairs in a string

# Given a string s, find the number of pairs of characters that are same. Pairs (s[i], s[j]), (s[j], s[i]), (s[i], s[i]), (s[j], s[j]) should be considered different. 

# Examples :

# Input: air
# Output: 3
# Explanation :
# 3 pairs that are equal are (a, a), (i, i) and (r, r)
# Input : geeksforgeeks
# Output : 31

# 1. Naive approach

# Time Complexity: O(N2), because of two nested loops
# Auxiliary Space: O(1), because no extra space has been used

# The naive approach will be you to run two nested for loops and find out all pairs and keep a count of all pairs. 

# Steps to implement-

# Find the size of the given string
# Initialize a variable let us say "ans" with value 0 to store the answer
# Run two nested "for loop" from 0 to the size of string-1
# In that nested loop if two pair of characters are the same then increment that "ans" by 1
# In last return or print the value stored in "ans"

# Function to count the number of equal pairs
def countPairs(s):
    # Length of the string
    n = len(s)

    # Initialize the answer
    ans = 0

    # Running nested loops to check equal pairs
    for i in range(n):
        for j in range(n):
            # When such pair is found
            if s[i] == s[j]:
                ans += 1

    return ans

s = "geeksforgeeks"
print(countPairs(s)) # 31

# 2. Efficient approach

# For an efficient approach, we need to count the number of equal pairs in linear time. Since pairs (x, y) and pairs (y, x) are considered different. We need to use a hash table to store the count of all occurrences of a character.So we know if a character occurs twice, then it will have 4 pairs - (i, i), (j, j), (i, j), (j, i). So using a hash function, store the occurrence of each character, then for each character the number of pairs will be occurrence^2. Hash table will be 256 in length as we have 256 characters. 

# Python3 program to count the 
# number of pairs 
MAX = 256

# Function to count the number 
# of equal pairs
def countPairs(s):
    
    # Hash table 
    cnt = [0 for i in range(0, MAX)]

    # Traverse the string and count 
    # occurrence 
    for i in range(len(s)):
        cnt[ord(s[i]) - 97] += 1

    # Stores the answer 
    ans = 0

    # Traverse and check the occurrence 
    # of every character 
    for i in range(0, MAX):
        ans += cnt[i] * cnt[i]

    return ans

s = "geeksforgeeks"
print(countPairs(s)) # 31    