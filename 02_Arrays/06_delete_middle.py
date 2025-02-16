# Deletion from the middle - O(n)
def delete_middle(arr, index):
    arr.pop(index)  # Removes the element at the specified index (middle)

# Example usage
arr = [1, 2, 3, 4, 5]
delete_middle(arr, 2)
print("Array after deleting from the middle:", arr)

# Time Complexity: O(n) - Removing an element from the middle requires shifting elements after the deleted index.
