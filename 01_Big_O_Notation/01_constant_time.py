# Constant time (O(1))

# The operation arr[0] accesses the first element of the array directly, regardless of the array's size. 
# It takes a constant amount of time, so the time complexity is O(1).

def constant_time_example(arr):
    # This function runs in constant time, O(1)
    return arr[0]  # Accessing the first element in a list

# Test the constant_time_example
arr = [1, 2, 3, 4, 5]
result = constant_time_example(arr)
print(f"Constant Time Example: {result}") # Constant Time Example: 1
