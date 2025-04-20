# Description
# Given an array arr. The task is to find the largest element in the given array. 

# Input: arr[] = [20, 10, 20, 4, 100]
# Output: 100

# Iterative Approach – O(n) Time and O(1) Space
def find_largest(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max

if __name__ == '__main__':
    arr = [10, 324, 45, 90, 9808]
    print(find_largest(arr)) # 9808

# Recursive Approach – O(n) Time and O(n) Space

def findMax(arr, i):
  
    # Last index returns the element
    if i == len(arr) - 1:
        return arr[i]

    # Find the maximum from the rest of the list
    recMax = findMax(arr, i + 1)

    # Compare with i-th element and return
    return max(recMax, arr[i])

def largest(arr):
    return findMax(arr, 0)

if __name__ == '__main__':
  arr = [10, 324, 45, 90, 9808, 1]
  print(largest(arr)) # 9808

def largest(arr):
    return findMax(arr, 0)

# Using Library Methods – O(n) Time and O(1) Space
def largest(arr):
    return max(arr)

if __name__ == '__main__':
  arr = [10, 324, 45, 90, 9808]
  print(largest(arr)) # 9808
