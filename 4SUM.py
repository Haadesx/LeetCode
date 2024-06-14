# 18. 4Sum
# Solved
# Medium
# Topics
# Companies
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
 

# Constraints:

# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109






class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        results = set()
        n = len(nums)
    
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                seen = set()
                for k in range(j + 1, n):
                    complement = target - nums[i] - nums[j] - nums[k]
                    if complement in seen:
                        results.add((nums[i], nums[j], complement, nums[k]))
                    seen.add(nums[k])
    
        return [list(quadruplet) for quadruplet in results]
