# 1248. Count Number of Nice Subarrays
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

# Return the number of nice sub-arrays.

 

# Example 1:

# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
# Example 2:

# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There are no odd numbers in the array.
# Example 3:

# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16
 

# Constraints:

# 1 <= nums.length <= 50000
# 1 <= nums[i] <= 10^5
# 1 <= k <= nums.lengt







class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Convert the original array to an array of 1s (odd) and 0s (even)
        transformed = [1 if num % 2 == 1 else 0 for num in nums]
        
        # Initialize the hashmap to store the frequency of prefix sums
        prefix_sum_count = {0: 1}
        curr_sum = 0
        result = 0
        
        # Iterate through the transformed array
        for num in transformed:
            curr_sum += num
            
            # Check if (curr_sum - k) is in the hashmap
            if (curr_sum - k) in prefix_sum_count:
                result += prefix_sum_count[curr_sum - k]
            
            # Update the hashmap with the current prefix sum
            if curr_sum in prefix_sum_count:
                prefix_sum_count[curr_sum] += 1
            else:
                prefix_sum_count[curr_sum] = 1
        
        return result
