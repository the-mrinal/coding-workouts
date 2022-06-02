# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def bst(node,lo,hi):
            if not node:
                return True

            if node.val <= lo or node.val >= hi:
                return False

            return bst(node.left,lo,node.val) and bst(node.right,node.val,hi)

        return bst(root,float('-inf'),float('inf'))