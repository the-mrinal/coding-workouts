class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        n = len(jobDifficulty)
        if n < d:
            return -1
        
        @lru_cache(None)
        def dp(i,day): # till index of job completed the prev day or index to start from today
            if day == d:
                return max(jobDifficulty[i:])

            j = n - (d - day)
            min_diff = float('inf')
            for k in range(i,j):
                this_day = max(jobDifficulty[i:k + 1])
                res = this_day + dp(k+1,day + 1)
                if res < min_diff:
                    min_diff = res
            
            return min_diff
        
        return dp(0,1)


# class Solution:
#     def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
#         n = len(jobDifficulty)
        
#         dp = [[float('inf')] * day + 1 for _ in range(n)]
        
#         dp[-1][d] = jobDifficulty[-1]
        
#         for i in range(n-2,-1,-1):
#              dp[i][d] = max(dp[i+1][d],jobDifficulty[i])
        
#         for jobs in range(n + 1):
#             for day in range(d):
                
                
        
        