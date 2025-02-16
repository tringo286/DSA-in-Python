# Insertion in the middle - O(n)
def insert_middle(arr, value, index):
    arr.insert(index, value)  # Insert at the specified index (middle)

# Example usage
arr = [1, 2, 3, 4, 5]
insert_middle(arr, 10, 2)
print("Array after inserting 10 in the middle:", arr) # [1, 2, 10, 3, 4, 5]

# Time Complexity: O(n) - Inserting an element at any position other than the end requires shifting elements.
