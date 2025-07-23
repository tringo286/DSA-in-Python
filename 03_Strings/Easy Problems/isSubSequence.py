# Check if one string is subsequence of other
# Given two strings s1 and s2, find if the first string is a Subsequence of the second string, i.e. if s1 is a subsequence of s2.  A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.

# Examples : 

# Input: s1 = "AXY", s2 = "ADXCPY"
# Output: True 
# All characters of s1 are in s2 in the same order

# Input: s1 = "AXY", s2 = "YADXCP"
# Output: False 
# All characters are present, but order is not same.

# Input: s1 = "gksrek", s2 = "geeksforgeeks"
# Output: True

# 1. Iterative Solution

# Time Complexity: O(n)
# Auxiliary Space: O(1)

# The idea is to use two pointers, one pointer will start from start of s1 and another will start from start of s2. If current character on both the indexes are same then increment both pointers otherwise increment the pointer which is pointing s2.

# Follow the steps below to solve the problem:

# Initialize the pointers i and j with zero, where i is the pointer to s1 and j is the pointer to s2.
# If s1[i] = s2[j] then increment both i and j by 1.
# Otherwise, increment only j by 1.
# If i reaches the end of s1 then return TRUE else return FALSE.

def issubsequence(s1, s2):

    n, m = len(s1), len(s2)
    i, j = 0, 0
    while (i < n and j < m):
        if (s1[i] == s2[j]):
            i += 1
        j += 1

    # If i reaches end of s1,that mean we found all
    # characters of s1 in s2,
    # so s1 is subsequence of s2, else not
    return i == n

s1 = "gksrek"
s2 = "geeksforgeeks"
if (issubsequence(s1, s2)):
    print("gksrek is subsequence of geekforgeeks")
else:
    print("gksrek is not a subsequence of geekforgeeks")

# Yes 

# 2. Using Recursion:

# Time Complexity: O(n), The recursion will call at most n times.
# Auxiliary Space: O(n) for recursion call stack.

# We match last characters of the two strings s1 and s2 of lengths m and n

# If the last characters match, we call for m-1 and n-1
# Otherwise, we ignore the last character of s2 and therefore call for m and n-1.

def isSubSequence(string1, string2, m, n):
    # Base Cases
    if m == 0:
        return True
    if n == 0:
        return False

    # If last characters of two
    # strings are matching
    if string1[m-1] == string2[n-1]:
        return isSubSequence(string1, string2, m-1, n-1)

    # If last characters are not matching
    return isSubSequence(string1, string2, m, n-1)

string1 = "gksrek"
string2 = "geeksforgeeks"

if isSubSequence(string1, string2, len(string1), len(string2)):
    print("Yes")
else:
    print("No")

# Yes 