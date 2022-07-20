# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
    
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def preorderTraversal(node):
            if not node:
                return False
            
            isFoundLeft = preorderTraversal(node.left)
            
            isFoundRight = preorderTraversal(node.right)
            
            mid = node == p or node == q
            
            if int(mid) + int(isFoundLeft) + int(isFoundRight) >= 2:
                self.ans = node
            
            return isFoundLeft or isFoundRight or mid
        
        preorderTraversal(root)
        return self.ans
        
        