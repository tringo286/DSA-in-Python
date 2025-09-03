# Unique Number I

# Given an array of integers, every element in the array appears twice except for one element which appears only once. The task is to identify and return the element that occurs only once.

# Examples: 

# Input:  arr[] = [2, 3, 5, 4, 5, 3, 4]
# Output: 2 
# Explanation: Since 2 occurs once, while other numbers occur twice, 2 is the answer.

# Input: arr[] = [2, 2, 5, 5, 20, 30, 30]
# Output: 20
# Explanation: Since 20 occurs once, while other numbers occur twice, 20 is the answer.

# 1. [Naive Approach] Nested Loop Frequency Counting - O(n^2) Time and O(1) Space

# This approach iterates through the array and counts the frequency of each element using a nested loop. For each element, the inner loop counts how many times it appears in the array. If an element appears exactly once, it is returned as the result. This method ensures that the correct element is identified but is inefficient due to the nested loop.

def findUnique(arr):
    n = len(arr)

    # Iterate over every element
    for i in range(n):

        # Initialize count to 0
        count = 0

        for j in range(n):

            # Count the frequency of the element
            if arr[i] == arr[j]:
                count += 1

        # If the frequency of the element is one
        if count == 1:
            return arr[i]

    # If no element exists at most once
    return -1

if __name__ == "__main__":
    arr = [2, 3, 5, 4, 5, 3, 4]
    print(findUnique(arr))