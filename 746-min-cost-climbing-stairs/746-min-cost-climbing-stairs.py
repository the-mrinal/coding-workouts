# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         n = len(cost)
#         if n == 1:
#             return cost[0]
#         if n < 3:
#             return min(cost[0],cost[1])        
        
#         def dp(i):
#             if i <= 1:
#                 return 0
            
#             if i not in memo:
#                 memo[i] = min(dp(i-1)+cost[i-1] , dp(i-2) + cost[i-2])
            
#             return memo[i]
        
#         memo = {}
#         return dp(n)
        

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0 for _ in range(n + 1)]
        
        dp[0] = 0
        dp[1] = 0
        
        for i in range(2,n+1):
            dp[i] = min(dp[i-1] + cost[i-1] ,dp[i-2] + cost[i-2])
        
        return dp[n]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        