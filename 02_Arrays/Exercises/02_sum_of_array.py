# Description:
# Given an array of integers, write a function 
# that returns sum of all the elements in the array

# Example: 
# arr = [1, 2, 3, 4, 5]
# sum_elements = find_sum(arr)
# print(sum_elements) # Output: 15

# Aproach #1: Using python built-in sum() function
# Time Complexity: O(n)
# Space Complexity: O(1)
def find_sum_1(arr):
    return sum(arr)

arr = [1, 2, 3, 4, 5]
print(find_sum_1(arr)) # 15

# Aproach #2: Using a loop manually sum the elements
# Time Complexity: O(n)
# Space Complexity: O(1)
def find_sum_2(arr):
    sum  = 0
    for i in arr:
        sum += i
    return sum

arr = [1, 2, 3, 4, 5]
print(find_sum_2(arr)) # 15

# Aproach #3: Using Recursion
# Time Complexity: O(n)
# Space Complexity: O(n) (due to the recursive call stack)
def find_sum_3(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + find_sum_3(arr[1:])

arr = [1, 2, 3, 4, 5]
print(find_sum_3(arr)) # 15