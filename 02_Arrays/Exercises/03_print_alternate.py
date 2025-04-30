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

arr = [10, 20, 30, 40, 50] 
print(get_alternate(arr)) # [10, 30, 50]

# Aproach #2: Recursive approach
# Time Complexity: O(n), where n is the number of elements in arr[].
# Auxiliary Space: O(n), for recursive call stack.

def get_alternates(arr, index=0):
    if index >= len(arr):
        return []
    else:
        return [arr[index]] + get_alternates(arr, index + 2)

arr = [10, 20, 30, 40, 50] 
print(get_alternates(arr)) # [10, 30, 50]
    
# index = 0: returns [10] + get_alternates(... index=2)

# index = 2: returns [30] + get_alternates(... index=4)

# index = 4: returns [50] + get_alternates(... index=6)

# index = 6: base case hit → returns []

# Final result: [10] + [30] + [50] + [] → [10, 30, 50]