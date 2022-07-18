# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        totalSum = head
        carry = 0
        while l1 and l2:
            curr = l1.val + l2.val + carry
            currNode = ListNode(curr%10)
            if totalSum:
                totalSum.next = currNode
                totalSum = totalSum.next
            else:
                totalSum = currNode
                head = totalSum
            carry = curr// 10
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            if carry > 0:
                while l1:
                    curr = l1.val + carry
                    currNode = ListNode(curr%10)
                    totalSum.next = currNode
                    totalSum = totalSum.next
                    carry = curr // 10
                    l1 = l1.next
            totalSum.next = l1
        if l2:
            if carry > 0:
                while l2:
                    curr = l2.val + carry
                    currNode = ListNode(curr%10)
                    totalSum.next = currNode
                    totalSum = totalSum.next
                    carry = curr // 10
                    l2 = l2.next
            totalSum.next = l2
        if carry:
            currNode = ListNode(carry)
            totalSum.next = currNode
        
        return head