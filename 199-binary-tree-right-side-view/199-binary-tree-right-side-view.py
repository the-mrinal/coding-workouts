# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        que = deque()
        if root:
            que.append(root)
        result = []
        
        while que:
            size = len(que)
            prev = -1
            for i in range(size):
                curr = que.popleft()
                prev = curr
                
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
            result.append(prev.val)
        return result