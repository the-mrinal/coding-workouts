# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = defaultdict(list)
        
        def dfs(node,layer):
            if node is None:
                return layer
            left = dfs(node.left,layer)
            right = dfs(node.right,layer)
            
            layer = max(left,right)
            
            ans[layer].append(node.val)
            layer += 1
            return layer
        
        dfs(root,0)
        return ans.values()