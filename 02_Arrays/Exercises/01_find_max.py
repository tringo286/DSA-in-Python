# Description:
# Given an array of integers, write a function 
# that returns the maximum element in the array.

# Example:
# arr = [1, 5, 3, 9, 2]
# max_element = find_max(arr)
# print(max_element) # Output: 9

# Approach #1: Iterating through the List Manually
# Time Complexity: O(n)
# Space Complexity: O(1) (because we're not using any extra space apart from the input array)
def find_max_1(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max

arr = [1, 5, 3, 9, 2]
print(find_max_1(arr)) #9

# Approach #2: Using python built-in function
# Time Complexity: O(n)
# Space Complexity: O(1) 
def find_max_2(arr):
    return max(arr)

arr = [1, 5, 3, 9, 2]
print(find_max_2(arr)) #9

# Approach #3: Sorting the array in descending order and return the first element.
# Time Complexity: O(n log n) (because of the sorting step)
# Space Complexity: O(1) (if the sorting is done in-place)

def find_max_3(arr):
    arr.sort(reverse=True)
    return arr[0]

arr = [1, 5, 3, 9, 2]
print(find_max_3(arr)) #9