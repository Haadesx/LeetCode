# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Start with the first string in the list as the common prefix
        prefix = strs[0]

        for string in strs[1:]:
            # Reduce the prefix length until it matches the start of the string
            while string[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix

# Test cases
solution = Solution()

print(solution.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))    # Output: ""
print(solution.longestCommonPrefix(["interstellar", "internet", "internal"]))  # Output: "inte"
print(solution.longestCommonPrefix(["a"]))  # Output: "a"
print(solution.longestCommonPrefix([""]))  # Output: ""
print(solution.longestCommonPrefix(["reflower", "flow", "flight"]))  # Output: ""
