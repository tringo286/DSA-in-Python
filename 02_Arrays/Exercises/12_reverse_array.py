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

    return arr

arr = [1, 4, 3, 2, 6, 5]
print('Temporay Array Approach')
print(reverseArray(arr)) # [5, 6, 2, 3, 4, 1]
print()

# 2. [Expected Approach – 1] Using Two Pointers – O(n) Time and O(1) Space

# The idea is to maintain two pointers: left and right, such that left points at the beginning of the array and right points to the end of the array. 


# While left pointer is less than the right pointer, swap the elements at these two positions. After each swap, increment the left pointer and decrement the right pointer to move towards the center of array. This will swap all the elements in the first half with their corresponding element in the second half.

def reverseArray(arr):
    
    # Initialize left to the beginning and right to the end
    left = 0
    right = len(arr) - 1
  
    # Iterate till left is less than right
    while left < right:
        
        # Swap the elements at left and right position
        arr[left], arr[right] = arr[right], arr[left]
      
        # Increment the left pointer
        left += 1
      
        # Decrement the right pointer
        right -= 1

    return arr

arr = [1, 4, 3, 2, 6, 5]
print('Two Pointer Approach')
print(reverseArray(arr)) # [5, 6, 2, 3, 4, 1]
print()

# print(reverseArray(arr))    

# 3. [Expected Approach - 2] By Swapping Elements - O(n) Time and O(1) Space

# The idea is to iterate over the first half of the array and swap each element with its corresponding element from the end. So, while iterating over the first half, any element at index i is swapped with the element at index (n - i - 1).

def reverseArray(arr):
    n = len(arr)
    
    # Iterate over the first half and for every index i,
    # swap arr[i] with arr[n - i - 1]
    for i in range(n // 2):
        temp = arr[i]
        arr[i] = arr[n - i - 1]
        arr[n - i - 1] = temp

        # arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]

    return arr

arr = [1, 4, 3, 2, 6, 5]
print('Swapping Elements Approach')
print(reverseArray(arr)) # [5, 6, 2, 3, 4, 1]
print()

# 4. [Alternate Approach] Using Recursion - O(n) Time and O(n) Space

# The idea is to use recursion and define a recursive function that takes a range of array elements as input and reverses it. Inside the recursive function, 

#  Swap the first and last element. 
#  Recursively call the function with the remaining subarray. 

# recursive function to reverse an array from l to r
def reverseArrayRec(arr, l, r):
    if l >= r:
        return
  
    # Swap the elements at the ends
    arr[l], arr[r] = arr[r], arr[l]
  
    # Recur for the remaining array
    reverseArrayRec(arr, l + 1, r - 1)
    
# function to reverse an array
def reverseArray(arr):
    n = len(arr)
    reverseArrayRec(arr, 0, n - 1)
    return arr

arr = [1, 4, 3, 2, 6, 5]

print('Recursive Approach')
print(reverseArray(arr)) # [5, 6, 2, 3, 4, 1]
print()

# 5. Using Inbuilt Methods - O(n) Time and O(1) Space

arr = [1, 4, 3, 2, 6, 5]

print('Built-in Method Approach')
arr.reverse()

for i in range(len(arr)):
    print(arr[i], end= ' ') # 5, 6, 2, 3, 4, 1