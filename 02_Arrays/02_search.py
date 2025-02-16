# Search operation - O(n)
def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Return -1 if target is not found

# Example usage
arr = [1, 2, 3, 4, 5]
print("Searching for 4:", search(arr, 4))  # Should print index 3

# Time Complexity: O(n) - In the worst case, we have to search through all n elements.
