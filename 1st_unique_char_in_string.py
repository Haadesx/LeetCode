# 387. First Unique Character in a String
# Solved
# Easy
# Topics
# Companies
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Step 1: Create a dictionary to count the occurrences of each character
        char_count = {}
        
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Step 2: Find the first character with a count of one
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index
        
        # If no unique character is found, return -1
        return -1