# Logarithmic time O(log n)

# With each step, the number of elements remaining in the search space is halved. 
# The number of iterations is proportional to the number of times the array can be halved, 
# which is about log₂(n). Therefore, the time complexity is O(log n).

def binary_search(arr, target):
    # This function performs binary search, which has a time complexity of O(log n)
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Target not found

# Test the binary_search function
arr = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search(arr, target)
print(f"Logarithmic Time Example: Found {target} at index {result}") # Logarithmic Time Example: Found 7 at index 3
