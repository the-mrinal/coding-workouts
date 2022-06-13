class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        stack = []
        n = len(graph)
        res = []
        def dfs():
            stack.append([0,[0]])
            
            visited = set()
            visited.add(0)
            while stack:
                curr,path = stack.pop()
                
                if curr == n - 1:
                    res.append(path.copy())
                    continue
                for neigh in graph[curr]:
                    if neigh is not visited:
                        stack.append([neigh,path+[neigh]])
                        visited.add(neigh)
        dfs()
        return res