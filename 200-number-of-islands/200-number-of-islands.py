class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        
        m = len(grid)
        n = len(grid[0])
        islands = 0
        
#         space = []
#         for i in range(m):
#             space.append([])
#             for j in range(n):
#                 space[i].append(False)
        
        
#         def connectIsland(queue):
#             while queue:
#                 r_c,c_c = queue.popleft()
#                 for r_d,c_d in directions:
#                     r_n = r_c + r_d
#                     c_n = c_c + c_d
                    
#                     if (r_n < 0 or r_n >= m or c_n < 0 or c_n >= n or space[r_n][c_n] == True or grid[r_n][c_n] == "0"):
#                         continue
                    
#                     space[r_n][c_n] =  True
#                     queue.append([r_n,c_n])
                        
        
        
        def dfs(dfsgrid,r,c):
            if (r < 0 or r>= m or c<0 or c>=n or dfsgrid[r][c] == "0"):
                return
            dfsgrid[r][c] = "0"
            dfs(dfsgrid,r - 1,c)
            dfs(dfsgrid,r + 1,c)
            dfs(dfsgrid,r,c - 1)
            dfs(dfsgrid,r,c + 1)

        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(grid,i,j)
        
        return islands