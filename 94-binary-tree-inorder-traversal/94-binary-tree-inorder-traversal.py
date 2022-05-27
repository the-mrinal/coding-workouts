# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if root is None:
#             return []
#         outLeft = self.inorderTraversal(root.left)
        
#         outLeft.append(root.val)
        
#         outLeft += self.inorderTraversal(root.right)
        
#         return outLeft
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            res.append(root.val)
            root = root.right
            
            
            
        return res
            