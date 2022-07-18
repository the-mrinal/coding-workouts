# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def findMiddle(root):
            fast = root
            slow = root
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def reverse(root):
            curr = root
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        def mergeTwo(root1,root2):

            while root2.next:
                temp = root1.next
                root1.next = root2
                root1 = temp
                
                temp = root2.next
                root2.next = root1
                root2 = temp
        
        middle = findMiddle(head)
        root2 = reverse(middle)
        mergeTwo(head,root2)
            
            
            
            
            
            
            
            
            