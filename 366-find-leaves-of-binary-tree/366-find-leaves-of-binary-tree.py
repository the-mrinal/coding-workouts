# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
# #         Time = O(n^2) <- bad
#         curr = root
#         ans = []
#         while root:
#             if not root.left and not root.right:
#                 ans.append([root.val])
#                 root = None
#                 continue
#             ans.append([])
#             que = deque([[root,None,-1]])
#             while que:
#                 curr,curr_root,side = que.popleft()
#                 if not curr.left and not curr.right:
#                     ans[-1].append(curr.val)
#                     if side == 1:
#                         curr_root.left = None
#                     elif side == 0:
#                         curr_root.right = None
#                     continue

#                 if curr.right:
#                     que.append([curr.right,curr,0])
#                 if curr.left:
#                     que.append([curr.left,curr,1])
            
#         return ans
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
#         time = O(N) 
        ans = defaultdict(list)
        def dfs(node,layer):
            if not node:
                return layer
            left = dfs(node.left,layer)
            right = dfs(node.right,layer)
            
            layer = max(left,right)
            
            ans[layer].append(node.val)
            
            return layer + 1
        
        dfs(root,0)
        return ans.values()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            