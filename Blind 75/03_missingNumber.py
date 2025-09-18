# 268. Missing Number

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:

# Input: nums = [3,0,1]

# Output: 2

# Explanation:

# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:

# Input: nums = [0,1]

# Output: 2

# Explanation:

# n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:

# Input: nums = [9,6,4,2,3,5,7,0,1]

# Output: 8

# Explanation:

# n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums. 

# Constraints:

# n == nums.length
# 1 <= n <= 104
# 0 <= nums[i] <= n
# All the numbers of nums are unique.

# 1. Approach 1(Sum of all elememnts)

# Time complexity:
# O(n)

# Space complexity:
# O(1)

# sum of all elements in the range[0,n].
# sum of nums.
# If we subtrate both we will get the missing number

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        Tsum = (n * (n + 1)) // 2
        actual_sum = sum(nums)
        return Tsum - actual_sum

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Missing number in the middle
    nums1 = [3, 7, 1, 2, 8, 4, 5]
    print(f"Missing number in {nums1}: {solution.missingNumber(nums1)}")  # Expected: 6

    # Test case 2: Missing number is 0
    nums2 = [1]
    print(f"Missing number in {nums2}: {solution.missingNumber(nums2)}")  # Expected: 0

    # Test case 3: Missing number is the largest
    nums3 = [0, 1, 2, 3]
    print(f"Missing number in {nums3}: {solution.missingNumber(nums3)}")  # Expected: 4

    # Test case 4: No missing number (but this is not valid for this problem as per the problem description)
    nums4 = [0, 1, 2, 3, 4]
    print(f"Missing number in {nums4}: {solution.missingNumber(nums4)}")  # Expected: 5 (but ideally, we need n+1 elements)

