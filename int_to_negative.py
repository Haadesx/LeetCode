# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -2^31 <= x <= 2^31 - 1



class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=str(x)
        if s[0]=="-":
            b=s.split("-")
            b[1]=b[1][::-1]
            b="-".join(b)
            b=int(b)
        else:
            b=s
            b=int(b[::-1])
            
                
        if b>(2**31)-1 or b<(-2**31):
            return 0
        else:
            return b


