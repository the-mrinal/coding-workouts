# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     curr = head
    #     prev = None
    #     while curr:
    #         temp = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = temp
    #     return prev
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        def revll(root):
            if root.next is None:
                return (root,root)
            
            res,newH = revll(root.next)
            
            res.next = root
            
            return (root,newH)
        root,newH = revll(head)
        root.next = None
        return newH