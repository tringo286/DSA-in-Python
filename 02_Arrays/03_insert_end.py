# Insertion at the end - O(1)
def insert_end(arr, value):
    arr.append(value)  # Appends to the end of the list

# Example usage
arr = [1, 2, 3, 4, 5]
insert_end(arr, 6)
print("Array after inserting 6 at the end:", arr) # [1, 2, 3, 4, 5, 6]

# Time Complexity: O(1) - Appending to the end of a list is a constant-time operation.
