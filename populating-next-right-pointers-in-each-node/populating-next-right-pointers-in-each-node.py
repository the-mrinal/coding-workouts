class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        prev = None
        prev_l = -1
        que = deque([[root,0]])
        while que:
            curr,level = que.popleft()

            if level == prev_l:
                prev.next = curr
            prev = curr
            prev_l = level

            if curr.left:
                que.append([curr.left,level + 1])
            if curr.right:
                que.append([curr.right,level + 1])
        
        return root