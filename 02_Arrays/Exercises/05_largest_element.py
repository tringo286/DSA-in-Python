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