# Factorial time O(n!)

# The function generates all permutations of the array. The number of permutations of n items is n! (factorial), 
# which means the time complexity is O(n!).

def factorial_time_example(n):
    # This function has factorial time complexity, O(n!)
    if n == 0 or n == 1:
        return 1
    result = []
    def generate_permutations(arr, index):
        if index == len(arr):
            result.append(arr[:])
            return
        for i in range(index, len(arr)):
            arr[index], arr[i] = arr[i], arr[index]
            generate_permutations(arr, index + 1)
            arr[index], arr[i] = arr[i], arr[index]  # Backtrack

    generate_permutations([1, 2, 3], 0)
    return result

# Test the factorial_time_example
n = 3
result = factorial_time_example(n)
print(f"Factorial Time Example: {result}")
# Factorial Time Example: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]