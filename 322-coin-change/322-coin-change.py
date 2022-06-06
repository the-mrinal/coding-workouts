# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
        
#         @lru_cache(None)
#         def dp(sumLeft):
#             if sumLeft < 0:
#                 return float('inf')
#             if sumLeft == 0:
#                 return 0

#             min_count = float(inf)
#             for coin in coins:
#                 res = 1 + dp(sumLeft - coin)
#                 if res < min_count:
#                     min_count = res
#             return min_count
        
#         ans = dp(amount)
#         return ans if ans < float('inf') else -1 
    
# 125 11
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
         
            dp = [float('inf') for _ in range(amount + 1)]
            dp[0] = 0
            
            for coin in coins:
                for x in range(coin,amount + 1):
                    dp[x] = min(dp[x],dp[x-coin] + 1)
            
            return dp[amount] if dp[amount] != float('inf') else -1
                    