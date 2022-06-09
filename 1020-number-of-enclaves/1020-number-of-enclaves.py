class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def dfs(x,y):
            
            st = [(x,y)]
            
            count = 0
            visited = set()
            flag = True
            while st:
                c_x,c_y = st.pop()
                
                count += 1
                grid[c_x][c_y] = 0
                for n_x,n_y in directions:
                    u_x = n_x + c_x
                    u_y = n_y + c_y
                    if u_x < 0 or u_x >= m or u_y < 0 or u_y >= n or grid[u_x][u_y] == 0 or (u_x,u_y) in visited:
                        continue
                    if u_x == 0 or u_y == 0 or u_x == m - 1 or u_y == n - 1:
                        flag = False
                    st.append((u_x,u_y))
                    visited.add((u_x,u_y))
            return count if flag else 0
        
        countsofar = 0
        
        for i in range(1,m - 1):
            for j in range(1,n-1):
                if grid[i][j] == 1:
                    temp = dfs(i,j)
                    countsofar += temp
                    # print(temp,i,j)
        
        return countsofar