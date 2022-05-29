class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid) - 1
        n = len(grid[0]) - 1
        
        
        if grid[0][0] == 1 or grid[m][n] == 1:
            return -1
        
        directions = [[1,0],[0,1],[-1,0],[0,-1],[-1,-1],[1,1],[-1,1],[1,-1]]
        
        que = deque([[0,0,1]])
        
        def findNeigbors(i,j):
            res = []
            for r,c in directions:
                n_r = r + i
                n_c = c + j
                if n_r < 0 or n_r > m or n_c < 0 or n_c > n or grid[n_r][n_c] != 0:
                    continue
                
                res.append([n_r,n_c])
            return res
        seen = set()
        while que:
            r,c,dist = que.popleft()
            print(r,c,dist)
            if [r,c] == [n,n]:
                return dist
            
            for n_r,n_c in findNeigbors(r,c):
                if (n_r,n_c) not in seen:
                    que.append([n_r,n_c,dist + 1])
                    seen.add((n_r,n_c))
        
        return -1
            
            
            