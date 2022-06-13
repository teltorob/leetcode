# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # dfs implementation of maximum depth, reaches the end node and starts counting from there
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def helper(root):
            
            if not root: return 0
            
            left, right = helper(root.left), helper(root.right)
            return 1 + max(left, right) # first counted node will be the deepest node in the tree (left, right = 0)
        
        return helper(root)
