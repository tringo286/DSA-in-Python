# Generating All Subarrays

# Given an array arr[], the task is to generate all the possible subarrays of the given array.

# Examples: 

# Input: arr[] = [1, 2, 3]
# Output: [ [1], [1, 2], [2], [1, 2, 3], [2, 3], [3] ]

# Input: arr[] = [1, 2]
# Output: [ [1], [1, 2], [2] ]

# 1. Iterative Approach - O(n^3)

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
arr = [1, 2, 3]
print("All Non-empty Subarrays:")
sub_array(arr) 
# 1 
# 1 2 
# 1 2 3 
# 2 
# 2 3 
# 3 

# 2. Recursive Approach - O(n^3)

# We use two pointers start and end to maintain the starting and ending point of the array and follow the steps given below: 

# Stop if we have reached the end of the array
# Increment the end index if start has become greater than end
# Print the subarray from index start to end and increment the starting index

def printSubArrays(arr, start, end):
    
    # Stop if we have reached the end of the array    
    if end == len(arr):
        return
    
    # Increment the end point and start from 0
    elif start > end:
        return printSubArrays(arr, 0, end + 1)
        
    # Print the subarray and increment the starting
    # point
    else:
        print(arr[start:end + 1])
        return printSubArrays(arr, start + 1, end)
        
# Driver code
arr = [1, 2, 3]
printSubArrays(arr, 0, 0)
# [1]
# [1, 2]
# [2]
# [1, 2, 3]
# [2, 3]
# [3]