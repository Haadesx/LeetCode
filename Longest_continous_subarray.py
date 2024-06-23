
# Code
# Testcase
# Testcase
# Test Result
# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

 

# Example 1:

# Input: nums = [8,2,4,7], limit = 4
# Output: 2 
# Explanation: All subarrays are: 
# [8] with maximum absolute diff |8-8| = 0 <= 4.
# [8,2] with maximum absolute diff |8-2| = 6 > 4. 
# [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
# [2] with maximum absolute diff |2-2| = 0 <= 4.
# [2,4] with maximum absolute diff |2-4| = 2 <= 4.
# [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
# [4] with maximum absolute diff |4-4| = 0 <= 4.
# [4,7] with maximum absolute diff |4-7| = 3 <= 4.
# [7] with maximum absolute diff |7-7| = 0 <= 4. 
# Therefore, the size of the longest subarray is 2.
# Example 2:

# Input: nums = [10,1,2,4,7,2], limit = 5
# Output: 4 
# Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
# Example 3:

# Input: nums = [4,2,2,2,4,4,2,2], limit = 0
# Output: 3
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 0 <= limit <= 109




from collections import deque

class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        minDeque = deque()
        maxDeque = deque()
        left = 0
        maxLength = 0
        
        for right in range(len(nums)):
            # Maintain the minDeque for minimum values
            while minDeque and nums[minDeque[-1]] >= nums[right]:
                minDeque.pop()
            minDeque.append(right)
            
            # Maintain the maxDeque for maximum values
            while maxDeque and nums[maxDeque[-1]] <= nums[right]:
                maxDeque.pop()
            maxDeque.append(right)
            
            # Ensure the current window satisfies the condition
            while nums[maxDeque[0]] - nums[minDeque[0]] > limit:
                left += 1
                if minDeque[0] < left:
                    minDeque.popleft()
                if maxDeque[0] < left:
                    maxDeque.popleft()
            
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength
