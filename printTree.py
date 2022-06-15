# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def helper_height(root):                            # helper function to get height using dfs
            if not root: return 0
            left, right = helper_height(root.left), helper_height(root.right)
            return 1 + max(left, right)
        
        def make_tree(root, row, left, right):              # helper funtion that inserts root.val in the middle of partition
            if not root: return
            
            # mid = left + (right - left) // 2
            mid = (left + right) // 2
            self.res[row][mid] = str(root.val)
            
            make_tree(root.left, row + 1, left, mid - 1)
            make_tree(root.right, row + 1, mid + 1, right)
            
            

        m = helper_height(root) 
        n = 2 ** m - 1
        
        self.res = [[''] * n for _ in range(m)]
        
        make_tree(root, 0, 0, n - 1)
        return self.res
