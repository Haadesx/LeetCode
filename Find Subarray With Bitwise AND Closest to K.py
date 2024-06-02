# 3171. Find Subarray With Bitwise AND Closest to K
# Attempted
# Hard
# Companies
# Hint
# You are given an array nums and an integer k. You need to find a 
# subarray
#  of nums such that the absolute difference between k and the bitwise AND of the subarray elements is as small as possible. In other words, select a subarray nums[l..r] such that |k - (nums[l] AND nums[l + 1] ... AND nums[r])| is minimum.

# Return the minimum possible value of the absolute difference.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,2,4,5], k = 3

# Output: 1

# Explanation:

# The subarray nums[2..3] has AND value 4, which gives the minimum absolute difference |3 - 4| = 1.

# Example 2:

# Input: nums = [1,2,1,2], k = 2

# Output: 0

# Explanation:

# The subarray nums[1..1] has AND value 2, which gives the minimum absolute difference |2 - 2| = 0.

# Example 3:

# Input: nums = [1], k = 10

# Output: 9

# Explanation:

# There is a single subarray with AND value 1, which gives the minimum absolute difference |10 - 1| = 9.

 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= 10


class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Initialize the answer with the maximum possible value
        ans = float('inf')
        
        # Sort the array to ensure the bitwise AND of any subarray only decreases
        nums.sort()
        
        # Iterate over the array and calculate the bitwise AND for each subarray
        for i in range(len(nums)):
            bitwise_and = nums[i]
            # If the current number is already less than or equal to k, no need to proceed further
            if bitwise_and <= k:
                ans = min(ans, k - bitwise_and)
                break
            for j in range(i+1, len(nums)):
                bitwise_and &= nums[j]
                # Once the bitwise AND drops below k, break the inner loop
                if bitwise_and <= k:
                    break
                ans = min(ans, abs(k - bitwise_and))
        
        # If no subarray found, the answer will be the absolute difference between k and the AND of all numbers
        return 0 if ans == float('inf') else ans
