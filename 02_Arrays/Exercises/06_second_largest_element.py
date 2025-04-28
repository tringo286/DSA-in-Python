# Description
# Given an array of positive integers arr[] of size n, the task is to find second largest distinct element in the array.

# Note: If the second largest element does not exist, return -1.

# Examples:
# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.


# Input: arr[] = [10, 5, 10]
# Output: 5
# Explanation: The largest element of the array is 10 and the second largest element is 5.


# Input: arr[] = [10, 10, 10]
# Output: -1
# Explanation: The largest element of the array is 10 there is no second largest element.

# 1. [Naive Approach] Using Sorting

def getSecondLargest(arr):
    n = len(arr)
    
    # Sort the array in non-decreasing order
    arr.sort()
  
    # start from second last element as last element is the largest
    for i in range(n - 2, -1, -1):
      
        # return the first element which is not equal to the 
        # largest element
        if arr[i] != arr[n - 1]:
            return arr[i]
    
    # If no second largest element was found, return -1
    return -1

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(getSecondLargest(arr)) # 34 

# 2. [Better Approach] Two Pass Search
# Python program to find the second largest element in the array
# using two traversals

# Function to find the second largest element in the array
def getSecondLargest(arr):
    n = len(arr)

    largest = -1
    secondLargest = -1

    # Finding the largest element
    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]

    # Finding the second largest element
    for i in range(n):
        
        # Update second largest if the current element is greater
        # than second largest and not equal to the largest
        if arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]
    
    return secondLargest

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(getSecondLargest(arr)) # 34 