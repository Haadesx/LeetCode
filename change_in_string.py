class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        key_changes = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i-1].lower():
                key_changes += 1
        return key_changes

# Example usage:
solution = Solution()
print(solution.countKeyChanges("aAbBcC"))  # Output: 2
print(solution.countKeyChanges("AaAaAaaA"))  # Output: 0
