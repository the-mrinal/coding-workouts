# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que = deque([])
        que.append([root,0])
        result = []
        
        while que:
            size = len(que)
            currLevel = deque()
            for i in range(size):
                curr,level = que.popleft()

                if level % 2 == 0:
                    currLevel.append(curr.val)
                else:
                    currLevel.appendleft(curr.val)

                if curr.left:
                    que.append([curr.left,level + 1])

                if curr.right:
                    que.append([curr.right,level + 1])
            
            result.append(list(currLevel))
            
        return result