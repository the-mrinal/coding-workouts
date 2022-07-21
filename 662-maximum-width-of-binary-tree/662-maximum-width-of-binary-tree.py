# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        que = deque()
        if root:
            que.append([root,0])
        
        maxWidth = 0
        
        while que:
            len_curr_level = len(que)
            _,head_index = que[0]
            for _ in range(len_curr_level):
                curr,col_index = que.popleft()
                
                if curr.left:
                    que.append([curr.left,2*col_index])
                
                if curr.right:
                    que.append([curr.right, 2* col_index + 1])
            maxWidth = max(maxWidth,col_index - head_index + 1)
        
        return maxWidth
            
            