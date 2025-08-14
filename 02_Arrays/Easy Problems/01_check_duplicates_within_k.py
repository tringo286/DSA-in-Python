# Duplicate within K Distance in an Array

# Given an integer array arr[] and an integer k, determine whether there exist two indices i and j such that arr[i] == arr[j] and |i - j| ≤ k. If such a pair exists, return 'Yes', otherwise return 'No'.

# Examples: 

# Input: k = 3, arr[] = [1, 2, 3, 4, 1, 2, 3, 4]
# Output: No
# Explanation: Each element in the given array arr[] appears twice and the distance between every element and its duplicate is 4.

# Input: k = 3, arr[] = [1, 2, 3, 1, 4, 5]
# Output: Yes
# Explanation: 1 is present at index 0 and 3.

# Input: k = 3, arr[] = [1, 2, 3, 4, 5]
# Output: No
# Explanation: There is no duplicate element in arr[].

# 1. [Naive Approach] - O(n * k) Time and O(1) Space

# The idea is to run two loops. The outer loop picks every index i as a starting index, and the inner loop compares all elements which are within k distance of i, i.e. i + k.

def check_duplicates_within_k(arr, k):
    n = len(arr)

    # Traverse for every element
    for i in range(n):
      
        # Traverse next k elements
        for c in range(1, k + 1):
            j = i + c
            
            # If we find one more occurrence within k
            if j < n and arr[i] == arr[j]:
                return True
              
    return False

# Driver method to test above method
arr = [10, 5, 3, 4, 3, 5, 6]
print("Yes" if check_duplicates_within_k(arr, 3) else "No") # Yes