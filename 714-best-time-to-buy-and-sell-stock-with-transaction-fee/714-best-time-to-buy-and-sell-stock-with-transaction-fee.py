# class Solution:
#     def maxProfit(self, prices: List[int], fee: int) -> int:
#         n = len(prices)
#         @lru_cache
#         def dp(i,isHolding):
#             if i == n:
#                 return 0

#             doNothing = dp(i+1,isHolding)
#             doSomething = None
#             if isHolding == 1:
#                 doSomething = -fee + prices[i] + dp(i+1,0)
#             else:
#                 doSomething = -prices[i] + dp(i+1,1)

#             return max(doSomething,doNothing)	
#         return dp(0,0)
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0]*2 for _ in range(n + 1)]
        for i in range(n-1,-1,-1):
            for isHolding in range(2):
                doNothing = dp[i + 1][isHolding]
                doSomething = None
                if isHolding:
                    doSomething =  -fee + prices[i] + dp[i+1][0]
                else:
                    doSomething = - prices[i] + dp[i+1][1]
            
                dp[i][isHolding] = max(doSomething,doNothing)
        
        return dp[0][0]
        