# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         res = []
        
#         def levelOrderRec(root,level):
#             if root is None:
#                 return 
#             if len(res) == level:
#                 res.append([])
                
#             res[level].append(root.val)
            
#             levelOrderRec(root.left,level + 1)

                
#             levelOrderRec(root.right,level + 1)
            
            
#             return
        
#         def levelOrderIter(root):
#             ret = []

#             level = [root]

#             while root and level:
#                 currentNodes = []
#                 nextLevel = []
#                 for node in level:
#                     currentNodes.append(node.val)
#                     if node.left:
#                         nextLevel.append(node.left)
#                     if node.right:
#                         nextLevel.append(node.right)
#                 ret.append(currentNodes)
#                 level = nextLevel


#             return ret
        
        
        que = deque()
        if root:
            que.append((root,0))
        ans = []
        
        while que:
            curr,level = que.popleft()
            if len(ans) == level:
                ans.append([])
            ans[level].append(curr.val)
            
            if curr.left:
                que.append((curr.left,level + 1))
                
            if curr.right:
                que.append((curr.right,level + 1))
        
        
        return ans