class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        WHITE,GREY,BLACK = 0,1,2
        
        colors = defaultdict(int)
        
        def dfs(node):
            if colors[node] != WHITE:
                return colors[node] == BLACK
            
            colors[node] = GREY # making this busy
            for neigh in graph[node]:
                if colors[neigh] == BLACK:
                    continue
                if colors[neigh] == GREY or not dfs(neigh):
                    return False
            colors[node] = BLACK
            return True
        
        return filter(dfs,range(len(graph)))
            