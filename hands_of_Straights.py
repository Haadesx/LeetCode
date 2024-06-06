# 846. Hand of Straights
# Solved
# Medium
# Topics
# Companies
# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

 

# Example 1:

# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
# Example 2:

# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.

 

# Constraints:

# 1 <= hand.length <= 104
# 0 <= hand[i] <= 109
# 1 <= groupSize <= hand.length

from collections import Counter

class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False
        
        card_count = Counter(hand)
        sorted_cards = sorted(card_count.keys())
        
        for card in sorted_cards:
            while card_count[card] > 0:
                for i in range(groupSize):
                    if card_count[card + i] > 0:
                        card_count[card + i] -= 1
                    else:
                        return False
        return True