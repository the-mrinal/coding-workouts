class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], src: int, dest: int) -> bool:

            adjMap = defaultdict(list)

            for start,end in edges:
                adjMap[start].append(end)

            visited = set()
            
            def dfs(v):
                if v in visited:
                    return False
                
                if not adjMap[v]:
                    return v == dest
                
                visited.add(v)
                for neigh in adjMap[v]:
                    if not dfs(neigh):
                        return False
                
                visited.remove(v)
                return True
            
            return dfs(src)