# Missing and Repeating in an Array

# Given an unsorted array arr[] of size n, containing elements from the range 1 to n, it is known that one number in this range is missing, and another number occurs twice in the array, find both the duplicate number and the missing number.

# Examples: 

# Input: arr[] = [3, 1, 3]
# Output: [3, 2]
# Explanation: 3 is occurs twice and 2 is missing.

# Input: arr[] = [4, 3, 6, 2, 1, 1]
# Output: [1, 5] 
# Explanation: 1 is occurs twice and 5 is missing.

# 1. [Approach 1] Using Visited Array - O(n) Time and O(n) Space

# The idea is to use a frequency array to keep track of how many times each number appears in the original array. Since we know the numbers should range from 1 to n with each appearing exactly once, any number appearing twice is our repeating number, and any number with zero frequency is our missing number.

def findTwoElement(arr):
    n = len(arr)

    # frequency array to count occurrences
    freq = [0] * (n + 1)
    repeating = -1
    missing = -1

    # count frequency of each element
    for num in arr:
        freq[num] += 1

    # identify missing and repeating numbers
    for i in range(1, n + 1):
        if freq[i] == 0:
            missing = i
        elif freq[i] == 2:
            repeating = i

    return [repeating, missing]

if __name__ == "__main__":
    arr = [3, 1, 3]
    ans = findTwoElement(arr)
    print(ans[0], ans[1]) # 3 2 

# 2. [Approach 2] Using Array Marking - O(n) Time and O(1) Space

# The main idea is to use the input array itself for tracking: it negates the value at the index corresponding to each element to mark it as visited. If it encounters a value that has already been negated, it identifies that number as the repeating one. In a second pass, it finds the index that remains positive, which corresponds to the missing number. 

def findTwoElement(arr):
    n = len(arr)
    repeating = -1

    # mark visited indices by negating the value 
    # at that index
    for i in range(n):
        val = abs(arr[i])

        # if value at index val - 1 is already negative,
        # val is repeating
        if arr[val - 1] > 0:
            arr[val - 1] = -arr[val - 1] 
        else:
            # Already visited → repeating element
            repeating = val  

    missing = -1

    # the index with a positive value corresponds 
    # to the missing number
    for i in range(n):
        if arr[i] > 0:
            missing = i + 1
            break

    return [repeating, missing]

if __name__ == "__main__":
    arr = [3, 1, 3]
    ans = findTwoElement(arr)
    print(ans[0], ans[1]) # 3 2