class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0]*2 for _ in range(k+1)] for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            for j in range(1,k+1):
                for isHolding in range(2):
                    doNothing = dp[i+1][j][isHolding]
                    if isHolding == 0:
                        doSomething = -prices[i] + dp[i+1][j][1]
                    else:
                        doSomething = prices[i] + dp[i+1][j - 1][0]
                    dp[i][j][isHolding] = max(doNothing,doSomething)
        
        return dp[0][k][0]
