class Solution:
    def validPath(self, n: int, edges: List[List[int]], src: int, dest: int) -> bool:
        adjMap = defaultdict(list)
	
        for a,b in edges:
            adjMap[a].append(b)
            adjMap[b].append(a)

        que = deque([src])
        
        visited = set()
        while que:
            curr = que.popleft()
            if curr == dest:
                return True
            for neigh in adjMap[curr]:
                if neigh not in visited:
                    que.append(neigh)
                    visited.add(neigh)
        return False
