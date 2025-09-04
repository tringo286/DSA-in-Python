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

#2. [Better Approach] Using Hash Map - O(n) Time and O(n) Space 

# This approach uses a hash map (or dictionary) to track the frequency of each element in the array. First, we iterate through the array to record how many times each element appears. Then, we scan the hash map to find the element that appears exactly once. If such an element is found, it is returned; otherwise, the function returns -1. This method efficiently solves the problem in linear time with a linear space complexity.

# Step by step approach:

# Traverse all elements and insert them into a hash table. Element is used as key and the frequency is used as the value in the hash table. 
# Iterate through the map and return the value with count equal to 1.

def findUnique(arr):
    # Dictionary to store the count of each element
    cnt = {}

    # Store frequency of each element
    for num in arr:
        cnt[num] = cnt.get(num, 0) + 1

    # Return the value with count = 1
    for key, value in cnt.items():
        if value == 1:
            return key

    # If no element exists that appears only once
    return -1

arr = [2, 3, 5, 4, 5, 3, 4]
print(findUnique(arr)) # 2
