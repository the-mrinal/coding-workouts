"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        prev_node = [None,-1]
        que = deque([[root,0]])
        
        while que:
            curr,level = que.popleft()
            prev,p_level = prev_node
            # print(curr,level)
            if level == p_level:
                prev.next = curr
            prev_node = [curr,level]
            
            if curr.left:
                que.append([curr.left,level + 1])
            
            if curr.right:
                que.append([curr.right,level + 1])
                
        return root