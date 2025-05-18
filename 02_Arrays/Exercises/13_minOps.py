# Minimum increment by k operations to make all equal

# You are given an array of n-elements, you have to find the number of operations needed to make all elements of array equal. Where a single operation can increment an element by k. If it is not possible to make all elements equal print -1.

# Example : 

# Input : arr[] = {4, 7, 19, 16},  k = 3
# Output : 10

# Input : arr[] = {4, 4, 4, 4}, k = 3
# Output : 0

# Input : arr[] = {4, 2, 6, 8}, k = 3
# Output : -1

# function for calculating min operations
def minOps(arr, n, k):

    # max elements of array
    max1 = max(arr)
    res = 0

    # iterate for all elements
    for i in range(0, n): 

        # check if element can make equal to
        # max or not if not then return -1
        if ((max1 - arr[i]) % k != 0):
            return -1

        # else update res for
        # required operations
        else:
            res += (max1 - arr[i]) / k
    
    # return result
    return int(res)

# driver program
arr = [21, 33, 9, 45, 63] 
n = len(arr)
k = 6
print(minOps(arr, n, k))  # 24