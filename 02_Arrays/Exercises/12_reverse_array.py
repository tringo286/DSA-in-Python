# Array Reverse 
# Given an array arr[], the task is to reverse the array. Reversing an array means rearranging the elements such that the first element becomes the last, the second element becomes second last and so on.

# Examples:

# Input: arr[] = {1, 4, 3, 2, 6, 5}  
# Output: {5, 6, 2, 3, 4, 1}
# Explanation: The first element 1 moves to last position, the second element 4 moves to second-last and so on.


# Input: arr[] = {4, 5, 1, 2} 
# Output: {2, 1, 5, 4}
# Explanation: The first element 4 moves to last position, the second element 5 moves to second last and so on.

# 1. [Naive Approach] Using a temporary array – O(n) Time and O(n) Space
# Python Program to reverse an array using temporary array

# function to reverse an array
def reverseArray(arr):
    n = len(arr)
    
    # Temporary array to store elements in reversed order
    temp = [0] * n
  
    # Copy elements from original array to temp in reverse order
    for i in range(n):
        temp[i] = arr[n - i - 1]
  
    # Copy elements back to original array
    for i in range(n):
        arr[i] = temp[i]

if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]

    reverseArray(arr)
  
    for i in range(len(arr)):
        print(arr[i], end=" ") # 5 6 2 3 4 1 