# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, node: Optional[TreeNode]) -> bool:
        
        def checkValidBST(root,lo,hi):
            if root.val <= lo or root.val >= hi:
                return False
            
            left = right = True
            if root.left:
                left = checkValidBST(root.left,lo,root.val)
            
            if root.right:
                right = checkValidBST(root.right,root.val,hi)
            
            return left and right
        
        return checkValidBST(node,float('-inf'),float('inf'))