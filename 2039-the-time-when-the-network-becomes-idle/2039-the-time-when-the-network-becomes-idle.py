class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        
        adjMap = defaultdict(list)
        n = len(edges)
        for a,b in edges:
            adjMap[a].append(b)
            adjMap[b].append(a)
            
        shortest = [float('inf') for i in range(n+1)]
        queue = deque([[0,0]])
        seen = set()
        while queue:
            currPos, currDist = queue.popleft()

            if currPos in seen:
                continue
            seen.add(currPos)
            shortest[currPos] = currDist

            for nei in adjMap[currPos]:
                queue.append((nei, currDist+1))
        
        
        new_res = []
        for dist,pat in zip(shortest,patience):
            if pat > 0:
                num_save = (dist * 2) + (((dist*2)-1)//pat) * pat
                new_res.append(num_save)

        return max(new_res) + 1