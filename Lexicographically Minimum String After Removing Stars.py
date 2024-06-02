class Solution(object):
    def clearStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for char in s:
            if char == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)

# Example usage
sol = Solution()
print(sol.clearStars("de*")) 