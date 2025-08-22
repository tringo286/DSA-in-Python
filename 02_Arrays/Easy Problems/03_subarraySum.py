# Sum of all Subarrays

# Given an integer array arr[], compute the sum of all possible sub-arrays of the array. A sub-array is a contiguous part of the array.

# Examples: 

# Input: arr[] = [1, 4, 5, 3, 2]
# Output: 116
# Explanation: Sum of all possible subarrays of the array [1, 4, 5, 3, 2] is 116.

# Input: arr[] = [1, 2, 3, 4]
# Output: 50
# Explanation: Sum of all possible subarrays of the array [1, 2, 3, 4] is 50.

# 1. Using Nested Loop - O(n2) Time and O(1) Space

# The main idea of this approach is to iterate over all possible subarrays of the given array using two nested loops. The outer loop selects the starting index of the subarray, while the inner loop extends the subarray to include all possible ending points. During this process, a running sum (temp) is maintained for each subarray and added to the total result. 

def subarraySum(arr):
    n = len(arr)
    result = 0
    
    # pick starting point
    for i in range(n):
        temp = 0
        
        # pick ending point
        for j in range(i, n):
          
            # sum subarray between current starting 
            # and ending points
            temp += arr[j]
            result += temp
    return result

if __name__ == "__main__":
    arr = [1, 4, 5, 3, 2]
    print(subarraySum(arr)) # 116

# 2. [Expected Approach] Element Contribution Method - O(n) Time and O(1) Space

# Let's take an example: arr[] = [1, 4, 5, 3, 2]
# All subarrays :  [1], [1, 4], [1, 4, 5], [1, 4, 5, 3], [1, 4, 5, 3, 2], [4], [4, 5], [4, 5, 3], [4, 5, 3, 2], [5], [5, 3], [5, 3, 2], [3], [3, 2], [2]

# subbaray-sum
 
# Third element arr[2] appears 3 time when subarray start with arr[0]: [1, 4, 5], [1, 4, 5, 3], [1, 4, 5, 3, 2]
# Third element arr[2] appears 3 time when subarray start with arr[1]: [4, 5], [4, 5, 3], [4, 5, 3, 2]
# Third element arr[2] appears 3 time when subarray start with arr[2]: [5], [5, 3], [5, 3, 2]

# So, We can clearly see that, For any element arr[i] in an array of size n, it appears in exactly (i + 1) * (n - i) subarrays.

# For arr[] = [1, 2, 3], sum of subarrays is: arr[0] * ( 0 + 1 ) * ( 3 - 0 )  +  arr[1] * ( 1 + 1 ) * ( 3 - 1 )  +  arr[2] * ( 2 + 1 ) * ( 3 - 2 ) = 1*3*3 + 2*2*2 + 3*3*1  = 20

def subarraySum(arr):
    
    n = len(arr)
    result = 0

    # Computing sum of subarrays using the formula
    for i in range(n):
        result += arr[i] * (i + 1) * (n - i)

    # Return the sum of all subarrays
    return result

if __name__ == "__main__":
    arr = [1, 4, 5, 3, 2]
    print(subarraySum(arr)) # 116
    

