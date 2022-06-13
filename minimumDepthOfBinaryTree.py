# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Slightly modified Maximum Dpeth Tree to make it work
        def helper(root):

            if not root: return 0

            left, right = helper(root.left), helper(root.right)
            
            if None in [root.left, root.right]: return 1 + max(left, right)
            else: return 1 + min(left, right) 
        
        return helper(root)
       
