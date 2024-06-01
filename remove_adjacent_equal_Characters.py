# 2957. Remove Adjacent Almost-Equal Characters
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given a 0-indexed string word.

# In one operation, you can pick any index i of word and change word[i] to any lowercase English letter.

# Return the minimum number of operations needed to remove all adjacent almost-equal characters from word.

# Two characters a and b are almost-equal if a == b or a and b are adjacent in the alphabet.

 

# Example 1:

# Input: word = "aaaaa"
# Output: 2
# Explanation: We can change word into "acaca" which does not have any adjacent almost-equal characters.
# It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 2.
# Example 2:

# Input: word = "abddez"
# Output: 2
# Explanation: We can change word into "ybdoez" which does not have any adjacent almost-equal characters.
# It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 2.
# Example 3:

# Input: word = "zyxyxyz"
# Output: 3
# Explanation: We can change word into "zaxaxaz" which does not have any adjacent almost-equal characters. 
# It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 3.
 

# Constraints:

# 1 <= word.length <= 100
# word consists only of lowercase English letters.



class Solution(object):
    def removeAlmostEqualCharacters(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        operations = 0
        word = list(word)  # Convert to list to allow modification

        for i in range(n -1):
            if abs(ord(word[i]) - ord(word[i + 1])) <= 1:
                operations += 1
                # Change word[i + 1] to a character that is not almost-equal to word[i] and word[i + 2] (if it exists)
                for j in range(26):  # There are 26 letters in the English alphabet
                    new_char = chr((ord(word[i]) - ord('a') + 2 + j) % 26 + ord('a'))
                    if (i + 2 < n and abs(ord(new_char) - ord(word[i + 2])) > 1) or i + 2 >= n:
                        word[i + 1] = new_char
                        break

        return operations

# Example usage:
solution = Solution()
print(solution.removeAlmostEqualCharacters("aaaaa"))  # Output: 2
print(solution.removeAlmostEqualCharacters("abddez"))  # Output: 2
print(solution.removeAlmostEqualCharacters("zyxyxyz"))  # Output: 3
