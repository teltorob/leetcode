# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        check = False
        
        
        def li_li (head, arr):
            while head:
                arr.append(head.val)
                head = head.next
            return arr
                
        
        def check_child(node, l):
            nonlocal check
            
            if not node:
                return 
            
            if l == linked:
                check = True
                return 
            
            if len(l) > len(linked):
                return
            
            if (node.left and node.left.val == linked[len(l)]):
                check_child(node.left, l+[node.left.val])
            if (node.right and node.right.val == linked[len(l)]):
                check_child(node.right, l+[node.right.val])
                
        
        def tree(root):
            if not root: return
            
            if root.val == linked[0]:
                check_child(root, [root.val])

            
            tree(root.left)
            tree(root.right)
                    
        linked = li_li(head, [])
        tree(root)
        
        return check
        
        
        
        
        