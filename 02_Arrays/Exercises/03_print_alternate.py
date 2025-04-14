# Description:
# Given an array arr[], the task is to print every 
# alternate element of the array starting from the first element.

# Example: 
# Input: arr = [10, 20, 30, 40, 50]
# Output: 10 30 50
# Explanation: Print the first element (10), skip the second element (20), print the third element (30), skip the fourth element(40) and print the fifth element(50).

# Aproach #1: Iterative aproach
# Time Complexity: O(n), where n is the number of elements in arr[].
# Auxiliary Space: O(1)

def get_alternate(arr):
    result = []
    
    # Iterate over all the alternate elements
    for i in range(0, len(arr), 2):
        result.append(arr[i])
    return result

if __name__ == '__main__':
    arr = [10, 20, 30, 40, 50] 
    print(get_alternate(arr)) # [10, 30, 50]

# Aproach #2: Recursive approach
# Time Complexity: O(n), where n is the number of elements in arr[].
# Auxiliary Space: O(n), for recursive call stack.

def get_alternates_rec(arr, index, res):
    if index < len(arr):
        res.append(arr[index])
        get_alternates_rec(arr, index + 2, res)

def get_alternates(arr):
    res = []
    get_alternates_rec(arr, 0, res)
    return res

if __name__ == '__main__':
    arr = [10, 20, 30, 40, 50] 
    res = get_alternates(arr)
    # Converts res to a string and joins them into one single string with a space " " between each element
    print(" ".join(map(str, res))) # 10 30 50
    