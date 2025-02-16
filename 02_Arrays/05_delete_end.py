# Deletion from the end - O(1)
def delete_end(arr):
    arr.pop()  # Removes the last element from the list

# Example usage
arr = [1, 2, 3, 4, 5]
delete_end(arr)
print("Array after deleting from the end:", arr)

# Time Complexity: O(1) - Removing the last element from the list is a constant-time operation.
