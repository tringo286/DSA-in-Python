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

# 2. [Expected Approach] - Using HashSet - O(n) Time and O(k) Space

# The idea is to use HashSet to store elements of the array arr[] and check if there is any duplicate present within a k distance. Also remove elements that are present at more than k distance from the current element. Following is a detailed algorithm.

# Create an empty HashSet. 
# Traverse all elements from left to right. Let the current element be 'arr[i]' 
# If the current element 'arr[i]' is present in a HashSet, then return true. 
# Else add arr[i] to hash and remove arr[i-k] from hash if i >= k


# Python 3 program to Check if a given array 
# contains duplicate elements within k distance
# from each other 
def checkDuplicatesWithinK(arr, n, k):

    # Creates an empty list
    myset = set()

    # Traverse the input array
    for i in range(n):
    
        # If already present n hash, then we 
        # found a duplicate within k distance
        if arr[i] in myset:
            return True

        # Add this item to hashset
        myset.add(arr[i])

        # Remove the k+1 distant item
        if (i >= k):
            myset.remove(arr[i - k])
    return False

# Driver Code
if __name__ == "__main__":
    
    arr = [10, 5, 3, 4, 3, 5, 6]
    n = len(arr)
    if (checkDuplicatesWithinK(arr, n, 3)):
        print("Yes")
    else:
        print("No")

# Yes 