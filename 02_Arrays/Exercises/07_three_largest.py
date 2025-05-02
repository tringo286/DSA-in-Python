# Largest three distinct elements in an array
# Given an array arr[], the task is to find the top three largest distinct integers present in the array.

# Note: If there are less than three distinct elements in the array, then return the available distinct numbers in descending order.

# Exmaples:
# Input: arr[] = [10, 4, 3, 50, 23, 90]
# Output: [90, 50, 23]


# Input: arr[] = [10, 9, 9]
# Output: [10, 9]
# There are only two distinct elements


# Input: arr[] = [10, 10, 10]
# Output: [10]
# There is only one distinct element


# Input: arr[] = []
# Output: []

# Expected Approach - One Traversal

def getThreeLargest(arr):
    arr_size = (len(arr))

    if arr_size < 3:
        print('Invalid Input')
        return
    
    third = second = first = float('-inf')

    for i in range(arr_size):
        if arr[i] > first:
            third = second
            second = first
            first = arr[i]

        elif arr[i] > second and arr[i] != first:
            third = second
            second = arr[i]

        elif arr[i] > third and arr[i] != second and arr[i] != first:
            third = arr[i]

    print("Three largest elements are: ", first, second, third)

arr = [12, 13, 1, 10, 34, 11, 34]
getThreeLargest(arr) # 34 13 12 