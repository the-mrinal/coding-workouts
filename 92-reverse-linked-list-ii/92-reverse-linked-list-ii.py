# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        
        curr,prev = head,None
        while curr and m > 1:
            prev = curr
            curr = curr.next
            m-= 1
            n -= 1
        tail,con = curr,prev
        
        while n:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            n -= 1
        
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = curr
        return head
        
        
        
        
        
        