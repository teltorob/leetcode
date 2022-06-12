# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(node, array):
            if not array:
                return None
            
            root = max(array)
            root_idx = array.index(root)
            
            node = TreeNode(root)
            node.left = helper(node, array[: root_idx])
            node.right = helper(node, array[root_idx + 1:])
            
            return node
        

        node = TreeNode(0)

        return helper(node, nums)
            


