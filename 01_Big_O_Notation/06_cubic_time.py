# Cubic time O(n^3)

# There are three nested loops, each iterating through the array. 
# Each loop runs up to n times, resulting in O(n * n * n) = O(n^3) time complexity.

def cubic_time_example(arr):
    # This function has cubic time complexity, O(n^3)
    triplets = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                triplets.append((arr[i], arr[j], arr[k]))  # All triplets of elements
    return triplets

# Test the cubic_time_example
arr = [1, 2, 3]
result = cubic_time_example(arr)
print(f"Cubic Time Example: {result}") # Cubic Time Example: [(1, 2, 3)]
