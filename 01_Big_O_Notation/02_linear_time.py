# Linear time (O(n))

# The function iterates through each element in the array once. 
# The time taken grows linearly with the size of the input (n), so the time complexity is O(n).

def linear_time_example(arr):
    # This function runs in linear time, O(n)
    total = 0
    for num in arr:
        total += num  # Summing up all elements
    return total

# Test the linear_time_example
arr = [1, 2, 3, 4, 5]
result = linear_time_example(arr)
print(f"Linear Time Example: {result}") # Linear Time Example: 15
