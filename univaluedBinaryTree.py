# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # dfs based implementation which returns -1 as soon as it encounters node.val different than root.val
        def helper(root):
            if not root: return
            
            left, right = helper(root.left), helper(root.right)
            
            if left == -1 or right == -1 or root.val != self.check_value:
                return -1
            
            return 1
        
        self.check_value = root.val
        res = helper(root)
        return res == 1
