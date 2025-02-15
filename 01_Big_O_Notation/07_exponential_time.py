# Exponential time O(2^n)

# This recursive function makes two calls for each n. Each call branches into two more calls, 
# doubling the work at each level. This results in exponential growth, with time complexity O(2^n).

def exponential_time_example(n):
    # This function has exponential time complexity, O(2^n)
    if n <= 1:
        return 1
    return exponential_time_example(n-1) + exponential_time_example(n-1)

# Test the exponential_time_example
n = 5
result = exponential_time_example(n)
print(f"Exponential Time Example: {result}")
