# Generating All Subarrays

# Given an array arr[], the task is to generate all the possible subarrays of the given array.

# Examples: 

# Input: arr[] = [1, 2, 3]
# Output: [ [1], [1, 2], [2], [1, 2, 3], [2, 3], [3] ]

# Input: arr[] = [1, 2]
# Output: [ [1], [1, 2], [2] ]

# 1. Iterative Approach

#Prints all subarrays in arr[0..n-1]
def sub_array(arr):
    n = len(arr)

    # Pick starting point
    for i in range(n):
        # Pick ending point
        for j in range(i, n):
            # Print subarray between current starting and ending points
            for k in range(i, j + 1):
                print(arr[k], end=" ")
            print()  # New line after each subarray

# Driver code
arr = [1, 2, 3, 4]
print("All Non-empty Subarrays:")
sub_array(arr)