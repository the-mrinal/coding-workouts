# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        que = deque()
        que.append((p,q))
        
        while que:
            curr_p,curr_q = que.popleft()
            
            if not curr_p and not curr_q:
                continue
            if not curr_p or not curr_q:
                return False
            
            if curr_p.val != curr_q.val:
                # curr_
                return False
            
            que.append((curr_p.left,curr_q.left))
            que.append((curr_p.right,curr_q.right))            
        
        return True