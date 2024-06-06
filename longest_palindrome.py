# 409. Longest Palindrome
# Solved
# Easy
# Topics
# Companies
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
# palindrome
#  that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

# Constraints:

# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        
        count = Counter(s)
        length = 0
        odd_found = False
        
        for char_count in count.values():
            if char_count % 2 == 0:
                length += char_count
            else:
                length += char_count - 1
                odd_found = True
                
        # Add one if there is any odd count character
        if odd_found:
            length += 1
            
        return length
