# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que = deque()
        
        if root:
            que.append([root,0])
        
        res = []
        
        while que:
            curr,level = que.popleft()
            
            if len(res) == level:
                res.append([])
                
            if level % 2 != 0:
                res[level] = [curr.val] + res[level]
            else:
                res[level].append(curr.val)
            
            if curr.left:
                que.append([curr.left,level + 1])
            if curr.right:
                que.append([curr.right,level + 1])
        
        return res