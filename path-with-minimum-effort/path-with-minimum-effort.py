class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        
        
        def costFun(a,b):
            xi,yi = a
            xj,yj = b
            return abs(heights[xi][yi] - heights[xj][yj])
        
        
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        
        adjMap = defaultdict(list)
        
        for row in range(m):
            for col in range(n):
                for a,b in directions:
                    n_row = row + a
                    n_col = col + b
                    if n_row < 0 or n_row >= m or n_col < 0 or n_col >= n:
                        continue
                    adjMap[(row,col)].append((n_row,n_col))
        
        curr_min = defaultdict(list)
        
        curr_min[(0,0)] = 0
        
        que = deque([(0,0)])
        
        visited = set()
        visited.add((0,0))
        
        while que:
            curr = que.popleft()
            
            visited.remove(curr)
            
            for nxt in adjMap[curr]:
                if nxt not in curr_min or (curr_min[nxt] > max(curr_min[curr], costFun(curr,nxt))):
                    curr_min[nxt] = max(curr_min[curr], costFun(curr,nxt))
                    if nxt not in visited:
                        visited.add(nxt)
                        que.append(nxt)
        
        return curr_min[(m-1,n-1)]
                
        
        
        
        
        
        
        