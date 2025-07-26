# Check if two strings are k-anagrams or not

# Given two strings of lowercase alphabets and a value k, the task is to find if two strings are K-anagrams of each other or not.

# Note: Two strings are called k-anagrams if the following two conditions are true. 

# Both have same number of characters.
# Two strings can become anagram by changing at most k characters in a string.
# Examples :  

# Input: str1 = "anagram" , str2 = "grammar" , k = 3
# Output: Yes
# Explanation: We can update maximum 3 values and it can be done in changing only 'r' to 'n' and 'm' to 'a' in str2.

# Input: str1 = "geeks", str2 = "eggkf", k = 1
# Output: No
# Explanation: We can update or modify only 1 value but there is a need of modifying 2 characters. i.e. g and f in str 2.

# 1. [Approach - 1] Using Map - O(n) Time and O(1) Space 

# The idea is to create a frequency map for the first string by storing character counts. Iterate through the second string, reducing the count of matching characters in the map. Finally, sum the remaining frequencies in the map, and if the total exceeds K, return false; otherwise, return true.

from collections import defaultdict

def are_k_anagrams(s1, s2, k):
    if len(s1) != len(s2):
        return False

    count = defaultdict(int)
    for ch in s1:
        count[ch] += 1

    for ch in s2:
        if count[ch] > 0:
            count[ch] -= 1

    diff_count = sum(count.values())

    if diff_count > k:
        return False
    else:
        return True

str1 = "anagram"
str2 = "grammar"
k = 2

if are_k_anagrams(str1, str2, k):
    print("Yes")
else:
    print("No")

# Yes 