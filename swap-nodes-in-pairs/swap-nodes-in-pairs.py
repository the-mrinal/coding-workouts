# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(prev,curr,count):
            if curr is None:
                return
            
            if count % 2 == 1:
                prev.val,curr.val = curr.val,prev.val
            
            helper(curr,curr.next,count + 1)
        
        if head and head.next:
            helper(head,head.next,1)
        return head