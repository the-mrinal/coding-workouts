class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        lockedLand = 0
        
        def dfs(x,y):
            nonlocal lockedLand
            st = [(x,y)]
            visited = set()
            visited.add((x,y))
            isClosed = True
            while st:
                c_x,c_y = st.pop()

                grid[c_x][c_y] = 1
                
                for n_x,n_y in directions:
                    u_x = n_x + c_x
                    u_y = n_y + c_y 
                    if u_x < 0 or u_x >= m or u_y < 0 or u_y >= n or grid[u_x][u_y] == 1 or (u_x,u_y) in visited:
                        continue
                    if (u_x == 0 or u_x == m-1) and grid[u_x][u_y] == 0:
                        isClosed = False
                    if (u_y == 0 or u_y == n-1) and grid[u_x][u_y] == 0:
                        isClosed = False
                    st.append((u_x,u_y))
                    visited.add((u_x,u_y))
            if isClosed:
                lockedLand += 1
        
        for i in range(1,m-1):
            for j in range(1,n-1):
                if grid[i][j] == 0:
                    dfs(i,j)
        
        return lockedLand