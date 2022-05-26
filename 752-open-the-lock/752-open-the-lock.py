class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(node):
                for i in range(4):
                    x = int(node[i])
                    for d in (-1, 1):
                        y = (x + d) % 10
                        yield node[:i] + str(y) + node[i+1:]
        queue = deque([("0000",0)])
        visited = {"0000"}
        while queue:
            curr,depth = queue.popleft()
            
            if curr == target:
                return depth
            if curr in deadends:
                continue
            for n in neighbors(curr):
                if n not in visited:
                    queue.append((n,depth + 1))
                    visited.add(n)
        return -1