# Rearrange array such that even positioned are greater than odd

# Given an array arr[], sort the array according to the following relations:  

# arr[i] >= arr[i - 1], if i is even, ∀ 1 <= i < n
# arr[i] <= arr[i - 1], if i is odd, ∀ 1 <= i < n
# Find the resultant array.[consider 1-based indexing]

# Examples:  

# Input: arr[] = [1, 2, 2, 1]
# Output: [1 2 1 2]
#  Explanation:
# For i = 2, arr[i] >= arr[i-1]. So, 2 >= 1.
# For i = 3, arr[i] <= arr[i-1]. So, 1 <= 2.
# For i = 4, arr[i] >= arr[i-1]. So, 2 >= 1.

# Input: arr[] = [1, 3, 2]
# Output: [1 3 2]
# Explanation: 

# 1.  Assign Maximum Elements to Even Positions

# Observe that array consists of [n/2] even positioned elements. If we assign the largest [n/2] elements to the even positions and the rest of the elements to the odd positions, our problem is solved. Because element at the odd position will always be less than the element at the even position as it is the maximum element and vice versa. Sort the array and assign the first [n/2] elements at even positions.

# Python program to Rearrange array such that even positioned are greater than odd

def rearrangeArray(arr):
    arr.sort()

    n = len(arr)
    result = [0] * n
    ptr1, ptr2 = 0, n - 1

    for i in range(n):
      
        # Assign even indexes (1-based) with maximum elements
        if (i + 1) % 2 == 0:
            result[i] = arr[ptr2]
            ptr2 -= 1
            
        # Assign odd indexes (1-based) with remaining elements
        else:
            result[i] = arr[ptr1]
            ptr1 += 1

    return result

 
arr = [1, 2, 2, 1]
res = rearrangeArray(arr)
print(res) # [1, 2, 1, 2]

# 2. Rearranging array by swapping elements

# One other approach is to traverse the array from the first element till n - 1 and swap the element with the next one if the condition is not satisfied. This is implemented as follows: 

# Python program to Rearrange array such that even positioned are greater than odd


def rearrangeArray(arr):
    n = len(arr)

    # Traverse the array and make adjustments to satisfy the condition
    for i in range(1, n):

        # Check if the index is even (1-based), i.e., i+1 is even
        if (i + 1) % 2 == 0:
            # Ensure that the current element is greater than
            # or equal to the previous element
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        else:
            # Ensure that the current element is less than or
            # equal to the previous element
            if arr[i] > arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]

    return arr


if __name__ == "__main__":

    inputArray = [1, 2, 2, 1]

    resultArray = rearrangeArray(inputArray)

    print(" ".join(map(str, resultArray))) # 1 2 1 2