# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que = deque()
        if root:
            que.append([root,0])
        result = []
        
        while que:
            curr,level = que.popleft()
            
            if len(result) == level:
                result.append([])
            result[level].append(curr.val)
            
            if curr.left:
                que.append([curr.left,level + 1])
            
            if curr.right:
                que.append([curr.right,level + 1])
            
        return result