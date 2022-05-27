class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        sum_sq = [i*i for i in range(1,int(math.sqrt(n))+ 1)]
        
        for i in range(1,n + 1):
            temp = []
            for sq in sum_sq:
                if sq > i:
                    break
                temp.append(dp[i - sq] + 1)
            dp[i] = min(temp)
        
        return dp[n]