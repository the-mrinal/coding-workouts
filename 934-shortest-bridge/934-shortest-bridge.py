class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        islandA = []
        bound = []
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        #find rooot is islandA 
        def findRoot():
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        return (i,j)
            return (-1,-1)
        
        def dfs():
            root = findRoot()
            stack = [root]
            
            while stack:
                a,b = stack.pop()
                
                grid[a][b] = -1
                islandA.append((a,b))
                for n_x,n_y in directions:
                    x = n_x + a
                    y = n_y + b
                    if x < 0 or x >= n or y < 0 or y >= n or grid[x][y] < 0:
                        continue
                    if grid[x][y] == 0:
                        bound.append((x,y))
                    else:
                        stack.append((x,y))
        
        def findMinRoute():
            nonlocal bound
            step = 1
            while bound:
                new = []
                for i, j in bound:
                    for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                        if 0 <= x < n and 0 <= y < n:
                            if grid[x][y] == 1:
                                return step
                            elif not grid[x][y]:
                                grid[x][y] = -1
                                new.append((x, y))
                step += 1
                bound = new
        
        dfs()
        return findMinRoute()
        
                    
                    
                    
                    
                    
                    
                    
            
            
            
            
            