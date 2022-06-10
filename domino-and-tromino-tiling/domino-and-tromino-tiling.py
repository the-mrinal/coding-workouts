class Solution:
    def numTilings(self, d: int) -> int:
        dp = {}
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        MOD = 10**9 + 7
        for n in range(4,d + 1):
            dp[n] = ((2 * dp[n - 1])%MOD+ (dp[n - 3])%MOD)%MOD
        return dp[d]