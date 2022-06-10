# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        # helper function for dfs
        def check(root):
            
            if not root: return 0
            
            left = check(root.left)
            right = check(root.right)
            
            self.res += abs(left - right)           #summing up the tilt for each subtree

            return root.val + left + right          #returning sum of total child element of a subtree
            
        
        self.res = 0
        check(root)
        return(self.res)
