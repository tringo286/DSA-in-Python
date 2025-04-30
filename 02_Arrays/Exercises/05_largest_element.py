# Description
# Given an array arr. The task is to find the largest element in the given array. 

# Input: arr[] = [20, 10, 20, 4, 100]
# Output: 100

# 1. Iterative Approach – O(n) Time and O(1) Space
def find_largest(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max

if __name__ == '__main__':
    arr = [10, 324, 45, 90, 9808]
    print(find_largest(arr)) # 9808

# 2. Recursive Approach – O(n) Time and O(n) Space

def findMax(arr, i): # i is the start index
    # Base case
    if i == len(arr) - 1:
        return arr[i]

    # Recursive case
    return max(findMax(arr, i + 1), arr[i])

arr = [10, 324, 45, 90, 9808, 1]
print(findMax(arr, 0)) # 9808

# 3. Using Library Methods – O(n) Time and O(1) Space
def largest(arr):
    return max(arr)

if __name__ == '__main__':
  arr = [10, 324, 45, 90, 9808]
  print(largest(arr)) # 9808
