class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        @lru_cache
        def dp(i,isHolding):
            if i == n:
                return 0

            doNothing = dp(i+1,isHolding)
            doSomething = None
            if isHolding == 1:
                doSomething = -fee + prices[i] + dp(i+1,0)
            else:
                doSomething = -prices[i] + dp(i+1,1)

            return max(doSomething,doNothing)	
        return dp(0,0)
