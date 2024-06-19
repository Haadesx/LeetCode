# 1239. Maximum Length of a Concatenated String with Unique Characters
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

# Return the maximum possible length of s.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All the valid concatenations are:
# - ""
# - "un"
# - "iq"
# - "ue"
# - "uniq" ("un" + "iq")
# - "ique" ("iq" + "ue")
# Maximum length is 4.
# Example 2:

# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
# Example 3:

# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26
# Explanation: The only string in arr has all 26 characters.
 

# Constraints:

# 1 <= arr.length <= 16
# 1 <= arr[i].length <= 26
# arr[i] contains only lowercase English letters.



class Solution:
    def maxLength(self, arr):
        def is_unique(s):
            return len(s) == len(set(s))
        
        def backtrack(index, current_string):
            if is_unique(current_string):
                max_length[0] = max(max_length[0], len(current_string))
            if index == len(arr):
                return
            for i in range(index, len(arr)):
                backtrack(i + 1, current_string + arr[i])
        
        max_length = [0]  # Use a list to store the maximum length
        backtrack(0, "")
        return max_length[0]