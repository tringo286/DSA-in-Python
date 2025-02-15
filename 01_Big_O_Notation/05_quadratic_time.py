# Quadratic time O(n^2)

# There are two nested loops: the outer loop runs n times, and for each iteration of the outer loop, 
# the inner loop runs up to n times. This results in O(n * n) = O(n^2) time complexity.

def quadratic_time_example(arr):
    # This function has quadratic time complexity, O(n^2)
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            pairs.append((arr[i], arr[j]))  # All pairs of elements
    return pairs

# Test the quadratic_time_example
arr = [1, 2, 3, 4]
result = quadratic_time_example(arr)
print(f"Quadratic Time Example: {result}")
# Quadratic Time Example: [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
