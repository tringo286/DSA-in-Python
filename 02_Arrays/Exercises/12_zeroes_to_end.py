# Move all zeros to end of array

# Given an array of integers arr[], the task is to move all the zeros to the end of the array while maintaining the relative order of all non-zero elements.

# Examples: 

# Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
# Output: arr[] = [1, 2, 4, 3, 5, 0, 0, 0]
# Explanation: There are three 0s that are moved to the end.

# Input: arr[] = [10, 20, 30]
# Output: arr[] = [10, 20, 30]
# Explanation: No change in array as there are no 0s.

# Input: arr[] = [0, 0]
# Output: arr[] = [0, 0]
# Explanation: No change in array as there are all 0s.

# 1. [Naive Approach] Using Temporary Array - O(n) Time and O(n) Space

# The idea is to create a temporary array of same size as the input array arr[]. 

# First, copy all non-zero elements from arr[] to the temporary array. 
# Then, fill all the remaining positions in temporary array with 0.
# Finally, copy all the elements from temporary array to arr[].

def pushZerosToEnd(arr):
    n = len(arr)
    temp = [0] * n  
    
    # to keep track of the index in temp[]
    j = 0

    # Copy non-zero elements to temp[]
    for i in range(n):
        if arr[i] != 0:
            temp[j] = arr[i]
            j += 1

    # Fill remaining positions in temp[] with zeros
    while j < n:
        temp[j] = 0
        j += 1

    # Copy all the elements from temp[] to arr[]
    for i in range(n):
        arr[i] = temp[i]

    return arr

arr = [1, 2, 0, 4, 3, 0, 5, 0]
print(pushZerosToEnd(arr)) # [1, 2, 4, 3, 5, 0, 0, 0]

# 2. [Better Approach] Two Traversals - O(n)
# The idea is to move all the zeros by traversing the array twice.

# First Traversal: Shift non-zero elements

# Traverse the array and maintain the count of non-zero elements. This count is initialized with 0 and keeps track of where the next non-zero element should be placed in the array.
# If the element is non-zero, place it at arr[count] and increment count by 1.
# After traversing all the elements, all non-zero elements will be shifted to the front while maintaining their original order.
# Second Traversal: Fill remaining positions with zeros

# After the first traversal, all non-zero elements will be at the start of the array and count will store the index where the first zero should be placed.

def pushZerosToEnd(arr):
    
    # Count of non-zero elements
    count = 0  

    # If the element is non-zero, replace the element at
    # index 'count' with this element and increment count
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    # Now all non-zero elements have been shifted to
    # the front. Make all elements 0 from count to end.
    while count < len(arr):
        arr[count] = 0
        count += 1
    
    return arr

arr = [1, 2, 0, 4, 3, 0, 5, 0]
print(pushZerosToEnd(arr)) # [1, 2, 4, 3, 5, 0, 0, 0]  

# 3. [Expected Approach] One Traversal - O(n)

# The idea is similar to the previous approach where we took a pointer, say count to track where the next non-zero element should be placed. However, on encountering a non-zero element, instead of directly placing the non-zero element at arr[count], we will swap the non-zero element with arr[count]. This will ensure that if there is any zero present at arr[count], it is pushed towards the end of array and is not overwritten.

def pushZerosToEnd(arr):
    
    # Pointer to track the position for next non-zero element
    count = 0
    
    for i in range(len(arr)):
        
        # If the current element is non-zero
        if arr[i] != 0:
            
            # Swap the current element with the 0 at index 'count'
            arr[i], arr[count] = arr[count], arr[i]
            
            # Move 'count' pointer to the next position
            count += 1
    
    return arr

arr = [1, 2, 0, 4, 3, 0, 5, 0]
pushZerosToEnd(arr)