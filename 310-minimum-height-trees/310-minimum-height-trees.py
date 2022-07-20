class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2: return [i for i in range(n)]
        indeg = {i:0 for i in range(n)}
        adjMap = {i:[] for i in range(n)}
        
        for a,b in edges:
            indeg[a] += 1
            indeg[b] += 1
            adjMap[a].append(b)
            adjMap[b].append(a)
            
        leaf = deque()
        for a,childs in adjMap.items():
            if len(childs) == 1:
                leaf.append(a)
        
        remaining = n
        while remaining > 2:
            remaining -= len(leaf)
            new_leaf = deque()
            while leaf:
                curr = leaf.popleft()
                
                parent = adjMap[curr].pop()
                
                adjMap[parent].remove(curr)
                
                if len(adjMap[parent]) == 1:
                    new_leaf.append(parent)
            
            leaf = new_leaf
        
        return leaf
            
            