class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        grid = [[0 if obstacleGrid[i][j] == 1 else 1 for j in range(n)] for i in range(m)]
        
        if grid[0][0] == 0 or grid[m-1][n-1] == 0:
            return 0
        
                # Filling the values for the first column
        for i in range(1,m):
            grid[i][0] = 1 if grid[i][0] == 1 and grid[i-1][0] == 1 else 0

        # Filling the values for the first row        
        for j in range(1, n):
            grid[0][j] =  1 if grid[0][j] == 1 and grid[0][j-1] == 1 else 0
        
        for i in range(1,m):
            for j in range(1,n):
                if grid[i][j] == 1:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
                else:
                    grid[i][j] = 0
        return grid[m-1][n-1]