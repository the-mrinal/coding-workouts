class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)]for _ in range(m)]
        
        for i in range(n):
            dp[0][i] = grid[0][i]
        
        for i in range(1,m):
            for j in range(n):
                minVal = float('inf')
                for k in range(n):
                    minVal = min(minVal,moveCost[grid[i - 1][k]][j] + dp[i - 1][k])
                dp[i][j] = minVal + grid[i][j]
        
        return min(dp[m - 1])