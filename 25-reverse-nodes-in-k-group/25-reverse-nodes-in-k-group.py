# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def magicFunction(curr_node,n):
            prev = None
            new_h = curr_node
            while n:
                nxt = curr_node.next
                curr_node.next = prev
                prev = curr_node
                curr_node = nxt
                n -= 1
            return prev

        curr = head
        count = 0
        while count < k and curr:
            count += 1
            curr = curr.next
        
        if count == k:
            revHead = magicFunction(head,k)
            
            head.next = self.reverseKGroup(curr,k)
            
            return revHead
        
        return head
        
        
        return head

