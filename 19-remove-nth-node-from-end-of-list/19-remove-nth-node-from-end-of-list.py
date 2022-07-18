# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        fast and slow pointers
        
        1 - 2 - 3 - 5 - 6
        
        4th node from last
        
        1 - 3 - 5 - 6
        
        while fast:
            fast = fast.next
            count += 1
            if count == K + 1:
                slow = slow.next
            else:
                count += 1
        if count == k -1:
            return head.next
        
        slow.next = slow.next.next
        
        '''
        fast=slow = head
        count = 0
        while fast:
            if count == k + 1:
                slow = slow.next
            else:
                count += 1
            fast = fast.next
        
        if count == k:
            return head.next

        slow.next = slow.next.next
        return head