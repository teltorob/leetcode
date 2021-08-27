# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head=ListNode(0)
        temp=head                   #Storing temporary head
            
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next=l1
                l1=l1.next
            else:
                temp.next=l2
                l2=l2.next
            temp=temp.next
        temp.next = l1 or l2

        return head.next            #returning head.next to skip initial 0