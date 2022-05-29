class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        m = len(grid)

        n = len(grid[0])
        
        que = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    que.append([i,j,0])
        
        maxTime = 0
        
        while que:
            r,c,time = que.popleft()
            
            for d_r,d_c in  directions:
                n_r = r + d_r
                n_c = c + d_c
                
                if n_r < 0 or n_r >= m or n_c < 0 or n_c >= n or grid[n_r][n_c] != 1:
                    continue
                
                que.append([n_r,n_c,time + 1])
                grid[n_r][n_c] = 2
                maxTime = time + 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return maxTime