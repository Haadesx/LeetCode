# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pseudoPalindromicPaths(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, path):
            if not node:
                return 0
            
            # XOR the path with the bit corresponding to the current node's value
            path ^= 1 << node.val
            
            # If it's a leaf node, check the path for pseudo-palindromic property
            if not node.left and not node.right:
                # Check if at most one bit is set in path (which corresponds to at most one odd count)
                if path & (path - 1) == 0:
                    return 1
                else:
                    return 0
            
            # Continue the DFS on children nodes
            left_paths = dfs(node.left, path)
            right_paths = dfs(node.right, path)
            
            return left_paths + right_paths
        
        return dfs(root, 0)