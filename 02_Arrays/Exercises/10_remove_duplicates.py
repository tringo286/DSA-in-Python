# Remove duplicates from Sorted Array
# Given a sorted array arr[] of size n, the goal is to rearrange the array so that all distinct elements appear at the beginning in sorted order. Additionally, return the length of this distinct sorted subarray.

# Note: The elements after the distinct ones can be in any order and hold any value, as they don’t affect the result.

# Examples: 

# Input: arr[] = [2, 2, 2, 2, 2]
# Output: [2]
# Explanation: All the elements are 2, So only keep one instance of 2.


# Input: arr[] = [1, 2, 2, 3, 4, 4, 4, 5, 5]
# Output: [1, 2, 3, 4, 5]

# Input: arr[] = [1, 2, 3]
# Output: [1, 2, 3]
# Explanation : No change as all elements are distinct.

# 1. Using Hash Set – Works for Unsorted Also – O(n) Time and O(n) Space

def removeDuplicates(arr):
    
    # To track seen elements
    seen = set()
    
    # To maintain the new size of the array
    idx = 0

    for i in range(len(arr)):
        if arr[i] not in seen:
            seen.add(arr[i])
            arr[idx] = arr[i]
            idx += 1

    # Return the size of the array 
    # with unique elements
    return idx

if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    newSize = removeDuplicates(arr)

    for i in range(newSize):
        print(arr[i], end=" ") # 1 2 3 4 5

# 2. Expected Approach – O(n) Time and O(1) Space

def removeDuplicates(arr):
    n = len(arr)
    if n <= 1:
        return n

    # Start from the second element
    idx = 1  
    
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            arr[idx] = arr[i]
            idx += 1

    return idx

if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    newSize = removeDuplicates(arr)

    for i in range(newSize):
        print(arr[i], end=" ") # 1 2 3 4 5