# Leaders in an array
# Given an array arr[] of size n, the task is to find all the Leaders in the array. An element is a Leader if it is greater than or equal to all the elements to its right side.

# Note: The rightmost element is always a leader.

# Examples:

# Input: arr[] = [16, 17, 4, 3, 5, 2]
# Output: [17 5 2]
# Explanation: 17 is greater than all the elements to its right i.e., [4, 3, 5, 2], therefore 17 is a leader. 5 is greater than all the elements to its right i.e., [2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.


# Input: arr[] = [1, 2, 3, 4, 5, 2]
# Output: [5 2]
# Explanation: 5 is greater than all the elements to its right i.e., [2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.

# 1. [Naive Approach] Using Nested Loops – O(n^2) Time and O(1) Space:
def leaders(arr):
    n = len(arr)
    result = []

    for i in range(n):
        for j in range(i+1, n):
            if arr[i] < arr[j]:
                break
        else:
            result.append(arr[i])
    
    return result

arr = [16, 17, 4, 3, 5, 2]
print(leaders(arr))

# 2. [Expected Approach] Using Suffix Maximum – O(n) Time and O(1) Space:
# The idea is to scan all the elements from right to left in an array and keep track of the maximum till now. When the maximum changes its value, add it to the result. Finally reverse the result 

def leaders2(arr):
    result = []
    n = len(arr)

    maxRight = arr[-1]
    result.append(maxRight)

    for i in range(n-2, -1, -1):
        if arr[i] >= maxRight:
            maxRight = arr[i]
            result.append(maxRight)

    result.reverse()

    return result

arr = [16, 17, 4, 3, 5, 2]
print(leaders2(arr)) # [17, 5, 2]