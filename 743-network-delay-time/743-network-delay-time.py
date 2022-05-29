class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #create adj map
        adjMap = defaultdict(list)
        
        for src,dest,time in times:
            adjMap[src].append((dest,time))
            
        
        que = [(0,k)]
        visited = set()
        max_cost = 0

        
        while que:
            
            cost,node = heapq.heappop(que)
            
            if node in visited:
                continue
            
            visited.add(node)
            
            max_cost = max(max_cost,cost)
            
            neighbours = adjMap[node]
        
        
            for ne in neighbours:
                n_node,n_cost = ne
                
                if n_node not in visited:
                    new_cost = cost + n_cost
                    heapq.heappush(que,(new_cost,n_node))
        
        return max_cost if len(visited) == n else -1