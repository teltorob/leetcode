# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        res =[]
        
        if not root1:
            res = self.inorder(root2, [])
            
        elif not root2:
            res = self.inorder(root1, [])
            
        else:
            res = self.inorder(root1, []) + self.inorder(root2, [])
            
        res.sort()
        return res
        
        
    def inorder(self, node, array):
        if not node:
            return
        
        self.inorder(node.left, array)
        array.append(node.val)
        self.inorder(node.right, array)
        return array
        
        
        
        
        
            
            
            