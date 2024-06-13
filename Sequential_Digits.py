# 1291. Sequential Digits
# Solved
# Medium
# Topics
# Companies
# Hint
# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

# Example 1:

# Input: low = 100, high = 300
# Output: [123,234]
# Example 2:

# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]
 

# Constraints:

# 10 <= low <= high <= 10^9








class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        result = []
        
        # Generate all sequential digit numbers
        for start in range(1, 10):
            num = start
            next_digit = start
            while num <= high and next_digit < 10:
                if num >= low:
                    result.append(num)
                next_digit += 1
                num = num * 10 + next_digit
        
        # Return sorted result
        return sorted(result)