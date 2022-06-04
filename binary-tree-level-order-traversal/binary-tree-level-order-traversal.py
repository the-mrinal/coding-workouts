# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que = deque([[root,0]])
        ans= []
        
        while que:
            curr,level = que.popleft()
            if len(ans) == level:
                ans.append([])
            ans[-1].append(curr.val)
            
            if curr.left:
                que.append([curr.left,level + 1])

            if curr.right:
                que.append([curr.right,level + 1])
        
        return ans