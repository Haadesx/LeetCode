# Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

# A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

 

# Example 1:


# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
# Example 2:


# Input: root = [2,1,3]
# Output: [2,1,3]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# 1 <= Node.val <= 105

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Step 1: Get the sorted list of values from the BST
        sorted_values = self.inorderTraversal(root)
        
        # Step 2: Build the balanced BST from the sorted values
        return self.sortedListToBST(sorted_values)
    
    def inorderTraversal(self, root):
        # Helper function to perform inorder traversal
        result = []
        self.inorderHelper(root, result)
        return result
    
    def inorderHelper(self, node, result):
        if not node:
            return
        self.inorderHelper(node.left, result)
        result.append(node.val)
        self.inorderHelper(node.right, result)
    
    def sortedListToBST(self, sorted_values):
        # Helper function to build balanced BST from sorted list
        if not sorted_values:
            return None
        return self.buildBST(sorted_values, 0, len(sorted_values) - 1)
    
    def buildBST(self, values, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        node = TreeNode(values[mid])
        node.left = self.buildBST(values, left, mid - 1)
        node.right = self.buildBST(values, mid + 1, right)
        return node

# Example usage:
# Input: root = [1,null,2,null,3,null,4,null,null]
# Expected output: [2,1,3,null,null,null,4]
root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
sol = Solution()
balanced_root = sol.balanceBST(root)

# The function `balanceBST` can be tested with different input trees to verify the output.
