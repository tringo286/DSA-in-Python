# Check if two Strings are Anagrams of each other

# Given two non-empty strings s1 and s2 of lowercase letters, determine if they are anagrams — i.e., if they contain the same characters with the same frequencies.

# Examples:

# Input: s1 = “geeks”  s2 = “kseeg”
# Output: true
# Explanation: Both the string have same characters with same frequency. So, they are anagrams.

# Input: s1 = "allergy", s2 = "allergyy"
# Output: false
# Explanation: Although the characters are mostly the same, s2 contains an extra 'y' character. Since the frequency of characters differs, the strings are not anagrams.

# Input: s1 = "listen", s2 = "lists"
# Output: false
# Explanation: The characters in the two strings are not the same — some are missing or extra. So, they are not anagrams.


# 1. [Naive Approach] Using Sorting

# The idea is that if the strings are anagrams, then their characters will be the same, just rearranged. Therefore, if we sort the characters in both strings, the sorted strings will be identical if the original strings were anagrams.

def areAnagrams(s1, s2):
    
    if len(s1) != len(s2):
        return False
    
    # Sort both strings
    s1 = sorted(s1)
    s2 = sorted(s2)

    # Compare sorted strings
    return s1 == s2

if __name__ == "__main__":
    
    s1 = "geeks"
    s2 = "kseeg"
    
    if(areAnagrams(s1,s2)):
        print("true")
    else:
        print("false")

# true