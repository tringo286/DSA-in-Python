# Longest substring between any pair of occurrences ōf similar characters

# Given a string s, your task is to determine the length of the longest substring that lies between two identical characters in the string. The substring should exclude the characters at the two ends. If no such pair of identical characters exists, return -1.

# Examples:

# Input: s = "accabbacc"
# Output: 6
# Explanation: The matching characters are 'c' at positions 1 and 8. Substring between them is "cabbac", of length 6.

# Input: s = "aa"
# Output: 0
# Explanation: Matching characters 'a' are at positions 0 and 1. No characters in between, so length is 0.

# Input: s = "abcd"
# Output: -1
# Explanation: No repeated characters exist, hence no valid substring between same characters.

# 1. [Brute-Force Approach] Generate and Check All Substrings - O(n^2) Time and O(1) Space

# The idea is to brute-force check every possible pair of characters in the string. We iterate through all indices (i, j) where s[i] == s[j], and compute the length of the substring between them. The goal is to track the maximum length found. This approach works because we are guaranteed to consider all valid pairs due to the nested loop.

# Python program to find the length of the longest 
# substring between two identical characters 
# using Brute-Force Approach

# Function to return the length of the longest valid substring
def longestSubstring(s):

    n = len(s)
    maxLen = -1

    # Check all pairs (i, j) where s[i] == s[j]
    for i in range(n):

        for j in range(i + 1, n):

            # If matching characters found
            if s[i] == s[j]:

                # Update maximum length
                maxLen = max(maxLen, j - i - 1)

    return maxLen

if __name__ == "__main__":

    s = "accabbacc"

    print(longestSubstring(s))

# 6

# 2. [Expected Approach] Using Hashing - O(n) Time and O(1) Space

# The idea is to efficiently track the first occurrence of each character using hashing so we avoid nested loops. The thought process is that if a character repeats, the substring length between its first and last occurrence can be easily calculated. By storing the first index in a map, whenever a character repeats, we update the answer using the difference between current and stored index. 

# Steps to implement the above idea:

# Create a map to store the first occurrence index of each character in the string.
# Initialize a variable to keep track of the maximum length found between repeating characters.
# Loop through the string, checking each character's presence in the map.
# If the character is not in the map, store its current index as the first occurrence.
# If it already exists, calculate the length between current and first index, excluding the matching characters.
# Update the maximum length whenever a longer valid substring is found.
# Return the maximum length, or -1 if no repeating characters are found.

# Python program to find the length of the longest substring
# between two identical characters using Hashing

# Function to return the length of the 
# longest valid substring
def longestSubstring(s):

    firstIndex = {}
    maxLen = -1

    # Traverse the string
    for i in range(len(s)):

        # If first occurrence of character, store its index
        if s[i] not in firstIndex:
            firstIndex[s[i]] = i

        # If character seen before, update maxLen
        else:
            maxLen = max(maxLen, i - firstIndex[s[i]] - 1)

    return maxLen

s = "accabbacc"

print(longestSubstring(s)) # 6