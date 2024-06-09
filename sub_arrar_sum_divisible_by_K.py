# 974. Subarray Sums Divisible by K
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
# Example 2:

# Input: nums = [5], k = 9
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -104 <= nums[i] <= 104
# 2 <= k <= 104


class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Dictionary to store the frequency of remainders
        remainder_dict = {0: 1}
        running_sum = 0
        count = 0
        
        for num in nums:
            running_sum += num
            remainder = running_sum % k
            
            # Adjust remainder to be positive
            if remainder < 0:
                remainder += k
            
            # If the remainder has been seen before, add its frequency to the count
            if remainder in remainder_dict:
                count += remainder_dict[remainder]
            
            # Update the frequency of the current remainder
            if remainder in remainder_dict:
                remainder_dict[remainder] += 1
            else:
                remainder_dict[remainder] = 1
        
        return count

# Example usage
solution = Solution()
print(solution.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))  # Output: 7