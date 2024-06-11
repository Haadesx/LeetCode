# 1657. Determine if Two Strings Are Close
# Solved
# Medium
# Topics
# Companies
# Hint
# Two strings are considered close if you can attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

 

# Example 1:

# Input: word1 = "abc", word2 = "bca"
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"
# Example 2:

# Input: word1 = "a", word2 = "aa"
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
# Example 3:

# Input: word1 = "cabbba", word2 = "abbccc"
# Output: true
# Explanation: You can attain word2 from word1 in 3 operations.
# Apply Operation 1: "cabbba" -> "caabbb"
# Apply Operation 2: "caabbb" -> "baaccc"
# Apply Operation 2: "baaccc" -> "abbccc"
 

# Constraints:

# 1 <= word1.length, word2.length <= 105
# word1 and word2 contain only lowercase English letters.









from collections import Counter

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        # If lengths are different, they cannot be close
        if len(word1) != len(word2):
            return False
        
        # Count the frequency of each character in both words
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        
        # Check if both words have the same set of unique characters
        if set(freq1.keys()) != set(freq2.keys()):
            return False
        
        # Check if both words have the same frequency distribution
        if sorted(freq1.values()) != sorted(freq2.values()):
            return False
        
        return True

# Example 1
word1 = "abc"
word2 = "bca"
solution = Solution()
print(solution.closeStrings(word1, word2))  # Output: True

# Example 2
word1 = "a"
word2 = "aa"
print(solution.closeStrings(word1, word2))  # Output: False

# Example 3
word1 = "cabbba"
word2 = "abbccc"
print(solution.closeStrings(word1, word2))  # Output: True
