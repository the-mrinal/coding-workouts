class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = {}
        
        MOD = 10**9 + 7
        
        def dfs(currSumLeft,currDiceLeft):
            if currSumLeft < 0:
                return 0
            if currDiceLeft == 0:
                if currSumLeft == 0:
                    return 1
                return 0
            key = (currSumLeft,currDiceLeft)
            
            if key not in dp:
                dp[key] = 0
                for i in range(1,k + 1):
                    if currSumLeft - i >= 0:
                        dp[key] = (dp[key] + dfs(currSumLeft - i,currDiceLeft - 1))% MOD
            return dp[key]
        
        dfs(target,n)
        return dp[(target,n)]%MOD