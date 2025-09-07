# Find the Missing Number

# Given an array arr[] of size n-1 with distinct integers in the range of [1, n]. This array represents a permutation of the integers from 1 to n with one element missing. Find the missing element in the array.

# Examples: 

# Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
# Output: 6
# Explanation: All the numbers from 1 to 8 are present except 6.

# Input: arr[] = [1, 2, 3, 5]
# Output: 4
# Explanation: Here the size of the array is 4, so the range will be [1, 5]. The missing number between 1 to 5 is 4

# 1. [Naive Approach] Linear Search for Missing Number - O(n^2) Time and O(1) Space

# This approach iterates through each number from 1 to n (where n is the size of the array + 1) and checks if the number is present in the array. For each number, it uses a nested loop to search the array. If a number is not found, it is returned as the missing number. 

def missingNum(arr):
    n = len(arr) + 1

    # Iterate from 1 to n and check
    # if the current number is present
    for i in range(1, n + 1):
        found = False
        for j in range(n - 1):
            if arr[j] == i:
                found = True
                break

        # If the current number is not present
        if not found:
            return i
    return -1

if __name__ == '__main__':
    arr = [8, 2, 4, 5, 3, 7, 1]
    print(missingNum(arr)) # 6

# 2. [Better Approach] Using Hashing - O(n) Time and O(n) Space

# This approach uses a hash array (or frequency array) to track the presence of each number from 1 to n in the input array. It first initializes a hash array to store the frequency of each element. Then, it iterates through the hash array to find the number that is missing (i.e., the one with a frequency of 0).

def missingNum(arr):
    n = len(arr) + 1

    # Create hash array of size n+1
    hash = [0] * (n + 1)

    # Store frequencies of elements
    for i in range(n - 1):
        hash[arr[i]] += 1

    # Find the missing number
    for i in range(1, n + 1):
        if hash[i] == 0:
            return i
    return -1

if __name__ == '__main__':
    arr = [8, 2, 4, 5, 3, 7, 1]
    res = missingNum(arr)
    print(res) # 6 