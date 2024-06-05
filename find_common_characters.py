# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
 

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.



from collections import Counter

class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # Initialize with the character count of the first word
        common_count = Counter(words[0])
        
        # Iterate over the rest of the words
        for word in words[1:]:
            word_count = Counter(word)
            # Take the intersection of counts
            common_count &= word_count
        
        # Expand the counts to the list of common characters
        result = []
        for char, count in common_count.items():
            result.extend([char] * count)
        
        return result


