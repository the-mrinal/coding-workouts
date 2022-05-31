# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        def helper(l1,l2,sortedHead):
            if not l1 or not l2:
                tail = l1 if l1 else l2
                sortedHead.next = tail
                return sortedHead
            
            if l1.val > l2.val:
                sortedHead.next = l2
                sortedHead = sortedHead.next
                return helper(l1,l2.next,sortedHead)
            else:
                sortedHead.next = l1
                sortedHead = sortedHead.next
                return helper(l1.next,l2,sortedHead)
            
        sortedHead = ListNode(-1)
        helper(list1,list2,sortedHead)
        return sortedHead.next