class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbours = defaultdict(list)
        
        for a,b in edges:
            neighbours[a].append(b)
            neighbours[b].append(a)
        
        seen = set([source])
        
        que = deque([source])
        
        while que:
            curr = que.popleft()
            
            if curr == destination:
                return True
            
            
            for n in neighbours[curr]:
                if n not in seen:
                    que.append(n)
                    seen.add(n)
                
        return False