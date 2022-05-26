class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        
        m = len(grid)
        n = len(grid[0])
        islands = 0
        
        space = []
        for i in range(m):
            space.append([])
            for j in range(n):
                space[i].append(False)
        
        
        def connectIsland(queue):
            while queue:
                r_c,c_c = queue.popleft()
                for r_d,c_d in directions:
                    r_n = r_c + r_d
                    c_n = c_c + c_d
                    
                    if (r_n < 0 or r_n >= m or c_n < 0 or c_n >= n or space[r_n][c_n] == True or grid[r_n][c_n] == "0"):
                        continue
                    
                    space[r_n][c_n] =  True
                    queue.append([r_n,c_n])
                        
        
        
        for i in range(m):
            queue = deque([])
            for j in range(n):
                if grid[i][j] == "1" and space[i][j] == False:
                    islands += 1
                    queue.append([i,j])
                    connectIsland(queue)
        
        return islands