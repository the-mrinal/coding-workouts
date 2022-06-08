class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i <= 0:
                    grid[i][j] = grid[i][j]
                elif j <= 0:
                    grid[i][j] = grid[i][j] + min(grid[i-1][j],grid[i-1][j+1])
                elif j >= n-1:
                    grid[i][j] = grid[i][j] + min(grid[i-1][j],grid[i-1][j-1])
                else:
                    grid[i][j] = grid[i][j] + min(grid[i-1][j],grid[i-1][j-1],grid[i-1][j+1])
        return min(grid[m-1])