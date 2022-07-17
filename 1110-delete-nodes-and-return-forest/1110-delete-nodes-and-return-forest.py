# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        
        
        def helperFunction(root):
            nonlocal ans
            if root:
                root.left = helperFunction(root.left)
                root.right = helperFunction(root.right)
    
                if root.val in to_delete:
                    if root.left:
                        ans.append(root.left)
                    if root.right:
                        ans.append(root.right)
                    root = None
                return root
            else:
                return None
        root = helperFunction(root)
        if root:
            ans.append(root)
        return ans