# 2 Sum - Find a pair with given sum

# Given an array arr[] and an integer target. You have to return the pair of elements which sum upto target. You cannot use the same element twice.
# Note: Inputs are given such that only one valid answer exists.

# Examples:

# Input: arr[] = [2, 9, 10, 4, 15], target = 12
# Output: [2, 10]
# Explanation: Pair with sum equal to 12 is (2, 10).
# Input: arr[] = [3, 2, 4], target = 8
# Output: []
# Explanation: No pair exists with sum equal to 8.
# Input: arr[] = [1, 4, 5, 6, 1], target = 2
# Output: [1, 1]
# Explanation: Pair with sum equal to 2 is (1, 1).
# Constraints:
# 1 <= arr.size() <= 105
# 0 <= arr[i] <= 104
# 1 <= target <= 104

# 1. Approach 1: Brute Force

# The brute force approach is simple. Loop through each element x and find if there is another value that equals to target−x.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [nums[i], nums[j]]
        # Return an empty list if no solution is found
        return []

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    solution = Solution()
    result = solution.twoSum(nums, target)

    print("Output:", result) # Output: [2, 7]
