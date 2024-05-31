# 260. Single Number III
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 

# Example 1:

# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.
# Example 2:

# Input: nums = [-1,0]
# Output: [-1,0]
# Example 3:

# Input: nums = [0,1]
# Output: [1,0]
 

# Constraints:

# 2 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# Each integer in nums will appear twice, only two integers will appear once.



class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Step 1: XOR all the numbers
        xor_result = 0
        for num in nums:
            xor_result ^= num
        
        # Step 2: Find a set bit in the xor_result
        set_bit = xor_result & -xor_result
        
        # Step 3: Partition the array into two groups and XOR within each group
        num1, num2 = 0, 0
        for num in nums:
            if num & set_bit:
                num1 ^= num
            else:
                num2 ^= num
        
        return [num1, num2]

# Example usage:
sol = Solution()
nums1 = [1, 2, 1, 3, 2, 5]
nums2 = [-1, 0]
nums3 = [0, 1]

print(sol.singleNumber(nums1))  # Output: [3, 5]
print(sol.singleNumber(nums2))  # Output: [-1, 0]
print(sol.singleNumber(nums3))  # Output: [1, 0]
