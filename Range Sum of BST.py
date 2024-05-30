# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.






class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0
        
        sum = 0
        
        if low <= root.val <= high:
            sum += root.val
        
        if root.val > low:
            sum += self.rangeSumBST(root.left, low, high)
        
        if root.val < high:
            sum += self.rangeSumBST(root.right, low, high)
        
        return sum


root1 = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18)))
solution = Solution()
print(solution.rangeSumBST(root1, 7, 15)) 

root2 = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(1), None), TreeNode(7, TreeNode(6), None)), TreeNode(15, TreeNode(13), TreeNode(18)))
print(solution.rangeSumBST(root2, 6, 10)) 
