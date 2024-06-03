# 792. Number of Matching Subsequences
# Medium
# Topics
# Companies
# Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
 

# Example 1:

# Input: s = "abcde", words = ["a","bb","acd","ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
# Example 2:

# Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# Output: 2
 

# Constraints:

# 1 <= s.length <= 5 * 104
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 50
# s and words[i] consist of only lowercase English letters.








from collections import defaultdict
import bisect

class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        # Preprocess s
        char_positions = defaultdict(list)
        for idx, char in enumerate(s):
            char_positions[char].append(idx)
        
        def is_subsequence(word):
            current_position = -1
            for char in word:
                if char not in char_positions:
                    return False
                pos_list = char_positions[char]
                idx = bisect.bisect_right(pos_list, current_position)
                if idx == len(pos_list):
                    return False
                current_position = pos_list[idx]
            return True
        
        count = 0
        for word in words:
            if is_subsequence(word):
                count += 1
        
        return count
