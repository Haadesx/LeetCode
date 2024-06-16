# 907. Sum of Subarray Minimums
# Solved
# Medium
# Topics
# Companies
# Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

 

# Example 1:

# Input: arr = [3,1,2,4]
# Output: 17
# Explanation: 
# Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
# Sum is 17.
# Example 2:

# Input: arr = [11,81,94,43,3]
# Output: 444
 

# Constraints:

# 1 <= arr.length <= 3 * 104
# 1 <= arr[i] <= 3 * 104





class Solution:
    def sumSubarrayMins(self, arr):
        MOD = 10**9 + 7
        n = len(arr)
        
        # Initialize left and right arrays
        left = [0] * n
        right = [0] * n
        
        # Find previous less element for each element
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            left[i] = i + 1 if not stack else i - stack[-1]
            stack.append(i)
        
        # Find next less element for each element
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            right[i] = n - i if not stack else stack[-1] - i
            stack.append(i)
        
        # Calculate the result
        result = 0
        for i in range(n):
            result = (result + arr[i] * left[i] * right[i]) % MOD
        
        return result

# Example usage:
solution = Solution()
print(solution.sumSubarrayMins([3, 1, 2, 4]))  # Output: 17
print(solution.sumSubarrayMins([11, 81, 94, 43, 3]))  # Output: 444
